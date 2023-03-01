from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'dataheroes',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='catchup_backfill',
    default_args=default_args,
    start_date=datetime(2022, 11, 1),
    schedule_interval='5 * * * *',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo bash command!'
    )