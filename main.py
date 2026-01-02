import pandas as pd
from src.agent_framework.orchestrator import AgentOrchestrator
from src.agents.data_analyzer import DataAnalyzerAgent

def main():
    # 1. Initialize the Orchestrator
    orchestrator = AgentOrchestrator()

    # 2. Register Agents
    analyzer = DataAnalyzerAgent()
    orchestrator.register_agent(analyzer)

    # 3. Prepare Sample Data
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, 35, 40, 45],
        "Salary": [50000, 60000, 70000, 80000, 90000],
        "Department": ["HR", "Engineering", "Engineering", "Sales", "HR"]
    }
    
    # 4. Define and Run Workflow
    print("\n--- Starting AI-Driven Workflow ---")
    workflow = ["DataAnalyzer"]
    
    try:
        final_result = orchestrator.run_workflow(data, workflow)
        
        print("\n--- Workflow Completed Successfully ---")
        print("Final Analysis Result:")
        print(f"Total Rows: {final_result['row_count']}")
        print(f"Columns: {', '.join(final_result['columns'])}")
        print("\nMissing Values Check:")
        for col, count in final_result['missing_values'].items():
            print(f"  - {col}: {count}")
            
    except Exception as e:
        print(f"\nWorkflow failed: {e}")

if __name__ == "__main__":
    main()
