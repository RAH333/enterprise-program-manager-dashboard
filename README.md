# enterprise-program-manager-dashboard

Enterprise Program Management & COE Analytics Dashboard. 

The project showcase cross-functional coordination, data analytics, and operational tracking across engineering, manufacturing, and sourcing.

This project demonstrates your ability to track business metrics, manage stakeholder dependencies, and generate actionable insights for leadership reviews.

# Enterprise Program Management & COE Analytics Dashboard

An interactive, data-driven PMO tracking tool designed for managing cross-functional programs across Engineering, Manufacturing, Sourcing, and Facilities.

## Key Features Demonstrated
- **Executive Dashboards**: High-level KPIs mapping milestone completion and budget variances.
- **Cross-Functional Governance**: Financial and delivery metrics broken down by department lines.
- **Risk Mitigation**: Proactive isolation of tracking dependencies and high-risk operations.

## How to Run Locally
1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Launch the dashboard: `streamlit run src/app.py`
4. 

```
enterprise-program-manager-dashboard/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── config/
│   └── settings.py
│
├── data/
│   ├── raw/
│   │   └── program_metrics_raw.csv
│   └── processed/
│       └── cleaned_metrics.csv
│
├── src/
│   ├── __init__.py
│   ├── data_processor.py
│   ├── analytics_engine.py
│   └── app.py
│
├── tests/
│   └── test_analytics.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

