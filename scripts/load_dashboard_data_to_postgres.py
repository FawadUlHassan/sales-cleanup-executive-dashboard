import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, text

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DASHBOARD_PATH = PROJECT_ROOT / "data" / "processed" / "dashboard"

DB_URL = "postgresql+psycopg2://admin:agency_password@localhost:5433/ecomm_analytics"
SCHEMA_NAME = "sales_dashboard"

engine = create_engine(DB_URL)

files_to_tables = {
    "executive_kpis.csv": "executive_kpis",
    "monthly_revenue.csv": "monthly_revenue",
    "top_products.csv": "top_products",
    "country_revenue.csv": "country_revenue",
    "customer_revenue.csv": "customer_revenue",
}

with engine.begin() as conn:
    conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME};"))

for file_name, table_name in files_to_tables.items():
    file_path = DASHBOARD_PATH / file_name

    print(f"Loading {file_name} into {SCHEMA_NAME}.{table_name}...")

    df = pd.read_csv(
        file_path,
        dtype={
            "customerid": "string",
            "stockcode": "string",
            "country": "string",
            "description": "string",
        }
    )

    df.to_sql(
        table_name,
        engine,
        schema=SCHEMA_NAME,
        if_exists="replace",
        index=False
    )

print("Dashboard summary tables loaded successfully.")
