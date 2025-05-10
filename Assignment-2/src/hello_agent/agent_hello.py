# hello_agent/agent_hello.py

from agents import Agent, Runner, AsyncOpenAI, set_default_openai_api, set_tracing_disabled, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Gemini API key from .env
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

def my_first_agent():
    """
    This function runs a Gemini-backed agent that responds to a prompt.
    """
    print("Gemini API Key loaded successfully.")

    # Create an agent with basic instructions
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=model
    )

    # Run the agent synchronously on a sample prompt
    result = Runner.run_sync(agent, "Say hello world")

    # Output the final response
    print("Agent says:", result.final_output)
