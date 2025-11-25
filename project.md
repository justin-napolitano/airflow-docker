---
slug: github-airflow-docker
id: github-airflow-docker
title: Dockerized Apache Airflow Setup for Local Development
repo: justin-napolitano/airflow-docker
githubUrl: https://github.com/justin-napolitano/airflow-docker
generatedAt: '2025-11-24T21:33:53.953Z'
source: github-auto
summary: >-
  A guide to setting up a Dockerized Apache Airflow environment with PostgreSQL
  and Redis for workflow orchestration.
tags:
  - apache airflow
  - docker
  - docker-compose
  - postgresql
  - redis
  - python
  - neo4j
  - workflow orchestration
  - docker compose
seoPrimaryKeyword: dockerized apache airflow setup
seoSecondaryKeywords:
  - airflow docker compose
  - postgresql integration
  - redis for airflow
  - local airflow setup
  - workflow management with airflow
seoOptimized: true
topicFamily: null
topicFamilyConfidence: null
kind: project
entryLayout: project
showInProjects: true
showInNotes: false
showInWriting: false
showInLogs: false
---

A Dockerized Apache Airflow setup designed for straightforward orchestration and management of workflows in a local development environment. This repository provides a Docker Compose configuration integrating Airflow with PostgreSQL and Redis, enabling rapid deployment and testing.

---

## Features

- Complete Docker Compose environment including Airflow components, PostgreSQL, and Redis
- Custom Dockerfile to build Airflow images tailored for this setup
- Sample DAGs demonstrating basic and advanced workflow orchestration
- Fernet key generation script to secure Airflow metadata
- Organized directories for DAGs, logs, plugins, and SQL scripts

## Tech Stack

- Apache Airflow 2.x
- Docker & Docker Compose
- PostgreSQL 13
- Redis 6.2
- Python (for DAG definitions and utility scripts)
- Neo4j (integrated in sample DAG for graph database operations)

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation & Running

1. Clone the repository:

```bash
git clone https://github.com/justin-napolitano/airflow-docker.git
cd airflow-docker
```

2. Generate a Fernet key (used by Airflow for encryption):

```bash
python3 fernet_key_generator.py
```

3. Export the Fernet key and set the SQL Alchemy connection string for PostgreSQL in your shell environment:

```bash
export AIRFLOW__CORE__FERNET_KEY="<your_generated_fernet_key>"
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN="postgresql+psycopg2://airflow:airflow@postgres/airflow"
```

4. Build and start the Docker containers:

```bash
docker-compose up --build
```

5. Access the Airflow webserver at [http://localhost:8089](http://localhost:8089).

6. Place your DAG files inside the `dags/` directory to have them automatically loaded.

## Project Structure

```
airflow-docker/
├── dags/                    # Airflow DAG definitions
│   ├── hello-world.py       # Example DAG printing "Hello, world!"
│   └── sup_court_graph_workflow.py  # DAG interacting with Neo4j graph database
├── logs/                   # Airflow logs
├── plugins/                # Custom Airflow plugins (empty by default)
├── sql/                    # Cypher and SQL scripts for workflows
├── Dockerfile              # Custom Dockerfile to build Airflow image
├── docker-compose.yml      # Docker Compose configuration
├── fernet_key_generator.py # Script to generate Fernet key
├── generate_fernet_key.sh  # Shell script alternative to generate Fernet key
├── README.md               # This file
├── requirements.txt        # Python dependencies
```

## Future Work / Roadmap

- Expand sample DAGs with more complex workflows and integrations
- Add automated tests for DAGs and environment setup
- Provide support for additional Airflow plugins and operators
- Enhance documentation with troubleshooting and advanced configuration guides
- Explore deployment options beyond local Docker, e.g., Kubernetes

