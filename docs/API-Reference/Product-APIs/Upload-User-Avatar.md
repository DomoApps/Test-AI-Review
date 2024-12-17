## Upload User avatars

**Method**: `POST`  
**Endpoint**: `/avatar/uploaduserimage/<USER_ID>`

**Example**:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/avatar/uploaduserimage/<USER_ID>",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": <BASE_64_ENCODED_IMAGE>
}
```

**Response**:  

```json
200:
{}

```
