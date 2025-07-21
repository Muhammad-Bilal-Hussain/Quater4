# from dotenv import load_dotenv
# load_dotenv()
# from agents import Agent, Runner
# from openai import AsyncOpenAI

# gemini_api_key = os.getenv('GEMINI_API_KEY')

# client = AsyncOpenAI(
#     api_key= gemini_api_key,
#     base_url=''
# )

# agent = Agent(
#     name="Assistant",
#     instructions="you are a helpful assistant"
# )

# prompt = "hello, How are You?"

# runner = Runner.run_sync(agent,prompt)
# print(runner.final_output)




























import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

gemini_api_key = "AIzaSyBaYQEjA0jz2F-k_J6AWl7I9NEobSRqejE"

#Reference: https://ai.google.dev/gemini-api/docs/openai
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )

    result = await Runner.run(
        agent,
        "Tell me about recursion in programming.",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())