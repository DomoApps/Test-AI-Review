---
stoplight-id:
---

# Files API

The Domo Data File Service is a centralized point in your Domo instance to manage, secure, share, and govern all of your files. This enables your applications the ability to upload documents, images, spreadsheets, and many other supported media types for re-use at a later time. The service also provides a version history chain that you can use to track your changes over time.

Domo supports nearly 100 different file types across over 300 file extensions. Please reach out to Domo Support if you have a question about supported file types, as the list changes often.

## Upload a file

Uploading a new file can be accomplished through the following request. You will pass in the file to upload, and Domo will store it and generate a unique identifier for the file, which is returned to you.

<!-- theme: info -->

> #### Default Permissions
>
> By default, the `public` param is set to `true`, granting all users in the Domo instance access to the file. Remember to set `public` to `false` if you want to restrict access to the user who originally uploaded the file. File permissions can be updated to give access to specific users and groups, if needed. You can find out how to do that by reviewing the [`Update file permissions`](#update-file-permissions) API.

#### Code Example

```js
function uploadFile(name, description = "", public = false, file) {
  const url = `/api/data/v1/data-files?name=${name}&description=${description}&public=${public}`;
  const response = await fetch(url, file);
  const { dataFileId } = await response.json();
}
```

#### Query Parameters

| Property Name | Type    | Required | Description                                           |
| ------------- | ------- | -------- | ----------------------------------------------------- |
| name          | String  | Required | The name to be given to the file in Domo              |
| description   | String  | Optional | A description of the file                             |
| public        | Boolean | Optional | Whether the permissions of the file are set to public |

#### HTTP Request

```text
POST /api/data/v1/data-files?name={name}&description={description}&public={public} HTTP/1.1
Accept: application/json
```

#### Request Body

The file to upload.

#### HTTP Response

Returns the id of the created file.

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "dataFileId": 401
}
```

## Upload a file revision

The Files API provides versioning support for files that have been uploaded. You may add another version of a file by sending a `PUT` request to the files endpoint referencing the `fileId` of the file you wish to revise.

#### Code Example

```js
function uploadRevision(dataFileId, file) {
  const url = `/api/data/v1/data-files/${dataFileId}`;
  const response = await fetch(url, file);
  const { revisionId } = await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                                                |
| ------------- | ------- | -------- | ---------------------------------------------------------- |
| dataFileId    | Integer | Required | The id of the file for which you wish to upload a revision |

#### HTTP Request

```text
PUT /api/data/v1/data-files/{dataFileId} HTTP/1.1
Accept: application/json
```

#### Request Body

The file to upload as a revision.

#### HTTP Response

Returns the current revision id of the file.

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "revisionId": 430
}
```

## Get all files metadata

Each file that you upload has corresponding metadata. This endpoint allows you to list all the metadata for each file you have access to. If you want to limit the files returned, you can include query parameters that filter the response.

#### Code Example

```js
function getFileDetailsList(
  userId = null,
  expand = null,
  dataFileIds = null
) {
  const params = new URLSearchParams();
  if (userId !== null) params.append("userId", userId);
  if (expand !== null) params.append("expand", expand);
  if (dataFileIds !== null) params.append("dataFileIds", dataFileIds);

  const queryString = params.toString();
  const url = `/api/data/v1/data-files/details${queryString !== '' ? `?${queryString}` : ''}`;
  const response = await fetch(url);
  const fileDetailsList = await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                                                                                                                    |
| ------------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| userId        | Integer | Optional | A Domo User Id if you want to limit the files returned by a specific owner                                                     |
| expand        | String  | Optional | An array of string properties specifying the additional details you want to retrieve (either `revisions`, `metadata`, or both) |
| dataFileIds   | String  | Optional | An array of File Ids that you wish to be returned if you only want a subset of files                                           |

#### HTTP Request

```text
GET /api/data/v1/data-files/details?userId={userId}&expand={expand}&dataFileIds={dataFileIds} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns an array of file objects.

```json
HTTP/1.1 200 OK
Content-Type: application/json

[
    {
        "dataFileId": 401,
        "name": "\"SampleFile\"",
        "responsibleUserId": 1089963280,
        "currentRevision": {
            "dataFileRevisionId": 430,
            "dataFileId": 401,
            "contentType": "application/pdf",
            "uploadUserId": 1089963280,
            "sizeBytes": 142783,
            "uploadTimeMillis": 199,
            "md5Hash": "B6C962A9288F132762051A6A33708B90",
            "datetimeUploaded": 1731613990000,
            "scanState": "SAFE",
            "sha256HashValue": "5E3EF0EF4CFAD65A1831D866DEEBD932C5A0AA3484A558FD0D1CA3EB852AE1BF"
        },
        "datetimeCreated": 1731611168000,
        "revisions": [],
        "existing": false
    }
]
```

## Get file metadata by ID

Given a known file ID, this endpoint allows you to list the metadata for that specific file.

#### Code Example

```js
function getFileDetails(dataFileId, expand = null) {
  let url = `/api/data/v1/data-files/${dataFileId}/details`;
  if (expand !== null) {
    url += `?expand=${expand.join()}`;
  }
  const response = await fetch(url);
  return await response.json();
}
```

#### Arguments

| Property Name | Type         | Required | Description                                                                                                                    |
| ------------- | ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| dataFileId    | Integer      | Required | The id of the file                                                                                                             |
| expand        | String Array | Optional | An array of string properties specifying the additional details you want to retrieve (either `revisions`, `metadata`, or both) |

#### HTTP Request

```text
GET /api/data/v1/data-files/{dataFileId}/details?expand={expand} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the file details object.

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "dataFileId": 90361,
    "name": "Sample",
    "responsibleUserId": 1249569521,
    "datetimeCreated": 1731613890000,
    "revisions": [],
    "existing": false
}
```

## Get revision metadata by ID

Given a known file revision ID, this endpoint allows you to list the metadata for that specific revision.

#### Code Example

```js
function getFileDetails(dataFileId, revisionId, expand = null) {
  let url = `/api/data/v1/data-files/${dataFileId}/revisions/${revisionId}/details`;
  if (expand !== null) {
    url += `?expand=${expand.join()}`;
  }
  const response = await fetch(url);
  return await response.json();
}
```

#### Arguments

| Property Name | Type         | Required | Description                                                                                                                    |
| ------------- | ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| dataFileId    | Integer      | Required | The id of the file                                                                                                             |
| revisionId    | Integer      | Required | The id of the file revision                                                                                                    |
| expand        | String Array | Optional | An array of string properties specifying the additional details you want to retrieve (either `revisions`, `metadata`, or both) |

#### HTTP Request

```text
GET /api/data/v1/data-files/{dataFileId}/revisions/{revisionId}/details?expand={expand} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the file revision details object.

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "dataFileRevisionId": 92251,
    "dataFileId": 90356,
    "contentType": "image/jpeg",
    "uploadUserId": 1249569521,
    "sizeBytes": 182457,
    "uploadTimeMillis": 216,
    "md5Hash": "CB3BEFA1DC2A5840E5DD61E81ACA1472",
    "datetimeUploaded": 1731620674000,
    "scanState": "SAFE",
    "sha256HashValue": "0E807933F5F0CD4F082784F243F78B1C56C16EF86C427796D52C64C2CFE4EDA9"
}
```

## Get all file revisions by ID

Given a known file ID, this endpoint fetches the revisions of the file.

#### Code Example

```js
function getFileRevisions(dataFileId, expand) {
  let url = `/api/data/v1/data-files/${dataFileId}/revisions/details`;
  if (expand !== null) {
    url += `?expand=${expand.join()}`;
  }
  const response = await fetch(url);
  return await response.json();
}
```

#### Arguments

| Property Name | Type         | Required | Description                                                                                                                    |
| ------------- | ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| dataFileId    | Integer      | Required | The id of the file                                                                                                             |
| expand        | String Array | Optional | An array of string properties specifying the additional details you want to retrieve (either `revisions`, `metadata`, or both) |

#### HTTP Request

```text
GET /api/data/v1/data-files/{dataFileId}/revisions/details?expand={expand} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns a list of all revisions of the file.

```json
HTTP/1.1 200 OK
Content-Type: application/json

[
    {
        "dataFileRevisionId": 92239,
        "dataFileId": 90356,
        "contentType": "image/jpeg",
        "uploadUserId": 1249569521,
        "sizeBytes": 182457,
        "uploadTimeMillis": 297,
        "md5Hash": "CB3BEFA1DC2A5840E5DD61E81ACA1472",
        "datetimeUploaded": 1731611168000,
        "scanState": "SAFE",
        "sha256HashValue": "0E807933F5F0CD4F082784F243F78B1C56C16EF86C427796D52C64C2CFE4EDA9"
    },
    ...
]
```

## Download a file

This endpoint fetches the file contents of a previously uploaded file, which can then be downloaded to the user's machine. You can optionally include a revisionId as a query parameter to fetch the contents of a specific revision.

#### Code Example

```js
function downloadFile(dataFileId, fileName = null) {
  const url = `/api/data/v1/data-files/${dataFileId}${fileName !== null ? `?fileName=${fileName}` : ''}`;
  const response = await fetch(url);
  const { revisionId } = await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                             |
| ------------- | ------- | -------- | --------------------------------------- |
| dataFileId    | Integer | Required | The id of the file you wish to download |
| fileName      | String  | Optional | The name you want to give the file      |

#### HTTP Request

To download the current file version:

```text
GET /api/data/v1/data-files/{fileId} HTTP/1.1
Accept: application/json
```

To download a previous version:

```text
GET /api/data/v1/data-files/{fileId}/revisions/{revisionId} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the File to be downloaded.

```text
HTTP/1.1 200 OK
Content-Type: {mime-type of the file}
```

### Copy/Move a file

This endpoint allows you to copy the current revision of a file to another target file. This essentially replaces the target file and leaves the source file intact.

#### Code Example

```js
function copyFile(sourceDataFileId, targetDataFileId) {
  const url = `/api/data/v1/data-files/copy/${sourceDataFileId}/revisions/current/${targetDataFileId}`;
  const response = await fetch(url);
  const { revisionId } = await response.json();
}
```

#### Query Parameters

| Property Name    | Type    | Required | Description                         |
| ---------------- | ------- | -------- | ----------------------------------- |
| sourceDataFileId | Integer | Required | The file id to move (source)        |
| targetDataFileId | Integer | Required | The file id to be replaced (target) |

#### HTTP Request

```text
POST /api/data/v1/data-files/copy/{sourceDataFileId}/revisions/current/{targetDataFileId} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the current revision id for the target file.

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "revisionId": 401
}
```

## Duplicate a file

This endpoint will create a new file object in Domo from an existing one.

#### Code Example

```js
function duplicateFile(dataFileId) {
  const url = `/api/data/v1/data-files/${dataFileId}/duplicate`;
  const response = await fetch(url);
  return await response.json();
}
```

#### Query Parameters

| Property Name | Type    | Required | Description              |
| ------------- | ------- | -------- | ------------------------ |
| dataFileId    | Integer | Required | The file id to duplicate |

#### HTTP Request

```text
POST /api/data/v1/data-files/{dataFileId}/duplicate HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the file metadata for the newly created duplicate.

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "dataFileId": 90370,
    "name": "Sample",
    "responsibleUserId": 1249569521,
    "currentRevision": {
        "dataFileRevisionId": 92257,
        "dataFileId": 90370,
        "contentType": "image/jpeg",
        "uploadUserId": 1249569521,
        "sizeBytes": 182457,
        "uploadTimeMillis": 290,
        "md5Hash": "CB3BEFA1DC2A5840E5DD61E81ACA1472",
        "datetimeUploaded": 1731622004000,
        "scanState": "SAFE",
        "sha256HashValue": "0E807933F5F0CD4F082784F243F78B1C56C16EF86C427796D52C64C2CFE4EDA9"
    },
    "datetimeCreated": 1731622002000,
    "revisions": [],
    "existing": false
}
```

## Delete a file

Permanently deletes a File from your instance.

#### Code Example

```js
function deleteFile(dataFileId) {
  const url = `/api/data/v1/data-files/${dataFileId}`;
  const response = await fetch(url);
  return await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                           |
| ------------- | ------- | -------- | ------------------------------------- |
| dataFileId    | Integer | Required | The id of the file you wish to delete |

#### HTTP Request

```text
DELETE /api/data/v1/data-files/{dataFileId} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the parameter of success or error based on the file Id being valid.

```text
HTTP/1.1 200 OK
```

## Delete a file revision

Deletes a specific revision of a file.

#### Code Example

```js
function deleteFileRevision(dataFileId, revisionId) {
  const url = `/api/data/v1/data-files/${dataFileId}/revisions/${revisionId}`;
  const response = await fetch(url);
  return await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                               |
| ------------- | ------- | -------- | ----------------------------------------- |
| dataFileId    | Integer | Required | The id of the file                        |
| revisionId    | Integer | Required | The id of the revision you wish to delete |

#### HTTP Request

```text
DELETE /api/data/v1/data-files/{dataFileId}/revisions/{revisionId} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the parameter of success or error based on the file Id being valid.

```text
HTTP/1.1 200 OK
```

## Get file permissions

#### Code Example

```js
function getFilePermissions(dataFileId) {
  const url = `/api/data/v1/data-files/${dataFileId}/permissions`;
  const response = await fetch(url);
  return await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                                               |
| ------------- | ------- | -------- | --------------------------------------------------------- |
| dataFileId    | Integer | Required | The id of the file you wish to get permission details for |

#### HTTP Request

```text
GET /domo/data-files/v1/{fileId}/permissions HTTP/1.1
Accept: application/json
```

#### HTTP Response

```json
HTTP/1.1 200 OK
Content-Type: application/json
{
    "publicAccess": false,
    "entries": [
        {
            "entityType": "USER",
            "entityId": "1089963280",
            "grant": "READ_WRITE_DELETE_SHARE_ADMIN",
            "pass": "NONE"
        }
    ]
}
```

## Update file permissions

#### Code Example

```js
function upadateFilePermissions(dataFileId, permissionData) {
  const url = `/api/data/v1/data-files/${dataFileId}/permissions`;
  const response = await fetch(url, permissionData);
  return await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                                                  |
| ------------- | ------- | -------- | ------------------------------------------------------------ |
| dataFileId    | Integer | Required | The id of the file you wish to update permission details for |

#### HTTP Request

```text
PUT /api/data/v1/data-files/{dataFileId}/permissions HTTP/1.1
Accept: application/json
```

#### Request Body

The request body accepts a permissions object.

```json
{
  "publicAccess": true,
  "entries": [
    {
      "entityType": "USER",
      "entityId": "1089963280",
      "grant": "READ_WRITE_DELETE_SHARE_ADMIN",
      "pass": "NONE"
    }
  ]
}
```

#### HTTP Response

Returns the parameter of success or error based on a valid permission object for the given file Id.

```text
HTTP/1.1 200 OK
```
