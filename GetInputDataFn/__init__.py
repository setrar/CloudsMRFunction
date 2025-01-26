
from azure.storage.blob import BlobServiceClient

def main(connection_string: str):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client("input-container")

    input_data = []
    for blob in container_client.list_blobs():
        blob_client = container_client.get_blob_client(blob.name)
        content = blob_client.download_blob().content_as_text()
        lines = content.splitlines()
        input_data.extend([(i, line) for i, line in enumerate(lines)])

    return input_data
