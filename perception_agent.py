from typing import Any, Dict, List
from ..agent_framework.base_agent import BaseAgent

class PerceptionAgent(BaseAgent):
    """
    An agent that handles environmental perception, identifying obstacles, lanes, and signs.
    """
    
    def __init__(self, name: str = "Perception"):
        super().__init__(name, "Processes sensor data to identify objects, lane markings, and traffic signals.")

    def execute(self, input_data: Any) -> Dict[str, Any]:
        """
        Simulates processing camera and LiDAR data.
        """
        print(f"Agent {self.name} is processing sensor streams...")
        
        raw_sensors = input_data.get("raw_sensors", {})
        detected_objects = []
        
        # Simulated detection logic
        if raw_sensors.get("front_camera_object_detected"):
            detected_objects.append({"type": "Pedestrian", "distance": 15, "confidence": 0.98})
            
        if raw_sensors.get("lidar_obstacle_distance", 100) < 20:
            detected_objects.append({"type": "Static Obstacle", "distance": raw_sensors["lidar_obstacle_distance"], "confidence": 0.95})

        result = {
            "perspective": "Perception",
            "detected_objects": detected_objects,
            "lane_status": "Centered" if raw_sensors.get("lane_keep_assist_active") else "Drifting",
            "visibility": raw_sensors.get("visibility_index", 1.0)
        }
        
        self.update_state("last_perception_frame", result)
        return result
