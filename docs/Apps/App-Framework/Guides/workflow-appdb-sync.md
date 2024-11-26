
# Sync AppDB Only Once a Day

Domo doesn't currently allow you to specify sync intervals. Either AppDB doesn't sync or it syncs every 15 minutes. In order to conserve credits on syncs you can create a Workflow to sync on your schedule instead.

This guide leverages Workflows, please make sure you are familiar with [Workflows](https://domo-support.domo.com/s/article/000005108?language=en_US) and [Code Engine](https://domo-support.domo.com/s/article/000005173?language=en_US) first. 

<!-- theme: info -->
> #### Links to documentation
> - Workflow Documentation (https://domo-support.domo.com/s/article/000005108?language=en_US) 
> - Code Engine Documentation (https://domo-support.domo.com/s/article/000005173?language=en_US)


1. Create a Workflow that runs at the time you want to sync the collection
2. Specify what collection you want to sync
3. Create a Code Engine function to do the sync: 
```js
const codeengine = require("codeengine");

async function syncCollection(collectionId) {
  const collection = await codeengine.sendRequest('get', `/api/datastores/v1/collections/${collectionId}`);
  const putBody = {id: collectionId, syncEnabled: true}
  // enables collection sync
  await codeengine.sendRequest(
    'put',
    `/api/datastores/v1/collections/${collectionId}`,
    JSON.stringify(putBody)
  );
  // forces collection sync
  await codeengine.sendRequest(
    'post',
    `/api/datastores/v1/export/${collection.datastoreId}`,
    ""
  );
  // turns off collection sync
  await codeengine.sendRequest(
    'put',
    `/api/datastores/v1/collections/${collectionId}`,
    JSON.stringify({...putBody, syncEnabled: false})
  );
}
```
4. call the new Code Engine function in the Workflow
