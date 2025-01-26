import azure.functions as func
from azure.storage.blob import BlobServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    connection_string = req.params.get("connection_string")
    if not connection_string:
        try:
            req_body = req.get_json()
        except ValueError:
            return func.HttpResponse("Invalid input", status_code=400)
        else:
            connection_string = req_body.get("connection_string")

    if not connection_string:
        return func.HttpResponse(
            "Please pass a valid connection_string in the query or request body",
            status_code=400,
        )

    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client("input-container")

        input_data = []
        for blob in container_client.list_blobs():
            blob_client = container_client.get_blob_client(blob.name)
            content = blob_client.download_blob().content_as_text()
            lines = content.splitlines()
            input_data.extend([(i, line) for i, line in enumerate(lines)])

        return func.HttpResponse(str(input_data), status_code=200)

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
