import datetime

from airflow import DAG
# from airflow.contrib.operators.kubernetes_pod_operator import \
# KubernetesPodOperator
from airflow.operators import BaseOperator

default_args = dict(
    owner="capitancambio",
    email=["capitan.cambio@gmail.com"],
    email_on_failure=False,
    email_on_retry=False,
    start_date=datetime.datetime(2019, 10, 20),
    depends_on_past=False,
    retries=1,
    retry_delay=datetime.timedelta(minutes=15),
)

dag = DAG("example", schedule_interval=None, catchup=False, default_args=default_args)
task = BashOperator(task_id="my_task", bash_command="echo 'hi, this is python in london'", dag=dag)


# task = KubernetesPodOperator(
# task_id="my_task",
# name="my-task",
# namespace="kubernetes-talk",
# image="scripts:latest",
# cmds=[
# "scripts",
# "transform",
# "--input-url",
# "sftp://octopus:tentacle@sftp.kubernetes-talk.svc/upload/input.csv",
# "--output-url",
# "sftp://octopus:tentacle@sftp.kubernetes-talk.svc/upload/output.csv",
# ],
# get_logs=True,
# in_cluster=True,
# image_pull_policy="Never",
# dag=dag,
# )
