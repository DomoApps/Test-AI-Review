# Datasets API

The Domo Datasets API provides a set of endpoints for managing, creating, and updating datasets within Domo. The API allows developers to execute SQL queries on datasets, revoke access to datasets for specific users, retrieve dataset metadata, append rows to datasets, share datasets with access permissions, etc. With these endpoints, developers can build integrations that interact with Domo datasets, enabling data-driven decision-making and automation of business processes.

## Query with SQL

**Method**: `POST`  
**Endpoint**: `/api/query/v1/execute/:datasetId`

This endpoint executes an SQL query on the specified DataSet and returns the result in the form of a list of objects.

### Parameters:

| Property Name | Type   | Required | Description                                             |
| ------------- | ------ | -------- | ------------------------------------------------------- |
| datasetId     | String | Yes      | The ID of the DataSet to query.                         |
| sql           | String | Yes      | The SQL statement to execute.                           |

### Example:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/query/v1/execute/{datasetId}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "sql": "SELECT * FROM your_table WHERE column = 'value'"
  }
}
```

### Response:

```json
[
  {
    "column1": "value 1",
    "column2": "value 2",
    "column3": "value 3"
  },
  {
    "column1": "value 1",
    "column2": "value 2",
    "column3": "value 3"
  }
]
```

## Revoke Dataset Access

**Method**: `DELETE`  
**Endpoint**: `/api/data/v3/datasources/:datasetId/permissions/USER/:userId`

This endpoint revokes access to a specified DataSet for a given user.

### Parameters:

| Property Name | Type   | Required | Description                                              |
| ------------- | ------ | -------- | -------------------------------------------------------- |
| datasetId     | String | Yes      | The ID of the DataSet to revoke access from.             |
| userId      | String | Yes      | The ID of the user to revoke access for.               |

### Example:

```json
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/data/v3/datasources/{datasetId}/permissions/USER/{userId}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
}
```

### Response:

```json
{
  "HTTP/1.1": "200 OK",
  "body": {}
}
```

## Get Metadata

**Method**: `GET`  
**Endpoint**: `/api/data/v3/datasources/:datasetId`

This endpoint retrieves metadata for a specified DataSet, including the dataset's properties and optionally requested parts of the metadata.

### Parameters:

| Property Name | Type   | Required | Description                                           |
| ------------- | ------ | -------- | ----------------------------------------------------- |
| datasetId     | String | Yes      | The ID of the DataSet to retrieve metadata for.      |
| requestedParts| String | No       | A comma-separated list of metadata parts to include. |

### Example:

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/data/v3/datasources/{datasetId}?part=core,permission",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
}
```

### Response:

```json
{
    "id": "dataset id",
    "displayType": "webform",
    "dataProviderType": "webform",
    "type": "webform",
    "name": "dataset name",
    "owner": {
        "id": "User id",
        "name": "User name",
        "type": "USER",
        "group": false
    },
    "status": "SUCCESS",
    "created": 1231234124,
    "lastTouched": 1231421312,
    "lastUpdated": 12341234412,
    "rowCount": 2,
    "columnCount": 3,
    "cardInfo": {
        "cardCount": 3,
        "cardViewCount": 0
    },
    "properties": {
        "formulas": {
            "formulas": {}
        }
    },
    "state": "SUCCESS",
    "validConfiguration": true,
    "validAccount": true,
    "streamId": 25222,
    "transportType": "WEBFORM",
    "adc": true,
    "adcExternal": false,
    "adcSource": "DIRECT",
    "masked": false,
    "currentUserFullAccess": true,
    "cloudId": "domo",
    "cloudName": "Domo",
    "permissions": "READ_WRITE_DELETE_SHARE_ADMIN",
    "hidden": false,
    "scheduleActive": true,
    "cardCount": 3,
    "cloudEngine": "domo"
}
```

## Append row to Dataset

**Method**: `POST`  
**Endpoint**: `/api/data/v3/datasources/:datasetId/uploads`

### Description:
This endpoint appends a row of values to a specified dataset.

### Parameters:

| Property Name | Type   | Required | Description                                                             |
| ------------- | ------ | -------- | ----------------------------------------------------------------------- |
| datasetId     | String | Yes      | The ID of the dataset to which values will be appended.                  |
| values        | String | Yes      | A comma-delimited text string of values to append to the dataset.       |
| delimiter     | String | No       | The delimiter used to split the values (default is comma).               |

### Example Request:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/data/v3/datasources/{datasetId}/uploads",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "action": "APPEND",
    "message": "Uploading",
    "appendId": "latest"
  }
}
```

### Response:

```json
{
  "HTTP/1.1": "200 OK",
  "body": {}
}
```

## Execute Dataset Stream

**Method**: `POST`  
**Endpoint**: `/api/data/v1/streams/:streamId/executions`

### Description:
This endpoint queries a dataset's stream ID and executes the dataset stream.

### Parameters:

| Property Name | Type   | Required | Description                                                             |
| ------------- | ------ | -------- | ----------------------------------------------------------------------- |
| streamId      | String | Yes      | The ID of the dataset stream to execute.                                |
| action        | String | Yes      | The action to execute on the. "Manual", for example dataset stream.                            |

### Example Request:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/data/v1/streams/{streamId}/executions",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "action": "MANUAL"
  }
}
```

### Response:

```json
{
  "HTTP/1.1": "200 OK",
  "body": {}
}
```

## createDatasetTag

**Method**: `POST`  
**Endpoint**: `/api/data/ui/v3/datasources/:datasetId/tags`

### Description:
This endpoint creates a tag for the specified dataset.

### Parameters:

| Property Name | Type   | Required | Description                                                             |
| ------------- | ------ | -------- | ----------------------------------------------------------------------- |
| datasetId     | String | Yes      | The ID of the dataset to tag.                                           |
| tag           | String | Yes      | The tag to assign to the dataset.                                       |

### Example Request:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/data/ui/v3/datasources/:datasetId/tags",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": ["tag1", "tag2"]
}
```

### Response:

```json
{
  "HTTP/1.1": "200 OK",
  "body": {}
}
```

## Share Dataset with Access permissions

**Method**: `POST`  
**Endpoint**: `/api/data/v3/datasources/:datasetId/share`

### Description:
This endpoint shares a dataset and grants access permissions to specified users.

### Parameters:
| Property Name  | Type   | Required | Description                                                                         |
| --------------- | ------ | -------- | ----------------------------------------------------------------------------------- |
| datasetId       | String | Yes      | The ID of the dataset to share.                                                     |
| permissions     | Array  | Yes      | A list of owners to add to the dataset. Each owner is an object with id, type, and accessLevel. |
| sendEmail       | Boolean| Yes      | A flag indicating whether to send an email.                                         |

### Example Request:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/data/v3/datasources/:datasetId/share",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "permissions": [
      {
        "id": "ownerId1",
        "type": "USER",
        "accessLevel": "CO_OWNER"
      }
    ],
    "sendEmail": true
  }
}
```

### Response:

```json
{
  "HTTP/1.1": "200 OK",
  "Content-Type": "application/json",
  "body": {}
}
```

## Remove user from dataset

**Method**: `DELETE`  
**Endpoint**: `/api/data/v3/datasources/:datasetId/USERS/:userId`

### Description:
This endpoint removes a user from a dataset's permissions.

### Parameters:

| Property Name | Type   | Required | Description                                                             |
| ------------- | ------ | -------- | ----------------------------------------------------------------------- |
| datasetId     | String | Yes      | The ID of the dataset from which the user will be removed.            |
| userId      | String | Yes      | The ID of the user to remove from the dataset's permissions.          |

### Example Request:

```json
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/data/v3/datasources/:datasetId/USERS/:userId",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
}
```

### Response:

```json
{
  "HTTP/1.1": "200 OK",
  "body": {}
}
```

## Remove multiple users from dataset

**Method**: `DELETE`  
**Endpoint**: `/api/data/v3/datasources/:datasetId/users`

### Description:
This endpoint removes multiple people from a dataset's permissions.

### Parameters:

| Property Name | Type   | Required | Description                                                             |
| ------------- | ------ | -------- | ----------------------------------------------------------------------- |
| datasetId     | String | Yes      | The ID of the dataset from which the people will be removed.            |
| body        | Array  | Yes      | An array of user objects, each containing `id` and `type` properties. |

### Example Request:

```json
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/data/v3/datasources/:datasetId/users",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": 
    [
      {"id": "userId1", "type": "USER"},
      {"id": "userId2", "type": "USER"}
    ]
}
```

### Response:

```json
{
  "HTTP/1.1": "200 OK",
  "body": {}
}
```