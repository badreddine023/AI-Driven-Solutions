from typing import Any, Dict
from ..agent_framework.base_agent import BaseAgent

class ControlAgent(BaseAgent):
    """
    An agent that translates plans into low-level vehicle commands (steering, throttle, brake).
    """
    
    def __init__(self, name: str = "VehicleControl"):
        super().__init__(name, "Executes steering, acceleration, and braking commands.")

    def execute(self, input_data: Any) -> Dict[str, Any]:
        """
        Translates the plan into actuator commands.
        """
        print(f"Agent {self.name} is sending commands to actuators...")
        
        plan = input_data.get("plan", {})
        action = plan.get("planned_action", "Maintain Speed")
        
        commands = {
            "throttle": 0,
            "brake": 0,
            "steering_angle": 0
        }
        
        if action == "Maintain Speed":
            commands["throttle"] = 0.3
        elif action == "Slow Down":
            commands["brake"] = 0.4
        elif action == "Emergency Brake":
            commands["brake"] = 1.0
            commands["throttle"] = 0

        result = {
            "perspective": "Control",
            "actuator_commands": commands,
            "execution_status": "Success"
        }
        
        self.update_state("last_commands", result)
        return result
