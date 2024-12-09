import logfire
from dotenv import load_dotenv
import os
from pydantic_ai import Agent, RunContext
import asyncio
import datetime
import random

logfire.configure()
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
agent = Agent(
    "gemini-1.5-flash",
    deps_type=str,
    system_prompt=(
        "You're a dice game, you should roll the die and see if the number ",
        "you get back matches the user's guess. If so, tell them they're a winner.",
        "Use the player's name in the response.",
        "You should also tell the user the date and time.",
    ),
)


@agent.tool_plain
def roll_die() -> str:
    """Roll a six-sided die and return the result."""
    return str(random.randint(1, 6))


@agent.tool
def get_player_name(ctx: RunContext[str]) -> str:
    """Get the player's name."""
    return ctx.deps


@agent.system_prompt
def add_the_users_name(ctx: RunContext[str]) -> str:
    return f"Hello {ctx.deps}!"


@agent.system_prompt
def add_the_date() -> str:
    return f"Today is {datetime.datetime.now().strftime('%Y-%m-%d')}"


async def main():
    dice_result = await agent.run(f"My guess is {roll_die()}", deps="Alice")
    print(dice_result.data)


if __name__ == "__main__":
    asyncio.run(main())
