from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('/opt/airflow/.env')  # Path within the Docker container

# Define Neo4j connection details from environment variables
NEO4J_URL = os.getenv('NEO4J_URL')
NEO4J_USER = os.getenv('NEO4J_USER')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

def read_query_file(filepath):
    with open(filepath, 'r') as file:
        query = file.read()
    return query

# Function for creating relationships between contributors and subjects
def make_contributor_to_subject_relationships():
    driver = GraphDatabase.driver(NEO4J_URL, auth=(NEO4J_USER, NEO4J_PASSWORD))
    cypher_query = read_query_file('/opt/airflow/sql/ctrbr_to_sbjt.cql')  # Path within the Docker container

    def execute_query(tx):
        result = tx.run(cypher_query)
        for record in result:
            print(record)

    with driver.session() as session:
        session.write_transaction(execute_query)
    driver.close()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 9),
    'retries': 1,
}

dag = DAG('neo4j_workflow', default_args=default_args, schedule_interval='@daily')

# Placeholder functions for future use
# def ingest_data():
#     sql_query = read_query_file('/opt/airflow/sql/ingest_data.sql')  # Path within the Docker container
#     # Execute your SQL query here using your database connection
#     print(sql_query)  # Replace this with actual query execution logic

# def transform_data():
#     sql_query = read_query_file('/opt/airflow/sql/transform_data.sql')  # Path within the Docker container
#     # Execute your SQL query here using your database connection
#     print(sql_query)  # Replace this with actual query execution logic

# Define the task for making contributor-to-subject relationships
t3 = PythonOperator(
    task_id='make_contributor_to_subject_relationships',
    python_callable=make_contributor_to_subject_relationships,
    dag=dag
)

# Define the DAG structure
t3
