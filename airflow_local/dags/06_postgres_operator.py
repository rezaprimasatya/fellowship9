from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    'owner': 'dataheroes',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='postgres_operator',
    default_args=default_args,
    start_date=datetime(2021, 12, 19),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = PostgresOperator(
        task_id='create_postgres_table',
        postgres_conn_id='fellowship_postgres',
        sql="""
            create table if not exists fellowship_member (
                id serial,
                name text not null,
                age  int  not null,
                address char(50),
                primary key (id)
            )
        """
    )

    task2 = PostgresOperator(
        task_id='insert_into_table',
        postgres_conn_id='fellowship_postgres',
        sql="""
            insert into fellowship_member(name,age,address) values ( 'Reza', 17, 'DPS')
        """
    )

    task3 = PostgresOperator(
        task_id='delete_data_from_table',
        postgres_conn_id='fellowship_postgres',
        sql="""
            delete from fellowship_member where id = 5;
        """
    )
    task1 >> task3 >> task2