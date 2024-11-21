### Changing a Workflow's Permissions

---

Changes the permissions of a workflow.

#### HTTP Request

```text
POST https://{instance}.domo.com/api/workflow/v1/models/${modelId}/permissions`
```

#### Request Body

| Property Name | Type   | Required | Description                   |
| ------------- | ------ | -------- | ----------------------------- |
| modelId       | String | Required | The id of the workflow model. |

#### Example

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/workflow/v1/models/${modelId}/permissions",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    [
        {
            "id": "123456",
            "permissions": [
                "ADMIN",
                "SHARE",
                "DELETE",
                "WRITE",
                "READ",
                "EXPORT",
                "EXECUTE",
                "UPDATE_CONTENT"
            ],
            "name": "John Doe",
            "type": "USER"
        },
        {
            "id": "98765",
            "name": "John Smith",
            "type": "USER",
            "permissions": [
                "READ"
            ]
        }
    ]
  }
}
```

#### HTTP Response

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
```

TODO: Do we want to show them how to get the permissions to verify that they updated?
