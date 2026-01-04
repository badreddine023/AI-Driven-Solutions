import unittest
from src.agents.mechanic_agent import MechanicAgent
from src.agents.passenger_agent import PassengerAgent
from src.agents.electronic_engineer_agent import ElectronicEngineerAgent
from src.agents.perception_agent import PerceptionAgent
from src.agents.planning_agent import PlanningAgent
from src.agents.control_agent import ControlAgent

class TestAgents(unittest.TestCase):

    def test_mechanic_agent(self):
        agent = MechanicAgent()
        input_data = {"symptoms": ["strange_noise"], "mileage": 60000}
        result = agent.execute(input_data)
        self.assertEqual(result["perspective"], "Mechanic")
        self.assertIn("Possible worn-out brake pads or loose belt.", result["diagnosis"])
        self.assertTrue(len(result["recommendations"]) > 0)

    def test_passenger_agent(self):
        agent = PassengerAgent()
        input_data = {"cabin_temp": 30, "ride_smoothness": "bumpy"}
        result = agent.execute(input_data)
        self.assertEqual(result["perspective"], "Passenger")
        self.assertLess(result["satisfaction_score"], 10)
        self.assertIn("It's getting a bit warm in here.", result["feedback"])

    def test_electronic_engineer_agent(self):
        agent = ElectronicEngineerAgent()
        input_data = {"battery_voltage": 10.5, "sensor_errors": ["GPS Failure"]}
        result = agent.execute(input_data)
        self.assertEqual(result["perspective"], "Electronic Engineer")
        self.assertEqual(result["system_status"], "Critical")
        self.assertTrue(any("Low battery voltage" in alert for alert in result["telemetry_alerts"]))

    def test_perception_agent(self):
        agent = PerceptionAgent()
        input_data = {"raw_sensors": {"front_camera_object_detected": True, "lidar_obstacle_distance": 10}}
        result = agent.execute(input_data)
        self.assertEqual(result["perspective"], "Perception")
        detected_types = [obj["type"] for obj in result["detected_objects"]]
        self.assertIn("Pedestrian", detected_types)
        self.assertIn("Static Obstacle", detected_types)

    def test_planning_agent(self):
        agent = PlanningAgent()
        input_data = {"perception": {"detected_objects": [{"type": "Pedestrian", "distance": 5}]}}
        result = agent.execute(input_data)
        self.assertEqual(result["perspective"], "Planning")
        self.assertEqual(result["planned_action"], "Emergency Brake")
        self.assertEqual(result["target_speed"], 0)

    def test_control_agent(self):
        agent = ControlAgent()
        input_data = {"plan": {"planned_action": "Emergency Brake"}}
        result = agent.execute(input_data)
        self.assertEqual(result["perspective"], "Control")
        self.assertEqual(result["actuator_commands"]["brake"], 1.0)
        self.assertEqual(result["actuator_commands"]["throttle"], 0)

if __name__ == "__main__":
    unittest.main()
