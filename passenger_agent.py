from typing import Any, Dict
from ..agent_framework.base_agent import BaseAgent

class PassengerAgent(BaseAgent):
    """
    An agent that represents the passenger's perspective, focusing on comfort and experience.
    """
    
    def __init__(self, name: str = "Passenger"):
        super().__init__(name, "Focuses on cabin comfort, ride quality, and overall passenger experience.")

    def execute(self, input_data: Any) -> Dict[str, Any]:
        """
        Evaluates the ride based on comfort-related parameters.
        """
        print(f"Agent {self.name} is evaluating the passenger experience...")
        
        cabin_temp = input_data.get("cabin_temp", 22)
        ride_smoothness = input_data.get("ride_smoothness", "smooth")
        noise_level = input_data.get("noise_level", "low")
        
        feedback = []
        satisfaction_score = 10
        
        if cabin_temp > 25:
            feedback.append("It's getting a bit warm in here.")
            satisfaction_score -= 2
        elif cabin_temp < 18:
            feedback.append("It's a bit chilly in the cabin.")
            satisfaction_score -= 2
            
        if ride_smoothness == "bumpy":
            feedback.append("The ride is quite rough, feeling every pothole.")
            satisfaction_score -= 3
            
        if noise_level == "high":
            feedback.append("The engine or road noise is distracting.")
            satisfaction_score -= 2

        result = {
            "perspective": "Passenger",
            "feedback": feedback if feedback else ["The ride is very comfortable."],
            "satisfaction_score": max(0, satisfaction_score),
            "requests": ["Adjust AC" if cabin_temp > 25 or cabin_temp < 18 else "None"]
        }
        
        self.update_state("last_experience_report", result)
        return result
