FROM apache/airflow:2.3.0

# Install any necessary dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

