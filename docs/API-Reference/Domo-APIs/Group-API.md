# Group API

Fetch Group
-----------

**Method**: `GET`  
**Endpoint**: `/api/content/v2/groups/{group}`

**Path Parameters**:

*   `group` - The ID of the group to fetch
    *   Param Type: String
    *   Required

**Example**:

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/content/v2/groups/{group}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:  
The group object containing group details.

```json
200:
{
  "id": "string",
  "name": "string",
  "description": "string",
  "type": "string"
}
```

* * *

Fetch Members of a Group
------------------------

**Method**: `GET`  
**Endpoint**: `/api/identity/v1/users/{userId}?parts=detailed`

**Path Parameters**:

*   `userId` - The ID of each user to fetch details for
    *   Param Type: String
    *   Required

**Query Parameters**:

*   `parts`
    *   Param Type: String
    *   Param Options:
        *   `detailed`

**Example**:

```json
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/identity/v1/users/{userId}?parts=detailed",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:  
Detailed user information for each group member.

```json
200:
{
  "users": [
    {
      "attributes": [
        {
          "key": "displayName",
          "values": ["string"]
        },
        {
          "key": "employeeLocation",
          "values": ["string"]
        }
      ]
    }
  ]
}
```

* * *

Create a Group
--------------

**Method**: `POST`  
**Endpoint**: `/api/content/v2/groups`

**Example**:

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/content/v2/groups",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "name": "string",
    "description": "string",
    "type": "string"
  }
}
```

**Response**:  
The created group’s ID and details.

```json
200:
{
  "id": "string",
  "name": "string",
  "description": "string",
  "type": "string"
}
```

* * *

Add People to a Group
---------------------

**Method**: `PUT`  
**Endpoint**: `/api/content/v2/groups/{group}/user`

**Path Parameters**:

*   `group` - The ID of the group to which people will be added
    *   Param Type: String
    *   Required

**Example**:

```json
{
  "method": "PUT",
  "url": "https://{instance}.domo.com/api/content/v2/groups/{group}/user",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": [
    {
      "id": "string",
      "type": "USER"
    }
  ]
}
```

**Response**:  
Returns `true` if the call was successful.

* * *
Remove a Person from a Group
----------------------------

**Method**: `DELETE`  
**Endpoint**: `/api/content/v2/groups/{group}/removeuser/{person}`

**Path Parameters**:

*   `group` - The ID of the group
    *   Param Type: String
    *   Required
*   `person` - The ID of the person to remove
    *   Param Type: String
    *   Required

**Example**:

```json
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/content/v2/groups/{group}/removeuser/{person}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:  
Returns `true` if the call was successful.

* * *

Remove Multiple People from a Group
-----------------------------------

**Method**: `PUT`  
**Endpoint**: `/api/content/v2/groups/access`

**Example**:

```json
{
  "method": "PUT",
  "url": "https://{instance}.domo.com/api/content/v2/groups/access",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": [
    {
      "groupId": "string",
      "removeMembers": [
        {
          "type": "USER",
          "id": "string"
        }
      ]
    }
  ]
}
```

**Response**:  
Returns `true` if the call was successful.
