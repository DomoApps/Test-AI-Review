---
stoplight-id: 1l1fm2g0sfm69
---

# AppDB API

AppDB allows the storage of arbitrary JSON documents similar to a normal nosql database. This enables the ability to store state within your DomoApp. Optionally, you can also sync the data in AppDB back to a Domo dataset. This data storage is provided through 3 layers analogous to traditional storage mechanisms:

1. Datastores – Analogous to a database. A CustomApp has a single Datastore that is created automatically, named with the CustomApp’s ID and managed transparently to the CustomApp
2. Collections – Analogous to a collection in a nosql database or a table in a relational database. A Datastore can have multiple Collections defined
3. Documents – Analogous to documents in a nosql database or a table row in a relational database. A Collection can have multiple documents

### Defining Collections in the Manifest
---

Within the app manifest, you can define the collections that you want your app to be able to use by simply listing it in a collections property like so:

```json
{
  "name": "Example comments app",
  "version": "1.0",
  "size": {
    "width": 2,
    "height": 2
  },
  "mapping": [],
  "collections": [
    {
      "name": "CommentsTable",
      "schema": {
        "columns": [
          { "name": "user", "type": "STRING" },
          { "name": "comment", "type": "STRING" }
        ]
      },
      "syncEnabled": true
    },
    {
      "name": "Users"
    }
  ],
  "id": "760ae493-6c29-4e61-8fe3-9c887265ea86"
}
```

As you can see, if you do not need to sync it back to Domo the only property you need to define is the collection name. If you want it to sync back to Domo, you must also provide the schema you wish for the Domo dataset to have.

#### Schema Object

The schema object takes a list of columns. Each column has a name and a type. The following types are accepted.

- `STRING`
- `LONG`
- `DECIMAL`
- `DOUBLE`
- `DATE`
- `DATETIME`

<!-- theme: info -->

> #### Note
>
> Documents that contain DATE or DATETIME data must be formatted as YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ in order to be successfully synced to a Domo dataset.

<!-- theme: danger -->

> #### Warning
>
> If your app has not yet created a dataset and you provide the wrong data type in the schema section of your manifest, your collection will not be able to create a dataset to export to. If, after adding documents to your collection and waiting the 15-minute period for a normally scheduled export, you do not see your AppDB dataset in your data center, double check to ensure that your schema is set up correctly. Common mistakes are to include a data type like NUMBER or INTEGER.

<!-- theme: danger -->

> #### Warning
>
> It's also important to be aware that collections won't sync to Domo if the owner of the collection doesn't have the correct permissions on the dataset that it's syncing to.
>
> This is important to know in the case of someone who gets removed from their Domo instance. For example, if Bob owns a collection that is synced to dataset, but then is removed from the Domo instance, "deleted user" will remain as owner of the collection unless updated, but will have no permissions on the dataset, so it will stop syncing.
>
> The new owner of the collection not only has to be the owner, but has to be given admin permissions on the collection as well.

### Making API Calls to Your Collection

Examples of how to make calls to the collections defined in your manifest are below. For now, you will not be able to make these calls in local dev without including a proxy. Instead, you must publish your app and ensure that it is making calls in an installed app.

<!-- theme: info -->

> #### Note
>
> If you make any updates to the manifest and re-publish your app design, **you will need to edit the installed app and re-save it** for the manifest changes to take effect on the installed app (similar to what you would have to do if you made changes to the mapping section of your manifest).

### Create Document

Create a single document in a collection.

#### Code Example

The `documentContent` variable in this post request is equal to the sample request body.

```text
domo.post(`/domo/datastores/v1/collections/Users/documents/`, documentContent)
    .then(data => console.log(data));
```

#### Arguments

| Property Name  | Type   | Required | Description                                      |
| -------------- | ------ | -------- | ------------------------------------------------ |
| collectionName | String | Required | The name given to the collection in the manifest |

#### HTTP Request

```text
POST /domo/datastores/v1/collections/{collectionName}/documents/ HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### Request Body

The request body accepts a document object. All document content should be wrapped in the content object. The properties of the document within the content object should match the schema of the collection if the schema is provided.

```json
{
  "content": {
    "username": "Bill S. Preston, Esquire"
  }
}
```

#### HTTP Response

Returns the created document.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "id": "b3ea3d2d-86c5-44e6-a2f4-985136bbbce1",
    "customer": "excellent-adventure",
    "owner": 1089963280,
    "datastoreId": "d4a4b9c4-e123-41ce-8f93-dcafbeea4642",
    "collectionId": "02c3a404-e18c-4f15-ac7f-a96cdb59ad10",
    "createdOn": "2019-03-04T16:59:25.184+0000",
    "updatedOn": "2019-03-04T16:59:25.184+0000",
    "updatedBy": 1089963280,
    "content": {
        "username": "Bill S. Preston, Esquire"
    },
    "syncRequired": true
}
```

#### Code Example

```js
domo.post(`/domo/datastores/v1/collections/Users/documents`, {
  content: {
    username: "Bill S. Preston, Esquire",
  },
});
```

### List Documents
---

List all documents from a given collection.

#### Code Example

```js
domo
  .get(`/domo/datastores/v1/collections/Users/documents/`)
  .then((data) => console.log(data));
```

#### Arguments

| Property Name  | Type   | Required | Description                                      |
| -------------- | ------ | -------- | ------------------------------------------------ |
| collectionName | String | Required | The name given to the collection in the manifest |

#### HTTP Request

```text
GET /domo/datastores/v1/collections/{collectionName}/documents/ HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### HTTP Response

Returns an array of documents.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

[
    {
        "id": "b3ea3d2d-86c5-44e6-a2f4-985136bbbce1",
        "customer": "excellent-adventure",
        "owner": 1089963280,
        "datastoreId": "d4a4b9c4-e123-41ce-8f93-dcafbeea4642",
        "collectionId": "02c3a404-e18c-4f15-ac7f-a96cdb59ad10",
        "createdOn": "2019-03-04T16:59:25.184+0000",
        "updatedOn": "2019-03-04T16:59:25.184+0000",
        "updatedBy": 1089963280,
        "content": {
            "username": "Bill S. Preston, Esquire"
        },
        "syncRequired": true
    },
    {
        "id": "1e61d99d-9885-419a-a33e-3be3941ee720",
        "customer": "excellent-adventure",
        "owner": 1089963280,
        "datastoreId": "d4a4b9c4-e123-41ce-8f93-dcafbeea4642",
        "collectionId": "02c3a404-e18c-4f15-ac7f-a96cdb59ad10",
        "createdOn": "2019-03-03T17:49:25.72+0000",
        "updatedOn": "2019-03-03T17:49:25.72+0000",
        "updatedBy": 1089963280,
        "content": {
            "username": "Ted Theodore Logan"
        },
        "syncRequired": true
    },
]
```

### Get Document
---

Retrieve a single document from a collection given its document ID.

#### Code Example

```js
domo
  .get(`/domo/datastores/v1/collections/Users/documents/b3ea3d2d-86c5-44e6-a2f4-985136bbbce1`)
  .then((data) => console.log(data));
```

#### Arguments

| Property Name  | Type   | Required | Description                                         |
| -------------- | ------ | -------- | --------------------------------------------------- |
| collectionName | String | Required | The name given to the collection in the manifest    |
| documentId     | UUID   | Required | The id of the document returned when it was created |

#### HTTP Request

```text
GET /domo/datastores/v1/collections/{collectionName}/documents/{documentId} HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### HTTP Response

Returns the indicated document.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "id": "b3ea3d2d-86c5-44e6-a2f4-985136bbbce1",
    "customer": "excellent-adventure",
    "owner": 1089963280,
    "datastoreId": "d4a4b9c4-e123-41ce-8f93-dcafbeea4642",
    "collectionId": "02c3a404-e18c-4f15-ac7f-a96cdb59ad10",
    "createdOn": "2019-03-04T16:59:25.184+0000",
    "updatedOn": "2019-03-04T16:59:25.184+0000",
    "updatedBy": 1089963280,
    "content": {
        "username": "Bill S. Preston, Esquire"
    },
    "syncRequired": true
}
```

### Update Document
---

Update an existing document in a collection given its document ID.

#### Code Example

The `documentContent` variable in this put request is equal to the sample request body.

```text
domo.put(`/domo/datastores/v1/collections/Users/documents/b3ea3d2d-86c5-44e6-a2f4-985136bbbce1`, documentContent)
    .then(data => console.log(data));
```

#### Arguments

| Property Name  | Type   | Required | Description                                         |
| -------------- | ------ | -------- | --------------------------------------------------- |
| collectionName | String | Required | The name given to the collection in the manifest    |
| documentId     | UUID   | Required | The id of the document returned when it was created |

#### HTTP Request

```json
PUT /domo/datastores/v1/collections/{collectionName}/documents/{documentId} HTTP/1.1
Content-Type: application/json
Accept: application/json
Request Body
{
    "content": {
        "username": "Bill S. Preston, Esquire",
        "Band": "Wyld Stallyns"
    }
}
```

#### HTTP Response

Returns the modified document.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "id": "b3ea3d2d-86c5-44e6-a2f4-985136bbbce1",
    "customer": "excellent-adventure",
    "owner": 1089963280,
    "datastoreId": "d4a4b9c4-e123-41ce-8f93-dcafbeea4642",
    "collectionId": "02c3a404-e18c-4f15-ac7f-a96cdb59ad10",
    "createdOn": "2019-03-04T16:59:25.184+0000",
    "updatedOn": "2019-03-05T15:42:16.115+0000",
    "updatedBy": 1089963280,
    "content": {
        "username": "Bill S. Preston, Esquire",
        "Band": "Wyld Stallyns"
    },
    "syncRequired": true
}
```

#### Code Example

```js
domo
    .put(`/domo/datastores/v1/collections/Users/documents/b3ea3d2d-86c5-44e6-a2f4-985136bbbce1`)
    .then(console.log)
```

### Delete Document
---

Permanently deletes a document from your application's collection.

<!-- theme: danger -->

> #### Warning
>
> This is destructive and cannot be reversed. Note: Deleting documents in an AppDB collection may have performance implications with regard to syncing to its corresponding dataset in Domo if the `syncEnabled` property is set to `true` for the collection.
> Code Example
> domo.delete(`/domo/datastores/v1/collections/Users/documents/1e61d99d-9885-419a-a33e-3be3941ee720`);

#### Arguments

| Property Name  | Type   | Required | Description                                         |
| -------------- | ------ | -------- | --------------------------------------------------- |
| collectionName | String | Required | The name given to the collection in the manifest    |
| documentId     | UUID   | Required | The id of the document returned when it was created |

#### HTTP Request

```text
DELETE /domo/datastores/v1/collections/{collectionName}/documents/{documentId} HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### HTTP Response

Returns the parameter of success or error.

```text
HTTP/1.1 200 OK
```

### Query Documents
---

Any MongoDB query that can be used in a Mongo `find()` function can be used to query for documents in an AppDB Datastore. Official MongoDB query documentation is below:
https://docs.mongodb.com/manual/reference/operator/query/

Example of querying for a document that includes a comment that has the word 'happy' (via a regex operator) or does not include the username 'Eeyore' (via the not equals operator) can be found below. The return value of this call will be an array of documents that match the query.

#### HTTP Request

```text
POST /domo/datastores/v1/collections/{collectionName}/documents/query HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### Arguments

| Property Name  | Type   | Required | Description                                      |
| -------------- | ------ | -------- | ------------------------------------------------ |
| collectionName | String | Required | The name given to the collection in the manifest |

#### Request Body

```js
{ $or:
       [
           { content.comments: {$regex: 'happy'} },
           { content.username: {$ne: 'Eeyore' } }
       ]
}
```

#### HTTP Response

Returns an array of documents matching the query.

```json
HTTP/1.1 200 OK

[
    {
        "id": "b3ea3d2d-86c5-44e6-a2f4-985136bbbce1",
        "customer": "excellent-adventure",
        "owner": 1089963280,
        "datastoreId": "d4a4b9c4-e123-41ce-8f93-dcafbeea4642",
        "collectionId": "02c3a404-e18c-4f15-ac7f-a96cdb59ad10",
        "createdOn": "2019-03-04T16:59:25.184+0000",
        "updatedOn": "2019-03-05T15:42:16.115+0000",
        "updatedBy": 1089963280,
        "content": {
            "username": "Mickey Mouse",
            "comments": "Happy Birthday!"
        },
        "syncRequired": true
     },
     {
        "id": "b3ea3d2d-86c5-44e6-a2f4-985136bbbce1",
        "customer": "excellent-adventure",
        "owner": 1089963280,
        "datastoreId": "d4a4b9c4-e123-41ce-8f93-dcafbeea4642",
        "collectionId": "02c3a404-e18c-4f15-ac7f-a96cdb59ad10",
        "createdOn": "2019-03-04T16:59:25.184+0000",
        "updatedOn": "2019-03-05T15:42:16.115+0000",
        "updatedBy": 1089963280,
        "content": {
            "username": "Tigger",
            "comments": "Bouncing makes me so happy!"
        },
        "syncRequired": true
     },
]
```

#### Querying based on dates

Dates can be queried in AppDB using the [MongoDB Extended JSON v2](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/) spec shown below. This essentially casts the string that is being provided to the "less than or equal to" operator into a Date object. MongoDB documentation on the `$date` operator can be found [here](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/#bson.Date). The date string provided will need to be in the demonstrated ISO date format.

```js
{
    "createdOn" : {
        "$lte" : {
            "$date" : "2020-05-12T00:00:00.000Z"
        }
    }
}
```

### Query Documents with Aggregations
---

After the query limits the documents that will be returned by the api call, you can optionally add query string parameters to the url to aggregate the results of the query. Each parameter (excluding `groupby`) has the optional ability to take an alias. While it is not required to alias each property that is being aggregated, it is useful in the event that you need to pass the same property to different aggregations to avoid name collisions.

#### HTTP Request

```text
POST /domo/datastores/v1/collections/{collectionName}/documents/query?groupby={property1, property2}&count={alias}&{avg|max|min|sum}={property1 alias1, property2 alias2}&orderby={alias1 ascending|descending, alias2 ascending|descending} HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### Arguments

| Property Name  | Type    | Required | Description                                                                                                                                                        |
| -------------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| collectionName | String  | Required | The name given to the collection in the manifest                                                                                                                   |
| query          | Object  | Required | The JSON object that represents a Mongo query                                                                                                                      |
| groupby        | String  | Optional | The comma-separated list of properties you wish to group by                                                                                                        |
| count          | String  | Optional | The name you wish to alias a count aggregation property                                                                                                            |
| avg            | String  | Optional | The comma-separated list of properties in which you wish to perform an average aggregation followed by the name you wish to alias the result                       |
| min            | String  | Optional | The comma-separated list of properties in which you wish to perform a minimum aggregation followed by the name you wish to alias the result                        |
| max            | String  | Optional | The comma-separated list of properties in which you wish to perform a maximum aggregation followed by the name you wish to alias the result                        |
| sum            | String  | Optional | The comma-separated list of properties in which you wish to perform a sum aggregation followed by the name you wish to alias the result                            |
| unwind         | String  | Optional | The comma-separated list of properties that you wish to unwind (the unwind operator flattens nested arrays - see MongoDB documentation for additional information) |
| orderby        | String  | Optional | Alias of the aggregation you wish to order by (ascending or descending)                                                                                            |
| limit          | Integer | Optional | The number of documents in which to limit the number of return objects, default is 10,000                                                                          |
| offset         | Integer | Optional | The number of documents in which to skip before returning documents, default is 0                                                                                  |

#### Code Example

```js
const url = '/domo/datastores/v1/collections/campaigns/documents/query?groupby=content.campaignName, content.month&count=documentCount&avg=content.clicks avgClicks, content.impressions avgImps&sum=content.clicks sumClicks, content.impressions sumImps&max=content.clicks maxClicks, content.impressions maxImps&min=content.clicks minClicks, content.impressions minImps&orderby=sumClicks descending';

domo.post(url, {}).then(data => console.log(data));
```

#### Response

```json
[
  {
    "maxImps": 1250,
    "sumClicks": 210,
    "sumImps": 2260,
    "documentCount": 2,
    "minImps": 1010,
    "avgImps": 1130,
    "campaignName": "Red Campaign",
    "minClicks": 90,
    "avgClicks": 105,
    "maxClicks": 120,
    "month": "February"
  },
  {
    "maxImps": 1150,
    "sumClicks": 190,
    "sumImps": 2050,
    "documentCount": 2,
    "minImps": 900,
    "avgImps": 1025,
    "campaignName": "Red Campaign",
    "minClicks": 85,
    "avgClicks": 95,
    "maxClicks": 105,
    "month": "January"
  },
  {
    "maxImps": 1000,
    "sumClicks": 100,
    "sumImps": 1000,
    "documentCount": 1,
    "minImps": 1000,
    "avgImps": 1000,
    "campaignName": "Blue Campaign",
    "minClicks": 100,
    "avgClicks": 100,
    "maxClicks": 100,
    "month": "January"
  },
  {
    "maxImps": 500,
    "sumClicks": 50,
    "sumImps": 500,
    "documentCount": 1,
    "minImps": 500,
    "avgImps": 500,
    "campaignName": "Blue Campaign",
    "minClicks": 50,
    "avgClicks": 50,
    "maxClicks": 50,
    "month": "February"
  }
]
```

### Partially Update Documents Using Queries
---
Using standard mongo queries and update operations, you can do partial updates on your documents. The query must reference a document, or reference a property in a document.

Supported Operators:

- currentDate
- inc
- min
- max
- mul
- rename
- set
- unset
- addToSet
- pop
- pullAll

Supported Modifiers:

- each
- position
- slice
- sort

Please refer to the official [mongoDB documentation](https://www.mongodb.com/docs/manual/reference/operator/update/) on Update Operators in order to better understand these operators and how to create them. Note that since we require that the query references an existing document or property, the operator `$setOnInsert` is not supported.

#### Code Example

```text
domo.put(`/domo/datastores/v1/collections/Users/documents/update`, body)
    .then(data => console.log(data));
```

#### Arguments

| Property Name  | Type   | Required | Description                                      |
| -------------- | ------ | -------- | ------------------------------------------------ |
| collectionName | String | Required | The name given to the collection in the manifest |

#### HTTP Request

```text
  PUT /domo/datastores/v1/collections/{collectionName}/documents/update
  Content-Type: application/json
  Accept: application/json
```

#### Request Body

Specification

The request body is a single object that must be structured as follows.

```json
{
  "query": "{mongo query JSON}",
  "operation": "{mongo operation JSON}"
}
```

Example

```json
{
  "query": { "content.username": "Bill S. Preston, Esquire" },
  "operation": {
    "$set": {
      "content.comment": "Excellent!"
    }
  }
}
```

#### HTTP Response

Returns the number of updated objects or properties.

```text
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
1
```

### Bulk Operations

AppDB also allows for the creation, upsertion, and deletion of bulk lists of documents as shown in the examples below.

### Create Documents in Bulk

Create multiple documents in a given collection in a single HTTP request.

#### Code Example

The documents variable in this post request is equal to the sample request body.

```text
domo.post(`/domo/datastores/v1/collections/Users/documents/bulk`, documents)
    .then(data => console.log(data));
```

#### Arguments

| Property Name  | Type   | Required | Description                                      |
| -------------- | ------ | -------- | ------------------------------------------------ |
| collectionName | String | Required | The name given to the collection in the manifest |

#### HTTP Request

```text
POST /domo/datastores/v1/collections/{collectionName}/documents/bulk HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### Request Body

The request body accepts an array of document objects.

```json
[
  {
    "content": {
      "username": "Bill S. Preston, Esquire"
    }
  },
  {
    "content": {
      "username": "Ted Theodore Logan"
    }
  }
]
```

#### HTTP Response

Returns the number of documents created successfully.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
   "Created": 2
}
```

### Upsert Documents in Bulk

To upsert documents, you will need to provide the content object for each document and the id for existing objects that need to be updated. Objects that have an id will be updated. Those with no id or where the id is not found in the collection will be created.

#### Code Example

The documents variable in this post request is equal to the sample request body.

```text
domo.put(`/domo/datastores/v1/collections/Users/documents/bulk`, documents)
    .then(data => console.log(data));
```

#### Arguments

| Property Name  | Type   | Required | Description                                      |
| -------------- | ------ | -------- | ------------------------------------------------ |
| collectionName | String | Required | The name given to the collection in the manifest |

#### HTTP Request

```text
PUT /domo/datastores/v1/collections/{collectionName}/documents/bulk HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### Request Body

The request body accepts an array of document objects.

```json
[
  {
    "id": "b3ea3d2d-86c5-44e6-a2f4-985136bbbce1",
    "content": {
      "username": "Bill S. Preston, Esquire",
      "Band": "Wyld Stallyns"
    }
  },
  {
    "id": "1e61d99d-9885-419a-a33e-3be3941ee720",
    "content": {
      "username": "Ted Theodore Logan",
      "Band": "Wyld Stallyns"
    }
  },
  {
    "content": {
      "username": "Rufus"
    }
  }
]
```

#### HTTP Response

Returns the number of documents created and/or updated.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "Updated": 2,
    "Created": 1
}
```

### Delete Documents in Bulk

Provide a list of document Ids to be permanently deleted as a comma-separated query parameter.

<!-- theme: danger -->

> #### Warning
>
> This is destructive and cannot be reversed. Note: Deleting documents in an AppDB collection may have performance implications with regard to syncing to its corresponding dataset in Domo if the `syncEnabled` property is set to `true` for the collection.

```js
domo.delete(`/domo/datastores/v1/collections/Users/documents/bulk?ids=2bdd6370-85af-4e06-aadb-380839e4de8c,c78ba737-5f84-49c9-8ac9-58615a0f8aa8,1e61d99d-9885-419a-a33e-3be3941ee720`)
    .then(data => console.log(data));
```

#### Arguments

| Property Name  | Type   | Required | Description                                      |
| -------------- | ------ | -------- | ------------------------------------------------ |
| collectionName | String | Required | The name given to the collection in the manifest |
| idList         | Array  | Required | Comma-separated list of document Ids             |

#### HTTP Request

```json
DELETE /domo/datastores/v1/collections/{collectionName}/documents/bulk?ids={idList} HTTP/1.1
Content-Type: application/json
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "Deleted": 3
}
```

### Programmatic Operations for Collections

While most of the time you are going to want to define a collection in your manifest and have the platform automatically create the collection for you, there is also the option to programmatically manipulate collections from your app code.
Add

### Create Collection

To create a collection programmatically, send a post request to the below endpoint and provide the same JSON value that you would have provided in your manifest for a collection as the body of the request. Once created, the collection can be retrieved by the name you provided it as usual.

#### Code Example

The `collection` variable in this code sample is equal to the collection object in the sample request body.

```js
domo.post(`/domo/datastores/v1/collections`, collection)
    .then(data => console.log(data));
```

#### HTTP Request

```text
POST /domo/datastores/v1/collections HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### Request Body

```json
{
  "name": "Users",
  "schema": {
    "columns": [
      { "name": "username", "type": "STRING" },
      { "name": "band", "type": "STRING" }
    ]
  },
  "syncEnabled": true
}
```

#### HTTP Response

Returns the created collection.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "id": "6de8034e-0aa3-4fd9-ac1d-9a1ffeccb759",
    "customer": "excellent-adventure",
    "owner": 1089963280,
    "datastoreId": "d4a4b9c4-e123-41ce-8f93-dcafbeea4642",
    "name": "Users",
    "schemaJson": "{\"columns\":[{\"type\":\"STRING\",\"name\":\"username\",\"visible\":true},{\"type\":\"STRING\",\"name\":\"band\",\"visible\":true}]}",
    "syncRequired": true,
    "fullReplaceRequired": true,
    "lastSync": "1970-01-02T00:00:00.000+0000",
    "updatedBy": 1089963280,
    "schema": {
        "columns": [
            {
                "type": "STRING",
                "name": "username",
                "visible": true
            },
            {
                "type": "STRING",
                "name": "band",
                "visible": true
            }
        ]
    },
    "createdOn": "2019-03-04T18:47:12.327+0000",
    "updatedOn": "2019-03-04T18:47:12.327+0000",
    "exportable": true,
    "syncEnabled": true
}
```

### List Collections

Retrieve a list of the existing collections for your application.

#### Code Example

```js
domo.get(`/domo/datastores/v1/collections/`)
    .then(data => console.log(data));
```

#### HTTP Request

```text
GET /domo/datastores/v1/collections HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### HTTP Response

Returns an array of collection objects.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

[
  {
    "id": "6de8034e-0aa3-4fd9-ac1d-9a1ffeccb759",
    "customer": "excellent-adventure",
    "owner": 1089963280,
    "datastoreId": "d4a4b9c4-e123-41ce-8f93-dcafbeea4642",
    "name": "Users",
    "schemaJson": "{\"columns\":[{\"type\":\"STRING\",\"name\":\"username\",\"visible\":true},{\"type\":\"STRING\",\"name\":\"band\",\"visible\":true}]}",
    "syncRequired": true,
    "fullReplaceRequired": true,
    "lastSync": "1970-01-02T00:00:00.000+0000",
    "updatedBy": 1089963280,
    "schema": {
        "columns": [
            {
                "type": "STRING",
                "name": "username",
                "visible": true
            },
            {
                "type": "STRING",
                "name": "band",
                "visible": true
            }
        ]
    },
    "createdOn": "2019-03-04T18:47:12.327+0000",
    "updatedOn": "2019-03-04T18:47:12.327+0000",
    "exportable": true,
    "syncEnabled": true
  },
  {
        "id": "6b3b7ab7-9e72-483e-bc79-f05011cee5ef",
        "customer": "excellent-adventure",
        "owner": 1089963280,
        "datastoreId": "d4a4b9c4-e123-41ce-8f93-dcafbeea4642",
        "name": "Comments",
        "datasourceId": "62b4a99f-a98f-4f01-92f2-b02c35693c97",
        "schemaJson": "{\"columns\":[{\"type\":\"STRING\",\"name\":\"user\",\"visible\":true},{\"type\":\"STRING\",\"name\":\"comment\",\"visible\":true}]}",
        "syncRequired": false,
        "fullReplaceRequired": true,
        "lastSync": "2019-01-29T19:15:10.239+0000",
        "updatedBy": 1089963280,
        "schema": {
            "columns": [
                {
                    "type": "STRING",
                    "name": "user",
                    "visible": true
                },
                {
                    "type": "STRING",
                    "name": "comment",
                    "visible": true
                }
            ]
        },
        "createdOn": "2019-01-15T20:17:48.533+0000",
        "updatedOn": "2019-01-29T19:15:10.255+0000",
        "exportable": true,
        "syncEnabled": true
    }
]
```

### Update Collection

This PUT request allows you to modify any of your collections programmatically.

<!-- theme: danger -->

> #### Warning
>
> If you override the properties of a collection manually that exists in your manifest, any time the card of an app is saved it will revert back to the manifest definition of that collection. It is a best practice to only update collections that you have created manually. Otherwise, if you need to update a collection, simply update the manifest.

#### Code Example

```js
domo.put(`/domo/datastores/v1/collections/{collectionName}`, collection)
    .then(data => console.log(data));
```

#### Arguments

| Property Name  | Type   | Required | Description                                                         |
| -------------- | ------ | -------- | ------------------------------------------------------------------- |
| collectionName | String | Required | The name of the collection provided when the collection was created |

#### HTTP Request

```text
PUT /domo/datastores/v1/collections/{collectionName} HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### Request Body

```json
{
  "id": "6de8034e-0aa3-4fd9-ac1d-9a1ffeccb759",
  "schema": {
    "columns": [
      {
        "type": "STRING",
        "name": "username",
        "visible": true
      },
      {
        "type": "STRING",
        "name": "band",
        "visible": true
      },
      {
        "type": "STRING",
        "name": "favorite color",
        "visible": true
      }
    ]
  },
  "syncEnabled": true
}
```

#### HTTP Response

Returns the updated collection object.

```json
{
  "id": "6de8034e-0aa3-4fd9-ac1d-9a1ffeccb759",
  "customer": "excellent-adventure",
  "owner": 1089963280,
  "datastoreId": "d4a4b9c4-e123-41ce-8f93-dcafbeea4642",
  "name": "Users",
  "schemaJson": "{\"columns\":[{\"type\":\"STRING\",\"name\":\"username\",\"visible\":true},{\"type\":\"STRING\",\"name\":\"band\",\"visible\":true},{\"type\":\"STRING\",\"name\":\"favorite color\",\"visible\":true}]}",
  "syncRequired": true,
  "fullReplaceRequired": false,
  "lastSync": "1970-01-02T00:00:00.000+0000",
  "updatedBy": 1089963280,
  "schema": {
    "columns": [
      {
        "type": "STRING",
        "name": "username",
        "visible": true
      },
      {
        "type": "STRING",
        "name": "band",
        "visible": true
      },
      {
        "type": "STRING",
        "name": "favorite color",
        "visible": true
      }
    ]
  },
  "createdOn": "2019-03-04T18:47:12.332+0000",
  "updatedOn": "2019-03-04T18:59:06.168+0000",
  "exportable": true,
  "syncEnabled": true
}
```

### Delete Collection

Programmatically delete a collection.

<!-- theme: danger -->

> #### Warning
>
> This is destructive and cannot be reversed.

#### Code Example

```js
domo.delete(`/domo/datastores/v1/collections/{collectionName}`)
```

#### Arguments

| Property Name  | Type   | Required | Description                                                         |
| -------------- | ------ | -------- | ------------------------------------------------------------------- |
| collectionName | String | Required | The name of the collection provided when the collection was created |

#### HTTP Request

```text
DELETE /domo/datastores/v1/collections/{collectionName} HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### HTTP Response

Returns the parameter of success or error.

```text
HTTP/1.1 200 OK
```

### Manually Exporting Collections

Collections that are marked as `syncEnabled` will be exported to the Domo instance every 15 minutes. If for some reason, you need the collections for your app to be exported at a certain moment in time, you can manually call the export endpoint and it will kick off the export process. If there is already an export in progress, you will receive a `423 LOCKED` HTTP response. Otherwise, you will receive a `200 OK` HTTP response suggesting that the export request was successfully received.

The export endpoint is a POST request that takes no body.

#### Code Example

```js
domo.post(`/domo/datastores/v1/export`)
```

#### HTTP Request

```text
POST /domo/datastores/v1/export HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### HTTP Response

Returns the parameter of success or error.

```text
HTTP/1.1 200 OK
```

By default, hitting this endpoint will only export collections that were created by the app instance you are routing the request against. If you'd like to export all collections wired to the app instance regardless of which instance created them, you can set `includeRelatedCollections=true` in the query string.

```javascript
const exportCollection = async () => {
  const response = await fetch(
    "/domo/datastores/v1/export?includeRelatedCollections=true",
    {
      body: "{}",
      method: "POST",
    }
  );
  console.log(response);
  return response;
};
```

### Document Level Security Filtering

While developing your application, you might find yourself creating specific queries to limit users to see or use only certain data that is stored in your AppDB collections. These queries might be aimed at accomplishing some of the following use-case examples:

- A user should only see data that has been assigned to a certain region or team.
- A user should only be able to update AppDB documents that they themselves created.
- Only a manager who belongs to a certain Domo group can delete documents from your collection.

While your front-end application code can accomplish these examples in an attempt to secure your app, it is also possible for a user to bypass your client-side code and write their own code that interfaces with the AppDB endpoints directly. In order to secure your documents on the server side, document level filtering rules can be applied to the collection within the manifest of your application. An example of a collection with a document level filter applied is shown below.

```json
"collections": [
    {
      "name": "secureCollection",
      "filters": [
        {
          "name": "defaultFilter",
          "applyOn": [
            "READ",
            "UPDATE",
            "DELETE"
          ],
          "applyTo": [
            {
              "type": "GROUP_ID",
              "values": [
                12,
                15
              ]
            }
          ],
          "applyToAll": false,
          "limitToOwner": false,
          "query": {
            "content.region": "West"
          }
        }
      ]
    }
  ]
```

In this example, any user who belongs to the group with id `12` or `15` in Domo will only be able to see, modify, or delete documents that have the value of “West” in the document’s `content.region` property. As you can see, the `filters` property of this collection configuration object takes a list of filter rules. Adding multiple filter rules in the `filters` property will chain together the rules as an `OR` statement would in any standard data query language. There are several properties of a filter rule that are required to secure your documents. The following image groups them together by function.

![Filter Rule](https://web-assets.domo.com/miyagi/images/product/product-feature-dev-portal-appdbb-security-Filtering.png)

#### Filter Rule

- `name` – the name of the filter rule that you intend to create. This will be used mainly as a description of what you intend the rule to accomplish.

#### Who

- `applyTo` – the property that describes who to apply this filter rule to. This property takes a list of one or more condition objects.

  - condition– the condition that must be met in order for the filter rule to apply to the current user. The condition contains two properties.

    - type – the property that determines what kind of condition to compare against the current user:
      - `USER_ID`
      - `GROUP_ID`
    - `values` – a property that takes a list of possible values that the current user will be compared to. For example, if the `type` of the condition is `USER_ID` and the `values` list contains the current user’s ID, then the condition will evaluate to true and this filter rule will apply to the current user. If the list does not contain the user’s ID, the condition will evaluate to false and the filter rule will not apply and will be skipped.
      - **Wildcards**: In addition to listing static values, this field also supports two wildcards: `%userId%` and `%groupIds%`. An example of using one would be: `"query": {"content.user": "%userId%"}`, which will replace the `%userId%` with the id of the current user.

- `applyToAll` – a boolean value that overrides the applyTo property. If this property is set to true, then the current filter rule will apply to all users of the app.

#### What

- `query` – the AppDB query that should be combined with any query the user is trying to make to further filter down their request for documents. For example, let’s say the user belongs to the “West Sales” group, as defined in our example collection, and they wrote the following query to search for documents:

```json
{ "content.country": "US" }
```

In this case, because the user is part of a group defined in the `applyTo` section of the filter rule definition, the condition would be evaluated to true and our additional document-level security filter would be applied. The resulting query to AppDB on the server-side would be transformed to look like the following:

```json
{ "content.country": "US", "content.region": "West" }
```

So, although the user requested all documents from the “US” country, only those documents that are both in the “US” and the “West” region will be returned to the user.

- `limitToOwner` – this property takes a boolean that determines whether to add another query to any request that limits documents to only those created by the current user. So, if this flag were set to `true` then the resulting query on the backend would be transformed still further to add the user’s ID to the request. So, in the case of our previous example, even though the user requested documents from the “US”, they would actually be returned all documents from the “US” that are in the “West” region and created by the existing user.

```json
{ "content.country": "US", "content.region": "West", "owner": "123456" }
```

#### When

- `applyOn` – takes a list of http methods that the current filter rule should apply to. The enumerable list of methods is as follows:

  - `READ`
  - `UPDATE`
  - `DELETE`

Any AppDB endpoint that performs one of these operations will apply extra filtering prior to executing the request that the user-specified. From our previous example, if the user was given the document ID of a document that was not in the “West” region and the `DELETE` method existed in a filter rule that applied to them, if they attempted to call the delete endpoint and use that document ID, they would not be allowed to delete it. In this case, if they called the single document delete endpoint, it would return a 404 not found. If they called the bulk endpoint, it would return 0 documents deleted.

### Collection Level Security

Some applications might find it necessary to add security permissioning at the collection level. This could range from adding or removing the ability for a user to modify the definition of a programmatically created collection to removing the ability of any user of the app to delete any documents from the collection. By default, all users of the app that owns the collection have all permissions to the collection and its documents until the permissions are updated to be more specific.

#### Modify Permissions

Assuming you already have permission to modify the collection, you can change the permissions of a collection by hitting following endpoint:

#### Code Example

```js
domo.put("/domo/datastores/v1/collections/Users/permission/RYUU_APP/733ff55b-387c-472e-b3c7-9911c7057f5f?permissions=read,create_content,update_content,read_content");
```

#### HTTP Request

```text
PUT /domo/datastores/v1/collections/{collectionName}/permission/{entity}/{entityId}?permissions={permissionList} HTTP/1.1
Content-Type: application/json
```

#### Http Response

```text
HTTP/1.1 200 OK
```

#### Entity

The following are the possible entities that can be used in the `entity` path parameter in the above endpoint:

- `USER`
- `GROUP`
- `RYUU_APP`

The value you choose for the `entity` path parameter will determine which entity ID you will need to provide for the `entityId` path parameter. For users and groups, you will use either the user ID or the group ID. If you want to modify permissions for anyone who has access to the app as a whole, you can use the `RYUU_APP` path parameter and provide the app instance ID as the `entityId`. The app instance ID is the first UUID provided in the url of the iframe that houses the app. You should be able to pull down the url in your javascript using `window.location` and parse the first UUID programmatically.

#### Permission List

The following are the possible permissions that can be added using the `permissions` query parameter:

- `admin` - all permissions to the collection and its documents
- `write` - permission to update properties of the collection
- `read` - permission to read the properties of the collection
- `share` - permission to add or remove any permissions this entity already has
- `delete` - permission to delete the collection or its documents
- `create_content` - permission to create documents in the collection
- `update_content` - permission to update documents in the collection
- `read_content` - permission to read documents in the collection
- `delete_content` - permission to delete documents in the collection

#### Delete Permissions

You can remove all permissions for an entity using the following endpoint. If all entities’ permissions are removed then only users with the Manage AppDB grant will still have access.

#### Code Example

```js
domo.delete("/domo/datastores/v1/collections/Users/permission/RYUU_APP/733ff55b-387c-472e-b3c7-9911c7057f5f");
```

#### HTTP Request

```text
DELETE /domo/datastores/v1/collections/{collectionName}/permission/{entity}/{entityId} HTTP/1.1
Content-Type: application/json
```

#### Http Response

```text
HTTP/1.1 200 OK
```
