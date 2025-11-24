---
slug: github-airflow-docker-note-technical-overview
id: github-airflow-docker-note-technical-overview
title: airflow-docker
repo: justin-napolitano/airflow-docker
githubUrl: https://github.com/justin-napolitano/airflow-docker
generatedAt: '2025-11-24T18:30:20.847Z'
source: github-auto
summary: >-
  This repo is a Dockerized setup for Apache Airflow, aimed at workflow
  orchestration in a local dev environment. It includes a pre-configured Docker
  Compose setup with Airflow, PostgreSQL, and Redis for easy testing and
  deployment.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

This repo is a Dockerized setup for Apache Airflow, aimed at workflow orchestration in a local dev environment. It includes a pre-configured Docker Compose setup with Airflow, PostgreSQL, and Redis for easy testing and deployment.

## Key Features

- Complete Docker Compose environment
- Custom Dockerfile for tailored Airflow images
- Sample DAGs for workflow demonstration
- Fernet key generation for secure metadata
- Organized directory structure for DAGs, logs, plugins, and SQL scripts

## Quick Start

### Requirements

- Docker
- Docker Compose

### Run It

1. Clone the repo:

   ```bash
   git clone https://github.com/justin-napolitano/airflow-docker.git
   cd airflow-docker
   ```

2. Generate and export the Fernet key:

   ```bash
   python3 fernet_key_generator.py
   export AIRFLOW__CORE__FERNET_KEY="<your_generated_fernet_key>"
   export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN="postgresql+psycopg2://airflow:airflow@postgres/airflow"
   ```

3. Start up the environment:

   ```bash
   docker-compose up --build
   ```

Access the Airflow webserver at [http://localhost:8089](http://localhost:8089). Place DAGs in the `dags/` directory to load automatically.
