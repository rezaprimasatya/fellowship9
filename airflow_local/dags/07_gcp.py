from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook
from datetime import datetime

def upload_file_to_gcs():
    # Define the GCS bucket and filename
    bucket_name = "fellowship9"
    file_name = f"example_file_{datetime.utcnow().isoformat()}.txt"
    
    # Create a hook to connect to GCS
    hook = GoogleCloudStorageHook(google_cloud_storage_conn_id = "fellowship_gcp")
    
    # Upload the file to GCS
    hook.upload(bucket_name, file_name, "./dags/rezaprimasatya.txt")
    print(f"File uploaded to GCS bucket {bucket_name} with filename {file_name}")

dag = DAG(
    'upload_to_gcs',
    description='Upload file to GCS',
    schedule_interval=None,
    start_date=datetime(2023, 3, 1),
)

upload_task = PythonOperator(
    task_id='upload_file',
    python_callable=upload_file_to_gcs,
    dag=dag,
)