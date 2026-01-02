import pandas as pd
import numpy as np
from typing import Any, Dict
from ..agent_framework.base_agent import BaseAgent

class DataAnalyzerAgent(BaseAgent):
    """
    An agent that performs basic statistical analysis on a given dataset.
    """
    
    def __init__(self, name: str = "DataAnalyzer"):
        super().__init__(name, "Performs statistical analysis on data.")

    def execute(self, input_data: Any) -> Dict[str, Any]:
        """
        Expects a dictionary or a path to a CSV file.
        Returns a summary of the data.
        """
        print(f"Agent {self.name} is analyzing data...")
        
        if isinstance(input_data, str):
            # Assume it's a file path
            df = pd.read_csv(input_data)
        elif isinstance(input_data, dict):
            # Assume it's raw data
            df = pd.DataFrame(input_data)
        elif isinstance(input_data, pd.DataFrame):
            df = input_data
        else:
            raise ValueError("Input data must be a file path, a dictionary, or a pandas DataFrame.")

        # Perform analysis
        summary = {
            "row_count": len(df),
            "column_count": len(df.columns),
            "columns": list(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
            "basic_stats": df.describe(include=[np.number]).to_dict() if not df.select_dtypes(include=[np.number]).empty else "No numeric columns found."
        }
        
        self.update_state("last_analysis_summary", summary)
        return summary
