from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Paramètres par défaut du DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Définition du DAG
dag = DAG(
    'ecommerce_etl_pipeline',
    default_args=default_args,
    description='Pipeline ETL e-commerce avec Spark + Delta Lake',
    schedule_interval='@daily',  # peut être aussi @once pour test
    catchup=False,
)

# Tâche 1 : Extraction & Transformation
extract_transform = BashOperator(
    task_id='extract_transform',
    bash_command='/opt/bitnami/spark/bin/spark-submit /opt/spark/jobs/extract_transform.py',
    dag=dag,
)

# Tâche 2 : Chargement dans Delta Lake
load_to_delta = BashOperator(
    task_id='load_to_delta',
    bash_command='/opt/bitnami/spark/bin/spark-submit /opt/spark/jobs/load_to_delta.py',
    dag=dag,
)

# Orchestration : extract_transform → load_to_delta
extract_transform >> load_to_delta
