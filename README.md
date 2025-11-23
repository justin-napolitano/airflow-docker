# airflow-docker

A Dockerized Apache Airflow setup for easy orchestration and management of workflows. This project provides a ready-to-use Docker Compose environment to run Airflow with PostgreSQL and Redis, simplifying local development and testing.

---

## Features

- Docker Compose setup including Airflow components, PostgreSQL, and Redis
- Custom Dockerfile to build Airflow images
- Sample DAGs demonstrating workflow orchestration
- Fernet key generation script for Airflow security
- Logs and SQL directories for extensibility

## Tech Stack

- Apache Airflow 2.x
- Docker & Docker Compose
- PostgreSQL 13
- Redis 6.2
- Python (for DAGs and utility scripts)
- Neo4j (used in sample DAG for graph database interactions)

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

2. Generate a Fernet key (used for Airflow encryption):

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

5. The Airflow webserver will be accessible at [http://localhost:8089](http://localhost:8089) (note the port mapping).

6. Place your DAG files inside the `dags/` directory to have them automatically loaded.

## Project Structure

```
airflow-docker/
├── dags/                    # Airflow DAG definitions
│   ├── hello-world.py       # Example DAG printing "Hello, world!"
│   └── sup_court_graph_workflow.py  # DAG interacting with Neo4j graph database
├── logs/                   # Airflow logs
├── plugins/                # Custom Airflow plugins (empty by default)
├── sql/                    # Cypher and SQL query files used by DAGs
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Dockerfile to build Airflow image
├── fernet_key_generator.py # Script to generate Fernet key
├── generate_fernet_key.sh  # Shell script alternative to generate Fernet key
├── readme.md               # This documentation
└── requirements.txt        # Python dependencies for Airflow environment
```

## Future Work / Roadmap

- Add more example DAGs showcasing different Airflow features and integrations
- Improve documentation with troubleshooting tips and advanced configuration
- Add support for Airflow plugins and custom operators
- Integrate CI/CD pipelines for automated testing and deployment
- Explore deployment options beyond Docker Compose, e.g., Kubernetes

---

*Note: This project is primarily designed for local development and testing. For production deployments, consider managed Airflow services or cloud-native solutions.*
