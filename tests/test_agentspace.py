import asyncio
import pytest
from agentspace import AgentManager

"""
This test file uses the `pytest` testing framework and includes the following tests:

1. `test_create_agent`: Tests the creation of an agent using the `create_agent` method of the `AgentManager`. It verifies that the created agent has the correct name and skills, and that it is added to the `agents` dictionary of the `AgentManager`.
2. `test_create_duplicate_agent`: Tests the behavior when attempting to create an agent with a duplicate name. It verifies that a `ValueError` is raised when trying to create an agent with the same name as an existing agent.
3. `test_assign_task_to_agent`: Tests the assignment of a task to an agent using the `assign_task_to_agent` method of the `AgentManager`. It creates an agent, assigns a test task to it, and runs the agents using the `run_agents` method.
4. `test_assign_task_to_nonexistent_agent`: Tests the behavior when attempting to assign a task to a nonexistent agent. It verifies that a `ValueError` is raised when trying to assign a task to an agent that does not exist.
5. `test_run_agents`: Tests the concurrent execution of agents using the `run_agents` method of the `AgentManager`. It creates multiple agents, assigns tasks to them, and runs the agents concurrently.

To run these tests, make sure you have `pytest` installed (`pip install pytest`) and run the following command in the terminal:
pytest tests/test_agentspace.py

The tests will be executed, and the results will be displayed in the terminal, indicating which tests passed or failed.
"""

@pytest.fixture
def agent_manager():
    return AgentManager()

@pytest.mark.asyncio
async def test_create_agent(agent_manager):
    agent = agent_manager.create_agent("TestAgent", ["skill1", "skill2"])
    assert agent.name == "TestAgent"
    assert agent.skills == ["skill1", "skill2"]
    assert agent_manager.agents["TestAgent"] == agent

@pytest.mark.asyncio
async def test_create_duplicate_agent(agent_manager):
    agent_manager.create_agent("TestAgent", ["skill1", "skill2"])
    with pytest.raises(ValueError):
        agent_manager.create_agent("TestAgent", ["skill3", "skill4"])

@pytest.mark.asyncio
async def test_assign_task_to_agent(agent_manager):
    agent = agent_manager.create_agent("TestAgent", ["skill1", "skill2"])
    
    async def test_task():
        print("TestAgent: Executing test task...")
    
    await agent_manager.assign_task_to_agent("TestAgent", test_task)
    await agent_manager.run_agents()

@pytest.mark.asyncio
async def test_assign_task_to_nonexistent_agent(agent_manager):
    async def test_task():
        print("TestAgent: Executing test task...")
    
    with pytest.raises(ValueError):
        await agent_manager.assign_task_to_agent("NonexistentAgent", test_task)

@pytest.mark.asyncio
async def test_run_agents(agent_manager):
    agent1 = agent_manager.create_agent("Agent1", ["skill1", "skill2"])
    agent2 = agent_manager.create_agent("Agent2", ["skill3", "skill4"])
    
    async def task1():
        print("Agent1: Executing task1...")
    
    async def task2():
        print("Agent2: Executing task2...")
    
    await agent_manager.assign_task_to_agent("Agent1", task1)
    await agent_manager.assign_task_to_agent("Agent2", task2)
    await agent_manager.run_agents()
