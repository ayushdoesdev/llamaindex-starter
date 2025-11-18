from dotenv import dotenv_values

import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI

openAPIKey = dotenv_values()["OPENAI_API_KEY"]

# define simple calculator operations
def multiply(a: float, b: float) -> float:
    return a * b

# Create an agent workflow with our calculator tool
agent = FunctionAgent(
    tools=[multiply],
    llm=OpenAI(model="gpt-4o-mini", api_key=openAPIKey),
    system_prompt="You are a helpful assistant that can multiply two numbers.",
)

async def main():
    response = await agent.run("What is 7986778 * 232323")
    print(str(response))


if __name__ == "__main__":
    asyncio.run(main())