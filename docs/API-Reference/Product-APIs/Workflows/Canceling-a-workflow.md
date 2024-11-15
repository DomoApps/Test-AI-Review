### Canceling a Workflow

---

Cancels an in progress Workflow.

#### HTTP Request

```text
POST https://{instance}.domo.com/api/workflow/v1/instances/${instanceId}/cancel`
```

#### Request Body

| Property Name | Type   | Required | Description                                                                                                         |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------- |
| instanceId    | String | Required | The id of the workflow instance. Note: this is not the model id, but the id generated when the workflow is started. |

> It is important to note that the instance id is not the model's id, but the id generated when the workflow is started. You will receive this from the api call to start a workflow or it will be available in the list of executions online.
>
> There is no body sent with this request.

#### Example

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

#### HTTP Response

Returns the information about the instance of the Workflow that was just canceled. Note: The `status` property can take the values `null`, `IN_PROGRESS`, `CANCELED`, or `COMPLETED` and does not reflect the outcome of the cancel call. It takes a moment for the cancel to be processed and this is the status of the workflow at the time the request was sent.

A status of `null` might be valid. It just means the workflow hasn’t reported back as started yet.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "id": "613b7df4-761a-498c-ba25-fd9ae7b5df5b", // id of the newly created workflow instance
  "modelId": "f5d7bbff-0f7b-455b-b9e1-b96970beaf90", // id of the workflow
  "deploymentId": "e9539999-35be-460f-8727-263c1d1e409f",
  "modelName": "AddTwoNumbers", // name of workflow model
  "modelVersion": "1.3.10", // workflow version number
  "bpmnProcessId": "Process_f5d7bbff-0f7b-455b-b9e1-b96970beaf90_1.3.10_1",
  "bpmnProcessName": "domo AddTwoNumbers 1.3.10 1",
  "createdBy": "1325917757", // user id of workflow creator
  "createdOn": "2024-11-15T15:57:17.082Z",
  "updatedBy": "1325917757", // id of the last user to update the workflow
  "updatedOn": "2024-11-15T15:57:17.197Z",
  "status": "IN_PROGRESS", // workflow status when cancel request was sent
  "isTestRun": false
}
```
