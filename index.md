---
slug: "github-airflow-docker"
title: "airflow-docker"
repo: "justin-napolitano/airflow-docker"
githubUrl: "https://github.com/justin-napolitano/airflow-docker"
generatedAt: "2025-11-23T08:11:25.534611Z"
source: "github-auto"
---


# Running Apache Airflow with Docker: My Journey and Insights

Hey folks! Today I want to share some thoughts and experiences around a project I put together called **airflow-docker**. It's a Dockerized setup for Apache Airflow that I built to simplify spinning up a local Airflow environment with PostgreSQL and Redis. If you've ever wrestled with Airflow's setup or wanted a quick way to test DAGs locally, this might resonate with you.

## Why I Built This

Apache Airflow is an amazing tool for orchestrating complex workflows, but its setup can sometimes be a bit daunting, especially when you want to get started quickly or test new DAGs. I wanted a reproducible, containerized environment where I could just `docker-compose up` and have everything running — the Airflow webserver, scheduler, workers, and the necessary backend services like PostgreSQL and Redis.

I also wanted to experiment with integrating Airflow with other data systems — for example, I have a DAG that interacts with a Neo4j graph database, running Cypher queries to build relationships. Having this all containerized means I can easily extend or modify the environment without polluting my local machine.

## How It's Built

The core of the project is a `docker-compose.yml` file that defines several services:

- **Postgres**: The metadata database for Airflow.
- **Redis**: Used as a broker for Celery executors.
- **Airflow-init**: A container that initializes the Airflow database and creates an admin user.
- **Airflow-webserver**: The UI for managing and monitoring DAGs.
- **Airflow-scheduler**: Responsible for scheduling DAG runs.
- **Airflow-worker**: Executes tasks using Celery.

I created a custom `Dockerfile` to build the Airflow image with any additional dependencies I might need. The DAGs, logs, and plugins directories are mounted as volumes so that changes are reflected immediately without rebuilding images.

Security-wise, Airflow requires a Fernet key for encrypting sensitive data. I included a simple Python script (`fernet_key_generator.py`) and a shell script to generate this key, which you then export as an environment variable before running the stack.

## Interesting Details

One of the DAGs I wrote (`sup_court_graph_workflow.py`) connects to a Neo4j graph database. It reads Cypher queries from `.cql` files in the `sql/` directory and executes them to create relationships between contributors and subjects. This is a neat example of how Airflow can orchestrate not just SQL workflows but also graph database operations.

I also included a super simple `hello-world.py` DAG that just prints "Hello, world!" to demonstrate the basic structure of a DAG and how tasks are defined.

The Docker Compose file uses environment variables for sensitive configuration like the Fernet key and database connection string, so you can keep secrets out of version control.

## Why this project matters for my career

Building this project sharpened my skills in containerization, orchestration, and workflow automation — all crucial areas in modern data engineering and DevOps roles. It also gave me hands-on experience integrating Airflow with different backend systems like PostgreSQL and Neo4j, which broadens my understanding of how to manage complex data pipelines.

Moreover, the project serves as a solid foundation I can extend for future data projects or use as a reference when setting up Airflow environments in professional settings. Having a reproducible, containerized Airflow stack is a big productivity booster and a great conversation starter in interviews or team discussions.

## Final Thoughts

While I personally lean towards using managed cloud services like GCP Cloud Run Jobs for many use cases, having this Dockerized Airflow environment is invaluable for experimentation, learning, and local development. If you're curious about Airflow or want a quick way to get started, give this project a try!

Happy orchestrating! 🚀