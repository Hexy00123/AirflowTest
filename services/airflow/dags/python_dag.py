from datetime import datetime, timedelta
import sys
import os

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from src.data import get_data



dafault_args = {
    'owner': 'hexy',
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}


def greet(name):
    print(f'Hello, {name}!')


def get_data_():
    print(os.getcwd())


with DAG(
    dag_id='TestPythonDAG',
    description='Just temporary python dag for testing',
    start_date=datetime(2024, 7, 9),
    schedule_interval=None,
    default_args=dafault_args
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={
            'name': 'Ruslan'
        }
    )

    task2 = PythonOperator(
        task_id='get_data',
        python_callable=get_data_,
    )

    task3 = BashOperator(
        task_id='ls',
        bash_command='ls -a',
    )

    task4 = BashOperator(
        task_id='pwd',
        bash_command='pwd',
    )

    task1 >> task2 >> task3 >> task4
