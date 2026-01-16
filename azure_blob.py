from azure.storage.blob import BlobServiceClient
import uuid

CONNECTION_STRING = "Connection_string_goes_here"
CONTAINER_NAME = "Your_container_name"


def upload_to_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(
        CONNECTION_STRING
    )
    container_client = blob_service_client.get_container_client(
        CONTAINER_NAME
    )

    blob_name = f"{uuid.uuid4()}_{file.name}"
    blob_client = container_client.get_blob_client(blob_name)

    blob_client.upload_blob(file, overwrite=True)

    return blob_client.url
