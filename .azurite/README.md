# Azurite

The Azure Functions runtime cannot connect to the Azure Blob Storage emulator (127.0.0.1:10000). This typically occurs when:
1.	Azurite (Blob Storage Emulator) is not running.
2.	The AzureWebJobsStorage connection string in `local.settings.json` is invalid or missing.

Steps to Fix

1. Start Azurite (Azure Blob Storage Emulator)

If you’re running the function locally, you need to ensure that Azurite (the local Azure Blob Storage emulator) is running:

	1.	Install Azurite:

If you don’t have Azurite installed, install it using npm:

```
npm install -g azurite
```

2.	Start Azurite:

```
azurite
```

or 

```
azurite --blobHost 127.0.0.1
```


3.	Verify Azurite is Running:

By default, Azurite runs on:
-	Blob service: http://127.0.0.1:10000
-	Queue service: http://127.0.0.1:10001

Check if these ports are active:

```
lsof -i :10000
lsof -i :10001
```

If Azurite is running, you should see an active process.

2. Update `local.settings.json`

The AzureWebJobsStorage setting must point to Azurite when running locally. Update your local.settings.json file to:

```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "UseDevelopmentStorage=true"
  }
}
```

3. Retry the Function

Restart the Azure Functions runtime after making the changes:

```
func start --verbose
```

Test the StartMapReduce function again:

```
curl -X POST http://localhost:7071/api/StartMapReduce
```

4. Additional Debugging

If the issue persists, ensure the following:

a. Azurite Logs

Check the Azurite logs to confirm it is running and accessible. If Azurite fails to start, try:

```
azurite --debug
```

b. Clear Azurite Data

If Azurite is running but data is corrupted, clear its storage:

```
rm -rf __azurite_db_blob__ __azurite_db_queue__
```

5. For Production Deployment

In production, replace the local storage emulator with a real Azure Storage account. Update the AzureWebJobsStorage key in local.settings.json with the connection string of your Azure Storage account.

Retrieve the connection string:

```
az storage account show-connection-string \
    --name <storage-account-name> \
    --resource-group <resource-group-name>
```

Replace `UseDevelopmentStorage=true` with the retrieved connection string.

