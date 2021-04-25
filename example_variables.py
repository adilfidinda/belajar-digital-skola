from airflow.utils.dates import days_ago
from airflow.models import DAG, Variable
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
import pandas as pd

args = {
    'owner': 'Airflow',
    'start_date': days_ago(0, hour=1, minute=0),
}

dag = DAG(
    dag_id='example_variables',
    default_args=args,
    schedule_interval="0 * * * *",
    tags=['example'],
    catchup=False
)

def print_variable():
    dfs = pd.read_html("https://id.wikipedia.org/wiki/Daftar_orang_terkaya_di_Indonesia", index_col = 0)
    dfs[7].to_csv('list_orang_terkaya_di_indonesia.csv')

cetak_variable = PythonOperator(
    task_id='cetak_variable',
    python_callable=print_variable,
    dag=dag,
)

send_email = EmailOperator(
        task_id='send_email',
        to='fia.digitalskola@gmail.com',
        subject='Dinda_DigitalSkola_Airflow',
        html_content=""" <h3>Dinda_DigitalSkola_Airflow</h3> """,
        files = ['orang_terkaya2020.csv'],
        dag=dag
)

cetak_variable >> send_email

