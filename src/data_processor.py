import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_and_clean_data(self):
        """Loads raw program management data and computes key execution metrics."""
        try:
            df = pd.read_csv(self.file_path)
            
            # Data Transformation & Business Logic
            df['Budget_Variance'] = df['Budget_Allocated'] - df['Budget_Spent']
            df['Milestone_Completion_Rate'] = (df['Milestones_Completed'] / df['Milestones_Total'] * 100).round(2)
            
            # flag budget overruns
            df['Budget_Status'] = np.where(df['Budget_Variance'] < 0, 'Over Budget', 'Within Budget')
            
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()
          
