from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BaseAgent(ABC):
    """
    Abstract base class for all AI agents in the framework.
    Defines the core interface for agent initialization, execution, and state management.
    """
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.state: Dict[str, Any] = {}

    @abstractmethod
    def execute(self, input_data: Any) -> Any:
        """
        The main execution logic for the agent.
        
        :param input_data: The data or task to be processed by the agent.
        :return: The result of the agent's execution.
        """
        pass

    def get_state(self) -> Dict[str, Any]:
        """
        Returns the current state of the agent.
        """
        return self.state

    def update_state(self, key: str, value: Any):
        """
        Updates a specific key in the agent's state.
        """
        self.state[key] = value

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name='{self.name}')>"

# Example of a simple data structure for agent communication (optional, but good practice)
class AgentMessage:
    def __init__(self, sender: str, content: Any, metadata: Dict[str, Any] = None):
        self.sender = sender
        self.content = content
        self.metadata = metadata if metadata is not None else {}

    def __repr__(self) -> str:
        return f"AgentMessage(sender='{self.sender}', content='{str(self.content)[:30]}...')"
