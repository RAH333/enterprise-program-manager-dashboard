import pandas as pd

class AnalyticsEngine:
    @staticmethod
    def get_executive_summary(df):
        """Generates high-level metrics for leadership dashboards."""
        summary = {
            "total_programs": int(df['Project_ID'].count()),
            "total_budget": float(df['Budget_Allocated'].sum()),
            "total_spent": float(df['Budget_Spent'].sum()),
            "average_completion": float(df['Milestone_Completion_Rate'].mean()),
            "high_risk_count": int(df[df['Risk_Level'] == 'High']['Project_ID'].count())
        }
        return summary

    @staticmethod
    def get_department_performance(df):
        """Aggregates metrics by department for cross-functional reviews."""
        return df.groupby('Department').agg({
            'Budget_Allocated': 'sum',
            'Budget_Spent': 'sum',
            'Milestone_Completion_Rate': 'mean'
        }).reset_index()
      
