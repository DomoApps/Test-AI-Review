---
stoplight-id: eeoadx67i6h46
---

# Files API

The Domo Data File Service is a centralized point in your Domo instance to manage, secure, share, and govern all of your files. This enables your applications the ability to upload documents, images, spreadsheets, and many other supported media types for re-use at a later time. The service also provides a version history chain that you can use to track your changes over time.

Domo supports nearly 100 different file types across over 300 file extensions. Please reach out to Domo Support if you have a question about supported file types, as the list changes often.

<!-- theme: info -->

> #### Domo Bricks
>
> Currently, Domo Bricks do not support the Files API.

### Upload a file

Uploading a new file can be accomplished through the following request. You will pass in the file to upload, and Domo will store it and generate a unique identifier for the file, which is returned to you.

<!-- theme: info -->

> #### Default Permissions
>
> The App Framework will automatically secure the file permissions so it can only be accessed by the same user who uploaded it, unless the `public` param is set to `true`. In that case, all users in the Domo instance will be able to access the file. File permissions can be updated to give access to specific users and groups, if needed. You can find out how to do that by reviewing the [`Update file permissions`](#update-file-permissions) API.

#### Code Example

```js
function uploadFile(name, description = "", public = false, file) {
  const formData = new FormData();
  formData.append("file", file);
  const url = `/domo/data-files/v1?name=${name}&description=${description}&public=${public}`;
  const options = { contentType: "multipart" };
  return domo.post(url, formData, options);
}
```

#### Query Parameters

| Property Name | Type    | Required | Description                                                                                           |
| ------------- | ------- | -------- | ----------------------------------------------------------------------------------------------------- |
| name          | String  | Required | The name to be given to the file in Domo                                                              |
| description   | String  | Optional | A description of the file                                                                             |
| public        | Boolean | Optional | Whether the permissions of the file are set to public - this is false by default in the App Framework |

#### HTTP Request

```text
POST /domo/data-files/v1?name={name}&description={description}&public={public} HTTP/1.1
Accept: application/json
```

#### Request Body

The request body is a javascript `FormData()` object which supports a multipart upload. The name given to the `File` that is to be appended to the `FormData` object is 'file'.

#### HTTP Response

Returns the id of the created file.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "dataFileId": 401
}
```

### Upload a file revision

The Files API provides versioning support for files that have been uploaded. You may add another version of a file by sending a `PUT` request to the files endpoint referencing the `dataFileId` of the file you wish to revise.

#### Code Example

```js
function uploadRevision(file, dataFileId) {
  const formData = new FormData();
  formData.append("file", file);
  const url = `/domo/data-files/v1/${dataFileId}`;
  const options = { contentType: "multipart" };
  return domo.put(url, formData, options);
}
```

#### Arguments

| Property Name | Type    | Required | Description                                               |
| ------------- | ------- | -------- | --------------------------------------------------------- |
| dataFileId    | Integer | Required | The id of the file of which you wish to upload a revision |

#### HTTP Request

```text
PUT /domo/data-files/v1/{dataFileId} HTTP/1.1
Accept: application/json
```

#### Request Body

The request body is a javascript `FormData()` object which supports a multipart upload. The name given to the `File` that is to be appended to the `FormData` object is 'file'.

#### HTTP Response

Returns the revision id of the uploaded revision file.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
    "revisionId": 430
}
```

### Get all files metadata

Each file that you upload has corresponding metadata. This endpoint allows you to list all the metadata for each file you have access to. If you want to limit the files to just those that you uploaded you can provide a `limitToOwned` boolean flag as a query parameter.

#### Code Example

```js
function getFileDetailsList(ids = null, expand = null, limitToOwned = false) {
  const params = new URLSearchParams();
  if (ids !== null) params.append("ids", ids);
  if (expand !== null) params.append("expand", expand);

  const queryString = params.toString();
  const url = `/domo/data-files/v1/details/?limitToOwned=${limitToOwned}${
    queryString !== "" ? `&${queryString}` : ""
  }`;
  return domo.get(url);
}
```

#### Arguments

| Property Name | Type          | Required | Description                                                                                                        |
| ------------- | ------------- | -------- | ------------------------------------------------------------------------------------------------------------------ |
| ids           | Integer Array | Optional | An array of File Ids that you wish to be returned if you only want a subset of files                               |
| expand        | String Array  | Optional | An array of string properties that you wish to see additional details of (either `revisions`, `metadata`, or both) |
| limitToOwned  | Boolean       | Optional | Whether or not to limit the result to only files that you uploaded                                                 |

#### HTTP Request

```text
GET /domo/data-files/v1/details?limitToOwned={limitToOwned}&ids={ids}&expand={expandList} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns an array of file objects.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
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
            "datetimeUploaded": 1731611168000,
            "scanState": "SAFE",
            "sha256HashValue": "5E3EF0EF4CFAD65A1831D866DEEBD932C5A0AA3484A558FD0D1CA3EB852AE1BF"
        },
        "datetimeCreated": 1731611168000,
        "revisions": [],
        "existing": false
    }
]
```

### Get file metadata by ID

Given a known file ID, this endpoint allows you to list the metadata for that specific file.

#### Code Example

```js
function getFileDetails(dataFileId, expandList = null) {
  let url = `/domo/data-files/v1/${dataFileId}/details`;
  if (expandList !== null) {
    url += `?expand=${expandList.join()}`;
  }

  return domo.get(url);
}
```

#### Arguments

| Property Name | Type   | Required | Description                                                                                                        |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ |
| expand        | String | Optional | An array of string properties that you wish to see additional details of (either `revisions`, `metadata`, or both) |

#### HTTP Request

```text
GET /domo/data-files/v1/{dataFileId}/details?expand={expandList} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the file details object.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
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
            "datetimeUploaded": "2019-03-06T00:26:37.000+0000",
            "scanState": "SAFE",
            "sha256HashValue": "5E3EF0EF4CFAD65A1831D866DEEBD932C5A0AA3484A558FD0D1CA3EB852AE1BF"
        },
        "datetimeCreated": "2019-03-04T21:41:01.000+0000",
        "revisions": [],
        "existing": false
    }
```

### Download a file

Below is the basic request for downloading a file. Depending on the type of file, this endpoint can be referenced inline in your application or called via an HTTP request. In this example, the `responseType` of the XHR request is being set to `blob` so that our code can reference it as a binary large object when passing the response to the Download method.

#### Code Example

```js
import Download from "downloadjs";
function downloadFile(dataFileId, filename, revisionId) {
  const options = { responseType: "blob" };
  const url = `/domo/data-files/v1/${dataFileId}${
    !!revisionId ? `/revisions/${revisionId}` : ""
  }`;
  return domo.get(url, options).then((data) => {
    Download(data, filename);
  });
}
```

#### Arguments

| Property Name | Type    | Required | Description                                      |
| ------------- | ------- | -------- | ------------------------------------------------ |
| dataFileId    | Integer | Required | The id of the file you wish to download          |
| revisionId    | Integer | Optional | The id of the file revision you wish to download |

#### HTTP Request

To download the current file version:

```text
GET /domo/data-files/v1/{dataFileId} HTTP/1.1
Accept: application/json
```

To download a previous version:

```text
GET /domo/data-files/v1/{dataFileId}/revisions/{revisionId} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the File to be downloaded.

```text
HTTP/1.1 200 OK
Content-Type: {mime-type of the file}
```

### Delete a file

Permanently deletes a File from your instance.

<!-- theme: danger -->

> #### Warning
>
> This is destructive and cannot be reversed. However, the delete does occur at the revision level, so if you unintentionally delete a file, the previous version will now be the current version of the file for a given file Id.

#### Code Example

```js
function deleteFile(dataFileId, revisionId) {
  const url = `/domo/data-files/v1/${dataFileId}/revisions/${revisionId}`;
  return domo.delete(url);
}
```

#### Arguments

| Property Name | Type    | Required | Description                                    |
| ------------- | ------- | -------- | ---------------------------------------------- |
| dataFileId    | Integer | Required | The id of the file you wish to delete          |
| revisionId    | Integer | Optional | The id of the revision file you wish to delete |

#### HTTP Request

```text
DELETE /domo/data-files/v1/{dataFileId}/revisions/{revisionId} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the parameter of success or error based on the file Id and the revisionId being valid.

```text
HTTP/1.1 200 OK
```

### Get file permissions

#### Code Example

```js
function getFilePermissions(dataFileId) {
  const url = `/domo/data-files/v1/${dataFileId}/permissions`;
  return domo.get(url);
}
```

#### Arguments

| Property Name | Type    | Required | Description                                               |
| ------------- | ------- | -------- | --------------------------------------------------------- |
| dataFileId    | Integer | Required | The id of the file you wish to get permission details for |

#### HTTP Request

```text
GET /domo/data-files/v1/{dataFileId}/permissions HTTP/1.1
Accept: application/json
```

#### HTTP Response

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
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

### Update file permissions

#### Code Example

```js
function upadateFilePermissions(dataFileId, data) {
  const url = `/domo/data-files/v1/${dataFileId}/permissions`;
  return domo.put(url, data);
}
```

#### Arguments

| Property Name | Type    | Required | Description                                                  |
| ------------- | ------- | -------- | ------------------------------------------------------------ |
| dataFileId    | Integer | Required | The id of the file you wish to update permission details for |

#### HTTP Request

```text
PUT /domo/data-files/v1/{dataFileId}/permissions HTTP/1.1
Accept: application/json
```

#### Request Body

```json
The request body accepts a permissions object.

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
