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
> Returns
```powershell
COMMAND   PID   USER   FD   TYPE DEVICE              SIZE/OFF NODE NAME
node    44029   me     16u  IPv4 0xafe13f2d29704696  0t0      TCP  localhost:ndmp (LISTEN)
COMMAND   PID   USER   FD   TYPE DEVICE              SIZE/OFF NODE NAME
node    44029   me     17u  IPv4 0x69b829b0e1cd50b   0t0      TCP  localhost:scp-config (LISTEN)
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

# References

```
npm info azurite
```
> Returns
```powershell

azurite@3.33.0 | MIT | deps: 22 | versions: 155
An open source Azure Storage API compatible server
https://github.com/azure/azurite#readme

keywords: Azurite, Azure, Storage, Blob, Queue, Emulator, Microsoft

bin: azurite, azurite-blob, azurite-queue, azurite-table

dist
.tarball: https://registry.npmjs.org/azurite/-/azurite-3.33.0.tgz
.shasum: 568f192b5d54cd71f53a8d21c7ace36945c9b63e
.integrity: sha512-GakEj0w7jjDVdQ8Nm3K+MooQxQpFBxCrWA470YFj0Na5/GKFvXtGZQ/3rj2f75jz0X8eJDDVPE1FhoSyfdWH9Q==
.unpackedSize: 4.1 MB

dependencies:
@azure/ms-rest-js: ^1.5.0  express: ^4.16.4           lokijs: ^1.5.6             rimraf: ^3.0.2             to-readable-stream: ^2.1.0 winston: ^3.1.0            
args: ^5.0.1               fs-extra: ^11.1.1          morgan: ^1.9.1             sequelize: ^6.31.0         tslib: ^2.3.0              xml2js: ^0.6.0             
axios: ^0.27.0             glob-to-regexp: ^0.4.1     multistream: ^2.1.1        stoppable: ^1.1.0          uri-templates: ^0.2.0      
etag: ^1.8.1               jsonwebtoken: ^9.0.0       mysql2: ^3.10.1            tedious: ^16.7.0           uuid: ^3.3.2               

maintainers:
- xiaonli <xiaoning.liu.leon@gmail.com>
- edwin-huber <edwin.huber@microsoft.com>
- vinjiang <VJ_MSFT@live.com>
- weiwei0430 <weiwei@microsoft.com>
- emmazhu <emmazhu@microsoft.com>

dist-tags:
alpha: 3.9.0-table-alpha.1  latest: 3.33.0              legacy: 2.7.1               

published 3 months ago by emmazhu <emmazhu@microsoft.com>
```
