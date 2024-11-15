
# Pages API

**Create Subpage**
----------------------

**Method**: `POST`  
**Endpoint**: `/api/content/v1/pages`

**Request Parameters**:

*   `parentPageId` - The ID of the parent page where the new subpage will be created.
    *   Param Type: String
    *   Required
*   `title` - The title of the subpage.
    *   Param Type: String
    *   Required
*   `hasLayout` - Specifies if the page should have a layout.
    *   Param Type: Boolean
    *   Optional
    *   Default: true

**Example**:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v1/pages",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "parentPageId": "12345",
    "title": "New Subpage Title",
    "hasLayout": true
  }
}
```

**Response**:  

*   **Success (200)**: Page created successfully.
*   **Forbidden (403)**: Operation not permitted.
*   **Conflict (409)**: Conflict encountered, such as a duplicate title.

```json
200:
{
  "id": "string",
  "background": {
    "type": "STRING",
    "dark": {
      "value": "string",
      "opacity": "string",
      "type": "STRING"
    },
    "light": {
      "value": "string",
      "opacity": "string",
      "type": "STRING"
    }
  },
  "isDynamic": true,
  "density": {
    "compact": 0,
    "standard": 0
  }
}
```

---
**Bulk Move Pages**
-----------------------

**Method**: `PUT`  
**Endpoint**: `/api/content/v1/pages/bulk/move`

**Request Parameters**:

*   `pageIds` - IDs of pages to move.
    *   Param Type: Array of Numbers
    *   Required
*   `parentPageId` - ID of the new parent page.
    *   Param Type: Number
    *   Required
*   `pagePermission` - Permission for the pages.
    *   Param Type: String
    *   Required
    *   Param Options:
        *   `"ORIGINAL"`

**Example**:

```json
{
  "method": "PUT",
  "url": "https://{instance}.domo.com/api/content/v1/pages/bulk/move",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "pageIds": [123, 456],
    "parentPageId": 789,
    "pagePermission": "ORIGINAL"
  }
}
```

**Response**:  

*   **Success (200)**: Pages moved successfully.
*   **Forbidden (403)**: Permission denied.
*   **Conflict (409)**: Conflict encountered, such as permission constraints.

---
**Revoke Page Access**
--------------------------

**Method**: `DELETE`  
**Endpoint**: `/api/content/v1/share/page/{pageId}/user/{personId}`

**Path Parameters**:

*   `pageId` - ID of the page for access revocation.
    *   Param Type: Number
    *   Required
*   `personId` - ID of the user whose access is being revoked.
    *   Param Type: Number
    *   Required

**Example**:

```json
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/content/v1/share/page/12345/user/67890",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:  

*   **Success (200)**: Access revoked successfully.
*   **Forbidden (403)**: Operation not permitted.
*   **Conflict (409)**: Conflict encountered while attempting to revoke access.

---