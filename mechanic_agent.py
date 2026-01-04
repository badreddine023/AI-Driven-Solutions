from typing import Any, Dict
from ..agent_framework.base_agent import BaseAgent

class MechanicAgent(BaseAgent):
    """
    An agent that thinks like a mechanic, focusing on vehicle diagnostics and maintenance.
    """
    
    def __init__(self, name: str = "Mechanic"):
        super().__init__(name, "Specializes in vehicle diagnostics, repair suggestions, and maintenance schedules.")

    def execute(self, input_data: Any) -> Dict[str, Any]:
        """
        Analyzes vehicle symptoms or sensor data from a mechanical perspective.
        """
        print(f"Agent {self.name} is inspecting the vehicle data...")
        
        symptoms = input_data.get("symptoms", [])
        mileage = input_data.get("mileage", 0)
        
        diagnosis = []
        recommendations = []
        
        if "strange_noise" in symptoms:
            diagnosis.append("Possible worn-out brake pads or loose belt.")
            recommendations.append("Inspect brake rotors and check belt tension.")
        
        if "engine_vibration" in symptoms:
            diagnosis.append("Potential misfire or unbalanced tires.")
            recommendations.append("Check spark plugs and perform tire balancing.")
            
        if mileage > 50000:
            recommendations.append("Standard 50k-mile service: Change oil, check fluids, and inspect suspension.")

        result = {
            "perspective": "Mechanic",
            "diagnosis": diagnosis if diagnosis else ["No immediate mechanical issues detected."],
            "recommendations": recommendations,
            "urgency": "High" if diagnosis else "Low"
        }
        
        self.update_state("last_inspection", result)
        return result
