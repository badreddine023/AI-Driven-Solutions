from typing import Any, Dict
from ..agent_framework.base_agent import BaseAgent

class PlanningAgent(BaseAgent):
    """
    An agent that makes high-level decisions and plans the vehicle's path.
    """
    
    def __init__(self, name: str = "PathPlanner"):
        super().__init__(name, "Determines the optimal path and speed based on perception and mission goals.")

    def execute(self, input_data: Any) -> Dict[str, Any]:
        """
        Plans the next move based on perception data.
        """
        print(f"Agent {self.name} is calculating the optimal path...")
        
        perception = input_data.get("perception", {})
        detected_objects = perception.get("detected_objects", [])
        
        action = "Maintain Speed"
        target_speed = 50 # km/h
        reasoning = "Clear path ahead."
        
        for obj in detected_objects:
            if obj["type"] == "Pedestrian" and obj["distance"] < 20:
                action = "Emergency Brake"
                target_speed = 0
                reasoning = "Pedestrian detected in close proximity."
                break
            elif obj["distance"] < 30:
                action = "Slow Down"
                target_speed = 20
                reasoning = f"Obstacle ({obj['type']}) detected ahead."

        result = {
            "perspective": "Planning",
            "planned_action": action,
            "target_speed": target_speed,
            "reasoning": reasoning
        }
        
        self.update_state("last_plan", result)
        return result
