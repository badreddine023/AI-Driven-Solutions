from src.agent_framework.orchestrator import AgentOrchestrator
from src.agents.perception_agent import PerceptionAgent
from src.agents.planning_agent import PlanningAgent
from src.agents.control_agent import ControlAgent
from src.agents.mechanic_agent import MechanicAgent
from src.agents.passenger_agent import PassengerAgent
from src.agents.electronic_engineer_agent import ElectronicEngineerAgent

def run_self_driving_simulation():
    # 1. Initialize Orchestrator
    orchestrator = AgentOrchestrator()

    # 2. Register All Agents
    agents = [
        PerceptionAgent(), PlanningAgent(), ControlAgent(),
        MechanicAgent(), PassengerAgent(), ElectronicEngineerAgent()
    ]
    for agent in agents:
        orchestrator.register_agent(agent)

    # 3. Define Simulation Scenario
    # Scenario: Driving at 50km/h, a pedestrian suddenly appears, while the car has a slight vibration.
    scenario_data = {
        "raw_sensors": {
            "front_camera_object_detected": True,
            "lidar_obstacle_distance": 18,
            "lane_keep_assist_active": True,
            "visibility_index": 0.9
        },
        "vehicle_health": {
            "symptoms": ["engine_vibration"],
            "mileage": 52000,
            "battery_voltage": 12.4,
            "infotainment_cpu_load": 30
        },
        "cabin_environment": {
            "cabin_temp": 22,
            "ride_smoothness": "bumpy",
            "noise_level": "low"
        }
    }

    print("\n" + "="*60)
    print("SELF-DRIVING SYSTEM SIMULATION: FULL STACK ANALYSIS")
    print("="*60)

    # 4. Step-by-Step Execution
    
    # Step A: Perception
    print("\n[PHASE 1: PERCEPTION]")
    perception_result = orchestrator.agents["Perception"].execute(scenario_data)
    print(f"Objects Detected: {[obj['type'] for obj in perception_result['detected_objects']]}")

    # Step B: Planning
    print("\n[PHASE 2: PLANNING]")
    planning_input = {"perception": perception_result}
    planning_result = orchestrator.agents["PathPlanner"].execute(planning_input)
    print(f"Planned Action: {planning_result['planned_action']} (Reason: {planning_result['reasoning']})")

    # Step C: Control
    print("\n[PHASE 3: CONTROL]")
    control_input = {"plan": planning_result}
    control_result = orchestrator.agents["VehicleControl"].execute(control_input)
    print(f"Actuator Commands: {control_result['actuator_commands']}")

    # Step D: Background Monitoring (Mechanic, Passenger, Engineer)
    print("\n[PHASE 4: SYSTEM MONITORING]")
    
    mechanic_res = orchestrator.agents["Mechanic"].execute(scenario_data["vehicle_health"])
    print(f"Mechanic Note: {mechanic_res['diagnosis'][0]}")
    
    passenger_res = orchestrator.agents["Passenger"].execute(scenario_data["cabin_environment"])
    print(f"Passenger Feedback: {passenger_res['feedback'][0]}")
    
    engineer_res = orchestrator.agents["ElectronicEngineer"].execute(scenario_data["vehicle_health"])
    print(f"Engineer Status: {engineer_res['system_status']}")

    print("\n" + "="*60)
    print("SIMULATION COMPLETE: ALL SYSTEMS NOMINAL")
    print("="*60)

if __name__ == "__main__":
    run_self_driving_simulation()
