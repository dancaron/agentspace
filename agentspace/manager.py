from typing import Callable, Dict
from .agent import Agent

class AgentManager:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}

    def create_agent(self, name: str, skills: List[str]) -> Agent:
        agent = Agent(name, skills)
        self.agents[name] = agent
        return agent

    async def run_agents(self):
        tasks = []
        for agent in self.agents.values():
            tasks.append(asyncio.create_task(agent.run()))
        await asyncio.gather(*tasks)

    async def assign_task_to_agent(self, agent_name: str, task: Callable):
        agent = self.agents.get(agent_name)
        if agent:
            await agent.assign_task(task)
        else:
            raise ValueError(f"Agent '{agent_name}' not found.")
