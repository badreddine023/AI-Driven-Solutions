from src.agent_framework.orchestrator import AgentOrchestrator
from src.agents.mechanic_agent import MechanicAgent
from src.agents.passenger_agent import PassengerAgent
from src.agents.electronic_engineer_agent import ElectronicEngineerAgent

def run_vehicle_scenario():
    # 1. Initialize Orchestrator
    orchestrator = AgentOrchestrator()

    # 2. Register Specialized Agents
    mechanic = MechanicAgent()
    passenger = PassengerAgent()
    engineer = ElectronicEngineerAgent()
    
    orchestrator.register_agent(mechanic)
    orchestrator.register_agent(passenger)
    orchestrator.register_agent(engineer)

    # 3. Define Scenario Data
    # A scenario where the car has a strange noise, high cabin temp, and low battery voltage.
    vehicle_data = {
        "symptoms": ["strange_noise"],
        "mileage": 55000,
        "cabin_temp": 28,
        "ride_smoothness": "smooth",
        "noise_level": "medium",
        "battery_voltage": 11.2,
        "sensor_errors": ["O2 Sensor Signal Intermittent"],
        "infotainment_cpu_load": 45
    }

    print("\n" + "="*50)
    print("VEHICLE DIAGNOSTIC SCENARIO: MULTI-PERSPECTIVE ANALYSIS")
    print("="*50)

    # 4. Run Individual Analysis (Simulating a parallel or sequential check)
    perspectives = ["Mechanic", "Passenger", "ElectronicEngineer"]
    
    for agent_name in perspectives:
        print(f"\n--- Consulting {agent_name} ---")
        result = orchestrator.agents[agent_name].execute(vehicle_data)
        
        if agent_name == "Mechanic":
            print(f"Diagnosis: {', '.join(result['diagnosis'])}")
            print(f"Recommendations: {', '.join(result['recommendations'])}")
        elif agent_name == "Passenger":
            print(f"Satisfaction Score: {result['satisfaction_score']}/10")
            print(f"Feedback: {', '.join(result['feedback'])}")
        elif agent_name == "ElectronicEngineer":
            print(f"System Status: {result['system_status']}")
            print(f"Alerts: {', '.join(result['telemetry_alerts'])}")
            print(f"Technical Notes: {result['technical_notes']}")

    print("\n" + "="*50)
    print("SUMMARY REPORT GENERATED")
    print("="*50)

if __name__ == "__main__":
    run_vehicle_scenario()
