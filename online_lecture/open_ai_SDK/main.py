from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

value = 123

greeting_agent = Agent(
    name="greeting agent",
    instructions="You are a helpful assistant that greets users. your task in to say salam, when someone says hello, hi or anything similar.",
    )

input_value = input("Enter a value: ")

agent_result = Runner.run_sync(greeting_agent, input_value)
print(agent_result.final_output)