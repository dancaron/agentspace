from typing import Callable, Dict
from .agent import Agent

class AgentManager:
    """
    Manages the creation and coordination of agents.

    The AgentManager class provides methods to create agents, assign tasks to agents,
    and run agents concurrently.

    Attributes:
        agents (Dict[str, Agent]): A dictionary mapping agent names to Agent instances.
    """

    def __init__(self):
        """
        Initialize an AgentManager instance.
        """
        self.agents: Dict[str, Agent] = {}

    def create_agent(self, name: str, skills: List[str]) -> Agent:
        """
        Create a new agent with the specified name and skills.

        Args:
            name (str): The name of the agent.
            skills (List[str]): The list of skills possessed by the agent.

        Returns:
            Agent: The created Agent instance.

        Raises:
            ValueError: If an agent with the same name already exists.
        """
        if name in self.agents:
            raise ValueError(f"Agent with name '{name}' already exists.")

        agent = Agent(name, skills)
        self.agents[name] = agent
        return agent

    async def run_agents(self):
        """
        Run all agents concurrently.

        This method creates a task for each agent's run() method and runs them concurrently
        using asyncio.gather().
        """
        tasks = []
        for agent in self.agents.values():
            tasks.append(asyncio.create_task(agent.run()))
        await asyncio.gather(*tasks)

    async def assign_task_to_agent(self, agent_name: str, task: Callable):
        """
        Assign a task to the specified agent.

        Args:
            agent_name (str): The name of the agent to assign the task to.
            task (Callable): The task to be assigned to the agent.

        Raises:
            ValueError: If the specified agent does not exist.
        """
        agent = self.agents.get(agent_name)
        if agent:
            await agent.assign_task(task)
        else:
            raise ValueError(f"Agent '{agent_name}' not found.")
