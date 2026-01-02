from typing import Dict, Any, List
from .base_agent import BaseAgent, AgentMessage

class AgentOrchestrator:
    """
    Manages a collection of agents and orchestrates their communication and execution flow.
    """
    
    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}
        self.message_log: List[AgentMessage] = []

    def register_agent(self, agent: BaseAgent):
        """
        Registers an agent with the orchestrator.
        """
        if agent.name in self.agents:
            raise ValueError(f"Agent with name '{agent.name}' is already registered.")
        self.agents[agent.name] = agent
        print(f"Agent '{agent.name}' registered.")

    def run_workflow(self, initial_task: Any, workflow: List[str]) -> Any:
        """
        Executes a predefined sequence of agents (a workflow).
        
        :param initial_task: The starting input for the first agent.
        :param workflow: A list of agent names defining the execution order.
        :return: The final output from the last agent in the workflow.
        """
        current_data = initial_task
        
        for agent_name in workflow:
            if agent_name not in self.agents:
                raise ValueError(f"Agent '{agent_name}' not found in registered agents.")
            
            agent = self.agents[agent_name]
            
            # Log the incoming message/data
            incoming_message = AgentMessage(
                sender="Orchestrator" if not self.message_log else self.message_log[-1].sender,
                content=current_data,
                metadata={"target_agent": agent_name}
            )
            self.message_log.append(incoming_message)
            print(f"Orchestrator passing data to {agent.name}...")
            
            # Execute the agent
            try:
                result = agent.execute(current_data)
                current_data = result
                
                # Log the outgoing message/result
                outgoing_message = AgentMessage(
                    sender=agent_name,
                    content=result,
                    metadata={"status": "success"}
                )
                self.message_log.append(outgoing_message)
                print(f"Agent {agent.name} finished execution.")
                
            except Exception as e:
                error_message = AgentMessage(
                    sender=agent_name,
                    content=f"Execution failed: {e}",
                    metadata={"status": "error"}
                )
                self.message_log.append(error_message)
                print(f"Agent {agent.name} failed: {e}")
                raise
                
        return current_data

    def get_log(self) -> List[AgentMessage]:
        """
        Returns the full message log of the orchestration process.
        """
        return self.message_log
