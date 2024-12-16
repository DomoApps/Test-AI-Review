---
stoplight-id: eeoadx67i6h46
---

# Files API

Custom Apps provides a convenient access point to the Domo Data File Service, a centralized point in your Domo instance to manage, secure, share, and govern all of your files. This enables your applications the ability to upload documents, images, spreadsheets, and many other supported media types for re-use at a later time. The service also provides a version history chain that you can use to track your changes over time for use in collaborating with your peers.

<!-- theme: info -->

> #### Domo Bricks
>
> Currently, Domo Bricks do not support the Files API.


### Uploading a file
---
Uploading a file can be accomplished through the following POST request. The `file` is a multipart upload file that you can select from your computer and add to a `FormData` object. The `name` query parameter is mandatory. The `description` query parameter takes a text-based description and is optional and the `public` query parameter takes a Boolean value and is also optional.

#### Code Example
```js
function uploadFile(name, description="", isPublic=false, file){
  const formData  = new FormData();
  formData.append('file', file);
  const url = `/domo/data-files/v1?name=
             ${name}&description=${description}&public=${isPublic}`;
  const options = { contentType: 'multipart' };
  return domo.post(url, formData, options);
}
```

#### Arguments
| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
|name | String | Required | The name to be given to the file in Domo|
|description | String | Optional | A description of the file|
|isPublic | Boolean | Optional | Whether the permissions of the file are set to public - this is false by default in the App Framework|

#### HTTP Request
```text
POST /domo/data-files/v1?name={name}&description={description}&public={isPublic} HTTP/1.1
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

### Uploading a file revision
---
The Files API provides versioning support for files that have been uploaded. You may add another version of a file by sending a `PUT` request to the files endpoint referencing the `fileId` of the file in which you wish to add a revision.

#### Code Example
```js
function uploadRevision(file, fileId) {
        const formData  = new FormData();
        formData.append('file', file);
        const url = `/domo/data-files/v1/${fileId}`;
        const options = { contentType: 'multipart' };
        return domo.put(url, formData, options);
}
```

#### Arguments
| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
| fileId | Long | Required | The id of the file of which you wish to upload a revision|

#### HTTP Request
```text
PUT /domo/data-files/v1/{fileId} HTTP/1.1
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

### Get a list of files metadata
---
Each file that you upload has corresponding metadata. This endpoint allows you to list all the metadata for each file you have access to. If you want to limit the files to just those that you uploaded you can provide a limitToOwned boolean flag as a query parameter.

#### Code Example
```js
function getFileDetailsList(idList=null, expandList=null, limitToOwned=false){
        let url = "/domo/data-files/v1/details/?limitToOwned=${limitToOwned}";
        if(idList !== null){ url += `&ids=${idList.join()}`;}
        if(expandList !== null){ url += `&expand=${expandList.join()}`;}

        return domo.get(url);
    }
```

#### Arguments
| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
| ids	| Long	| Optional |	An array of File Ids that you wish to be returned if you only want a subset of files|
| expand | String	| Optional	| An array of string properties that you wish to see additional details of (either `revisions`, `metadata`, or both)|
|limitToOwned	| Boolean |	Optional	| Whether or not to limit the result to only files that you uploaded|

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
            "datetimeUploaded": "2019-03-06T00:26:37.000+0000",
            "scanState": "SAFE",
            "sha256HashValue": "5E3EF0EF4CFAD65A1831D866DEEBD932C5A0AA3484A558FD0D1CA3EB852AE1BF"
        },
        "datetimeCreated": "2019-03-04T21:41:01.000+0000",
        "revisions": [],
        "existing": false
    }
]
```

### Get an individual file's metadata
---
Given a known file ID, this endpoint allows you to list the metadata for that specific file.

#### Code Example

```js
function getFileDetails(fileId, expandList=null){
        let url = `/domo/data-files/v1/{fileId}/details`;
        if(expandList !== null){ url += `?expand=${expandList.join()}`;}

        return domo.get(url);
    }
```

#### Arguments

| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
|expand	| String |	Optional	|An array of string properties that you wish to see additional details of (either `revisions`, `metadata`, or both)|

#### HTTP Request

```text
GET /domo/data-files/v1/{fileId}/details?expand={expandList} HTTP/1.1
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
---
Below is the basic request for downloading a file. Depending on the type of file, this endpoint can be referenced inline in your application or called via an HTTP request. In this example, the `responseType` of the XHR request is being set to `blob` so that our code can reference it as a binary large object when passing the response to the Download method.

#### Code Example

```js
import Download from 'downloadjs';
function downloadFile(fileId, filename, revisionId){
  const options = { responseType: 'blob' };  
  const url = `/domo/data-files/v1/${fileId}${!!revisionId ? `/revisions/${revisionId}` : ''}`
  return domo.get(url, options)
     .then(data => { Download(data, filename); });
}
```

#### Arguments
| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
|fileId	|Long	|Required	|The id of the file you wish to download|
|revisionId	|Long	|Optional|	The id of the revision file you wish to download|

#### HTTP Request

For a basic file retrieval:

```text
GET /domo/data-files/v1/{fileId} HTTP/1.1
Accept: application/json
```

For a file revision retrieval:

```text
GET /domo/data-files/v1/{fileId}/revisions/{revisionId} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the File to be downloaded.

```text
HTTP/1.1 200 OK
Content-Type: {mime-type of the file}
```

### Delete a file
---
Permanently deletes a File from your instance.

<!-- theme: danger -->

> #### Warning
>
> This is destructive and cannot be reversed. However, the delete does occur at the revision level, so if you unintentionally delete a file, the previous version will now be the current version of the file for a given file Id.

#### Code Example

```js
function deleteFile(fileId, revisionId){
        const url = `/domo/data-files/v1/${fileId}/revisions/${revisionId}`;
        return domo.delete(url);
}
```

#### Arguments
| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
|fileId	|Long	|Required	|The id of the file you wish to delete|
|revisionId	|Long	|Optional	|The id of the revision file you wish to delete|

#### HTTP Request

```text
DELETE /domo/data-files/v1/{fileId}/revisions/{revisionId} HTTP/1.1
Accept: application/json
```

#### HTTP Response
Returns the parameter of success or error based on the file Id and the revisionId being valid.

```text
HTTP/1.1 200 OK
```

### Get file permissions
---
#### Code Example

```js
function getFilePermissions(fileId){
        const url = `/domo/data-files/v1/${fileId}/permissions`;
        return domo.get(url);
}
```

#### Arguments
| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
|fileId	|Long	|Required	|The id of the file you wish to get permission details for|

#### HTTP Request

```text
GET /domo/data-files/v1/{fileId}/permissions HTTP/1.1
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
---
#### Code Example

```js
function upadateFilePermissions(fileId, data){
        const url = `/domo/data-files/v1/${fileId}/permissions`;
        return domo.put(url, data)
}
```

#### Arguments
| Property Name| Type | Required | Description |
| --- | --- | --- | --- |
|fileId	|Long	|Required	|The id of the file you wish to update permission details for|

#### HTTP Request

```json
PUT /domo/data-files/v1/{fileId}/permissions HTTP/1.1
Accept: application/json
Request Body
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
