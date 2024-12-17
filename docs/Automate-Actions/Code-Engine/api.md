# Code Engine API

This API reference is useful if you are wanting to use your Code Engine functions outside of your Domo instance.

Each function in Code Engine is a serverless function that can be run on demand. You can pass in input variables and get back a result. You can also choose to get logs from the function execution.

If you are unfamiliar with how to authenticate against Product APIs, [please see this overview page](../Getting-Started/api-authentication.md).

## Run Function

**Method**: `POST`  
**Endpoint**: `/api/codeengine/v2/packages/{{packageId}}/versions/{{version}}/functions/{{functionName}}`

**Example**:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/codeengine/v2/packages/756f0b19-5125-44f6-b541-058980ff6a94/versions/1.0.1/functions/getExecutionDetails",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "inputVariables": {
        "paramName": any // these should match your function input parameters
    },
    "settings": { "getLogs": boolean }
  }
}
```

**Response**:

```json
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
{
    "executionId": string,
    "packageId": string,
    "version": string,
    "functionName": string,
    "status": string,
    "settings": {
        "getLogs": boolean
    },
    "startedOn": Date,
    "startedBy": string,
    "completedOn": Date,
    "result": any,
    "stdout": {
        "log": any[]
    },
    "stderr": {
        "log": any[]
    },
    "errorInformation": {
        "result": any,
        "expectedType": string,
        "actualType": string,
        "expectedIsList": boolean,
        "actualIsList": boolean,
        "expectedAllowNull": boolean,
        "errorMessages": string[]
    }
}
```
