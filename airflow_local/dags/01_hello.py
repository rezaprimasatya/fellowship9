from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'dataheroes',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='first_dag',
    default_args=default_args,
    description='Hello Data Heroes',
    schedule_interval="1 * * * *", 
    catchup=False,
    start_date=datetime(2022, 7, 29, 2)
) as dag:
    task1 = BashOperator(
        task_id='task_1',
        bash_command="Hello Task 1"
    )

    task2 = BashOperator(
        task_id='task_2',
        bash_command="Hello Task 2"
    )

    task3 = BashOperator(
        task_id='task_3',
        bash_command="Hello Task 3"
    )

    task1

    # Task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task dependency method 2
    # task1 >> task2
    # task1 >> task3

    # Task dependency method 3
    # task1 >> [task2, task3]