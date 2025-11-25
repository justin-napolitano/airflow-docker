---
slug: github-airflow-docker
title: Dockerized Apache Airflow Setup with PostgreSQL and Redis
repo: justin-napolitano/airflow-docker
githubUrl: https://github.com/justin-napolitano/airflow-docker
generatedAt: '2025-11-23T08:34:38.625053Z'
source: github-auto
summary: >-
  Explore a streamlined Docker setup for Apache Airflow, integrating PostgreSQL
  and Redis for efficient local workflow orchestration.
tags:
  - apache-airflow
  - docker
  - postgresql
  - redis
  - neo4j
  - workflow-orchestration
  - apache airflow
  - docker-compose
  - workflow orchestration
seoPrimaryKeyword: dockerized apache airflow setup
seoSecondaryKeywords:
  - airflow local development
  - postgresql integration
  - redis message broker
  - docker-compose configuration
  - workflow examples
  - environment variable management
seoOptimized: true
topicFamily: automation
topicFamilyConfidence: 0.95
topicFamilyNotes: >-
  The post focuses on automating the setup and orchestration of Airflow
  workflows using Docker Compose, involving configuration of supporting services
  like PostgreSQL, Redis, and Neo4j. The content aligns with automation of
  deployment and environment setup, matching the 'automation' family's
  description and example slugs that include docker and deployment workflows.
kind: project
id: github-airflow-docker
---

# airflow-docker: Technical Overview and Implementation Notes

## Motivation

Apache Airflow is widely adopted for orchestrating complex workflows, but setting it up with all dependencies can be cumbersome, especially for local development or testing. This project addresses that by providing a Dockerized Airflow environment integrated with PostgreSQL and Redis, enabling rapid deployment without manual dependency management.

## Problem Statement

Running Airflow typically requires configuring a metadata database, message broker, and the Airflow components themselves. Manual setup can lead to environment inconsistencies, version conflicts, and slow iteration cycles. This repository solves these problems by containerizing all necessary components and providing a unified Docker Compose configuration.

## Architecture and Components

- **PostgreSQL 13** serves as the Airflow metadata database, storing DAG states, task instances, and user data.
- **Redis 6.2** is used as the Celery broker to manage distributed task queues.
- **Airflow Components** include the webserver, scheduler, worker, and an initialization service to set up the database and default admin user.
- A **Custom Dockerfile** builds Airflow images tailored to this setup, ensuring compatibility and ease of extension.

The Docker Compose file orchestrates these services, mounts local directories for DAGs, logs, and plugins, and exposes ports for webserver access.

## Security

Airflow requires a Fernet key to encrypt sensitive data in its metadata database. The repository includes a Python script (`fernet_key_generator.py`) to generate this key, which must be exported as an environment variable before starting the services. This approach maintains separation of secrets from the codebase.

## Workflow Examples

Two sample DAGs illustrate usage:

- `hello-world.py`: A minimal DAG that prints "Hello, world!" daily, demonstrating basic Airflow task orchestration.
- `sup_court_graph_workflow.py`: A more complex DAG interacting with a Neo4j graph database. It loads Cypher queries from SQL files and executes them using the Neo4j Python driver, showcasing integration with external graph databases.

This DAG also uses environment variables loaded from a `.env` file inside the container, illustrating best practices for managing sensitive connection details.

## Implementation Details

- The `docker-compose.yml` defines services with environment variables for the Fernet key and SQL Alchemy connection string, which must be set externally.
- Volumes map local directories into containers to allow live editing of DAGs and access to logs.
- The `airflow-init` service runs database migrations and creates an admin user before other Airflow components start.
- The DAGs use the `PythonOperator` to execute Python callables, enabling flexible task definitions.

## Practical Considerations

- Port mapping exposes the Airflow webserver on port 8089 locally, avoiding conflicts with other services.
- The setup assumes the user will generate and manage the Fernet key and database connection string securely.
- Logs and SQL scripts are organized in dedicated directories for maintainability.
- The Neo4j integration requires a running Neo4j instance accessible from the Airflow containers and appropriate environment variables set.

## Limitations and Assumptions

- This setup is optimized for local development and testing, not production use.
- Secrets management is manual; users must handle environment variables securely.
- The Neo4j DAG is a sample and requires further development for production workflows.

## Summary

This project provides a practical, containerized Airflow environment that simplifies local orchestration development. It integrates key components, supports workflow examples including graph database interactions, and follows best practices for environment configuration and security. The modular structure and clear separation of concerns facilitate extension and adaptation to specific use cases.

