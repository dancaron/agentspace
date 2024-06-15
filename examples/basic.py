import asyncio
from agentspace import AgentManager

"""
In this example, we demonstrate the basic usage of the `AgentSpace` package. Here's a step-by-step explanation:

1. We import the necessary modules: `asyncio` for asynchronous programming and `AgentManager` from the `agentspace` package.
2. We define an asynchronous `main` function that serves as the entry point of our example.
3. Inside the `main` function, we create an instance of `AgentManager` called `manager`. This will be used to manage our agents.
4. We create two agents using the `create_agent` method of the `manager`. Each agent is given a name and a list of skills.
5. We define two asynchronous tasks, `task1` and `task2`, which simulate some work performed by the agents. In this example, `task1` represents data analysis and report generation, while `task2` represents web scraping and data cleaning. We use `asyncio.sleep` to simulate some processing time.
6. We assign the tasks to the respective agents using the `assign_task_to_agent` method of the `manager`. We specify the name of the agent and the task to be assigned.
7. Finally, we run the agents using the `run_agents` method of the `manager`. This starts all the agents concurrently and waits for them to complete their tasks.
8. The `if __name__ == "__main__":` block ensures that the `main` function is executed only when the script is run directly (not imported as a module). We use `asyncio.run` to run the asynchronous `main` function.

When you run this example script, you should see output similar to the following:

Agent1: Performing data analysis...
Agent2: Scraping web data...
Agent1: Generating report...
Agent1: Task completed.
Agent2: Cleaning scraped data...
Agent2: Task completed.

This demonstrates how the agents concurrently perform their assigned tasks using the `AgentSpace` package.
"""

async def main():
    manager = AgentManager()

    # Create agents
    agent1 = manager.create_agent("Agent1", ["data_analysis", "report_generation"])
    agent2 = manager.create_agent("Agent2", ["web_scraping", "data_cleaning"])

    # Define tasks
    async def task1():
        print("Agent1: Performing data analysis...")
        await asyncio.sleep(2)
        print("Agent1: Generating report...")
        await asyncio.sleep(1)
        print("Agent1: Task completed.")

    async def task2():
        print("Agent2: Scraping web data...")
        await asyncio.sleep(3)
        print("Agent2: Cleaning scraped data...")
        await asyncio.sleep(1)
        print("Agent2: Task completed.")

    # Assign tasks to agents
    await manager.assign_task_to_agent("Agent1", task1)
    await manager.assign_task_to_agent("Agent2", task2)

    # Run agents
    await manager.run_agents()

if __name__ == "__main__":
    asyncio.run(main())
