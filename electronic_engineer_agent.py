from typing import Any, Dict
from ..agent_framework.base_agent import BaseAgent

class ElectronicEngineerAgent(BaseAgent):
    """
    An agent that thinks like an electronic engineer, focusing on sensors, circuits, and software.
    """
    
    def __init__(self, name: str = "ElectronicEngineer"):
        super().__init__(name, "Specializes in electronic control units (ECUs), sensor health, and system telemetry.")

    def execute(self, input_data: Any) -> Dict[str, Any]:
        """
        Analyzes electronic system health and sensor readings.
        """
        print(f"Agent {self.name} is monitoring electronic systems...")
        
        voltage = input_data.get("battery_voltage", 12.6)
        sensor_errors = input_data.get("sensor_errors", [])
        cpu_load = input_data.get("infotainment_cpu_load", 20)
        
        system_status = "Healthy"
        alerts = []
        
        if voltage < 11.5:
            system_status = "Critical"
            alerts.append("Low battery voltage detected. Potential alternator failure.")
            
        if sensor_errors:
            system_status = "Degraded"
            for error in sensor_errors:
                alerts.append(f"Sensor Error: {error}")
                
        if cpu_load > 90:
            alerts.append("High CPU load on infotainment system. Potential software lag.")

        result = {
            "perspective": "Electronic Engineer",
            "system_status": system_status,
            "telemetry_alerts": alerts if alerts else ["All electronic systems nominal."],
            "technical_notes": f"Battery: {voltage}V, CPU: {cpu_load}%"
        }
        
        self.update_state("last_telemetry_scan", result)
        return result
