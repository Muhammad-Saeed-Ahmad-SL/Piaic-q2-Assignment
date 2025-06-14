import chainlit as cl
from agent import call_openrouter_api, tools
import json

@cl.on_chat_start
async def start():
    cl.user_session.set("chat_history", [])
    await cl.Message("👋 Welcome! Ask me anything.").send()

@cl.on_message
async def handle_msg(message: cl.Message):
    history = cl.user_session.get("chat_history") or []

    msg = cl.Message(content="💭 Thinking...")
    await msg.send()

    content = message.content

    # Tool command check
    if content.startswith("/"):
        cmd, *args = content[1:].split()
        tool = tools.get(cmd)
        if tool:
            result = tool.run(" ".join(args))
            msg.content = result
            await msg.update()

            history.append({"role": "user", "content": content})
            history.append({"role": "assistant", "content": result})
            cl.user_session.set("chat_history", history)
            return

    # Chatbot response
    try:
        response = call_openrouter_api(content, history)
        msg.content = response
        await msg.update()

        history.append({"role": "user", "content": content})
        history.append({"role": "assistant", "content": response})
        cl.user_session.set("chat_history", history)

    except Exception as e:
        msg.content = f"❌ Error: {str(e)}"
        await msg.update()

@cl.on_chat_end
async def save_history():
    history = cl.user_session.get("chat_history") or []
    with open("chat_history.json", "w") as f:
        json.dump(history, f, indent=4)
