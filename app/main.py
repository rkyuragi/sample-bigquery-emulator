from google.cloud import bigquery
from google.auth.credentials import AnonymousCredentials


project_id = "test"
client = bigquery.Client(
    project=project_id,
    credentials=AnonymousCredentials(),
    client_options={
        "api_endpoint": "http://host.docker.internal:9050",
    }
)

table_name = f"{project_id}.dataset1.table_a"

query = f'''
SELECT id, name FROM `{table_name}`
'''
result = client.query(query)
for row in result:
    print(row)