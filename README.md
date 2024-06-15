# AgentSpace

![AgentSpace](https://img.shields.io/badge/Agent-Space-blue)
![ML/AI](https://img.shields.io/badge/ML-AI-blue)
![Python](https://img.shields.io/badge/Python-yellow)

AgentSpace is a compact and easy-to-use agent framework for building agent-based systems in Python. It provides a simple way to create and manage agents, assign tasks to agents, and run agents concurrently.

## Features

- Create agents with specific names and skills
- Assign tasks to agents
- Run agents concurrently
- Lightweight and easy to integrate into existing projects
- Asyncio-based for efficient concurrent execution

## Installation

You can install AgentSpace using pip:

```
pip install agentspace
```

## Usage

Here's a basic example of how to use AgentSpace:

```python
import asyncio
from agentspace import AgentManager

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
```

## Documentation

For detailed documentation and API reference, please visit the [AgentSpace Documentation](https://github.com/dancaron/agentspace/wiki).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/yourusername/agentspace).

## License

AgentSpace is released under the [MIT License](https://github.com/dancaron/agentspace/blob/main/LICENSE).

## Contact

If you have any questions or inquiries, please contact the maintainer:

Dan Caron
GitHub: [dancaron](https://github.com/dancaron)
