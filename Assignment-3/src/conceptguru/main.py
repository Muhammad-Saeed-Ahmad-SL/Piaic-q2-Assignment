from agents import Agent, Runner, AsyncOpenAI, set_default_openai_api, set_tracing_disabled, OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv

load_dotenv()

# Get API Key from .env
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure external OpenAI-compatible client (Gemini in this case)
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Set this client as the default and disable tracing
set_default_openai_api(external_client)
set_tracing_disabled(True)


# Use the OpenAI-compatible model name for Gemini
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

# Define the agent
conceptguru = Agent(
    name="ConceptGuru",
    instructions="""
    You are ConceptGuru, an AI teacher who explains complex ideas in simple words.
    Use clear examples, analogies, and avoid jargon.
    Always end with: 'Would you like a deeper explanation or an example?'
    """,
    model=model,
)

# Run the agent on a sample question
result = Runner.run_sync(conceptguru, "Explain recursion in programming.")
print(result.final_output)

question = "Explain recursion in programming."
result = Runner.run_sync(conceptguru, question)

print(f"\n🧠 Input Question: {question}")
print(f"\n📘 ConceptGuru Response:\n{result.final_output}")

with open("output.md", "w", encoding="utf-8") as f:
    f.write("# ConceptGuru Agent Response\n\n")
    f.write(f"**Question:** {question}\n\n")
    f.write(f"**Response:**\n{result.final_output}")