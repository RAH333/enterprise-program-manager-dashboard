import streamlit as st
import pandas as pd
import plotly.express as px
from data_processor import DataProcessor
from analytics_engine import AnalyticsEngine

# Page configurations
st.set_page_config(page_title="Executive PMO Dashboard", layout="wide")
st.title("Enterprise Program Management & COE Analytics")
st.subheader("Cross-Functional Operations & Risk Tracking Portal")

# Initialize and Process Data
processor = DataProcessor("data/raw/program_metrics_raw.csv")
df = processor.load_and_clean_data()
metrics = AnalyticsEngine.get_executive_summary(df)

# Top row metrics cards (Executive Review Style)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Portfolios", metrics["total_programs"])
col2.metric("Total Budget Allocated", f"${metrics['total_budget']:,}")
col3.metric("Avg Milestone Completion", f"{metrics['average_completion']:.1f}%")
col4.metric("High-Risk Dependencies", metrics["high_risk_count"], delta_color="inverse")

st.markdown("---")

# Visual Analytics Section
left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Budget vs Spent by Department")
    fig_budget = px.bar(df, x='Department', y=['Budget_Allocated', 'Budget_Spent'], 
                        barmode='group', title="Financial Overview")
    st.plotly_chart(fig_budget, use_container_width=True)

with right_chart:
    st.subheader("Program Risk & Execution Status")
    fig_risk = px.scatter(df, x='Milestone_Completion_Rate', y='Budget_Variance',
                          color='Risk_Level', size='Budget_Allocated', hover_name='Project_Name',
                          title="Milestone Progress vs Budget Variance")
    st.plotly_chart(fig_risk, use_container_width=True)

# Master Data Table with Critical Escalation Highlighting
st.subheader("Cross-Functional Master Tracking Matrix")
st.dataframe(df.style.highlight_max(axis=0, subset=['Budget_Spent']), use_container_width=True)
