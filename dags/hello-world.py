from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, world!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG('hello_world_dag', default_args=default_args, schedule_interval='@daily')

t1 = PythonOperator(task_id='hello_world_task', python_callable=hello_world, dag=dag)

