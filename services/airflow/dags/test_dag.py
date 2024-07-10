from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta


dafault_args={
    'owner': 'hexy', 
    'retries': 1, 
    'retry_delay': timedelta(seconds=10), 
}

with DAG(
    dag_id='TestingDag_v2',
    description='Just temporary dag for testing',
    start_date=datetime(2021, 7, 30, 2), 
    schedule_interval='@daily', 
    default_args=dafault_args
) as dag:
    task1 = BashOperator(
        task_id='first_task', 
        bash_command='echo hello world'
    )

    task2 = BashOperator(
        task_id='second_task', 
        bash_command='echo i am the second task'
    )

    task1.set_downstream(task2)
