import chainlit as cl
import json
from datetime import datetime
from my_secrets import Secrets
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_api, set_tracing_disabled, OpenAIChatCompletionsModel

# Track entire conversation
chat_history = []

@cl.on_chat_start
async def setup():
    secrets = Secrets()
    external_client = AsyncOpenAI(
        api_key=secrets.get_api_key(),
        base_url=secrets.get_api_base_url()
    )
    set_tracing_disabled(True)
    set_default_openai_api(external_client)

    cl.user_session.set("agent", Agent(
        name="ConceptGuru",
        instructions="""
        You are ConceptGuru, a helpful and clear AI tutor who explains complex topics simply.
        Use analogies, examples, and never use jargon. Always ask:
        'Would you like a deeper explanation or an example?'
        """,
        model=OpenAIChatCompletionsModel(
            model=secrets.get_api_model(),
            openai_client=external_client
        )
    ))

@cl.on_message
async def main(msg: cl.Message):
    agent = cl.user_session.get("agent")
    result = Runner.run_sync(agent, msg.content)
    response = result.final_output

    # Log to chat history
    chat_history.append({
        "user": msg.content,
        "assistant": response,
        "timestamp": datetime.now().isoformat()
    })

    await cl.Message(content=response).send()

@cl.on_chat_end
def save_history():
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(chat_history, f, indent=4, ensure_ascii=False)
