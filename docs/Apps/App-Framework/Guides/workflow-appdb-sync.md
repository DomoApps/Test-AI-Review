
# Sync AppDB only once a day

This guide leverages workflows, please make sure you are familiar with Workflows and code engine first. 

<!-- theme: info -->
> #### Links to documentation
> - Workflow Documentation (https://domo-support.domo.com/s/article/000005108?language=en_US) 
> - Code Engine Documentation (https://domo-support.domo.com/s/article/000005173?language=en_US)


1. Create a workflow that runs at the time you want to sync the collection
2. Specify what collection you want to sync.
2. Create a code engine function that looks like this: 
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
4. call the new code engine function in the workflow
