### Canceling a Workflow

---

Cancels an in progress Workflow. If you are unfamiliar with how to authenticate against Product APIs, [please see this overview page](../Getting-Started/api-authentication.md).

**Method**: `POST`  
**Endpoint**: `/api/workflow/v1/instances/${instanceId}/cancel`  
**Path Parameters**:

- `id` - The ID of the Workflow instance to cancel
  - String
  - Required

**Example**

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/workflow/v1/instances/${instanceId}/cancel",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
  "id": string,
  "modelId": string,
  "deploymentId": string,
  "modelName": string,
  "modelVersion": string,
  "bpmnProcessId": string,
  "bpmnProcessName": string,
  "createdBy": string,
  "createdOn": string,
  "updatedBy": string,
  "updatedOn": string,
  "status": string,
  "isTestRun": boolean
}
```
