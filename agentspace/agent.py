import asyncio
from typing import Callable, List

class Agent:
    """
    Represents an agent with a name, skills, and a task queue.
    """

    def __init__(self, name: str, skills: List[str]):
        """
        Initialize an Agent instance.

        Args:
            name (str): The name of the agent.
            skills (List[str]): The list of skills possessed by the agent.
        """
        self.name = name
        self.skills = skills
        self.tasks = asyncio.Queue()

    async def run(self):
        """
        Run the agent and process tasks from the task queue.

        The agent continuously retrieves tasks from its queue and executes them.
        """
        while True:
            task = await self.tasks.get()
            await task()
            self.tasks.task_done()

    async def assign_task(self, task: Callable):
        """
        Assign a task to the agent's task queue.

        Args:
            task (Callable): The task to be assigned to the agent.
        """
        await self.tasks.put(task)
