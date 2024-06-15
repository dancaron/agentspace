import asyncio
from typing import Callable, List

class Agent:
    def __init__(self, name: str, skills: List[str]):
        self.name = name
        self.skills = skills
        self.tasks = asyncio.Queue()

    async def run(self):
        while True:
            task = await self.tasks.get()
            await task()
            self.tasks.task_done()

    async def assign_task(self, task: Callable):
        await self.tasks.put(task)
