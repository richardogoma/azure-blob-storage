import os
import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    print("Azure Blob Storage Python quickstart sample")
        
    # Create the BlobServiceClient object
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # Create a unique name for the container
    container_name = str(uuid.uuid4())

    # Create the container
    container_client = blob_service_client.create_container(container_name)

    local_file_folder = './files'
    for local_file_name in os.listdir(local_file_folder):
        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

        # Upload blobs to the container
        upload_file_path = os.path.join(local_file_folder, local_file_name)
        with open(file=upload_file_path, mode="rb") as data:
            blob_client.upload_blob(data)

    print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)

    # Clean up
    print("\nPress the Enter key to begin clean up")
    input()

    print("Deleting blob container...")
    container_client.delete_container()
    
    print("Done")

except Exception as ex:
    print('Exception:')
    print(ex)
    