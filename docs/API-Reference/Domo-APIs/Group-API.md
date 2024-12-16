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
    "id": 6789456782,
    "name": "Group Name",
    "type": "closed",
    "userIds": [
        123123123,
        342342344,
        555543423,
        432423423
    ],
    "creatorId": 4421231232,
    "memberCount": 4,
    "guid": "guid-goes-here",
    "description": "",
    "hidden": false,
    "default": false,
    "active": true
}
```

* * *

Fetch User Details
------------------------

Please use the Fetch Group API to get the list of members in a group, and use that same list of user ids to fetch the details for each member.

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
Detailed user information for each user. 

```json
200:
{
  [
    {
      "name": "Domo User",
      "id": 3817263817,
      "location": "",
      "manager": "",
      "phoneNumber": "+phone number",
      "title": "Software Engineer",
    },
  ]
}
```

* * *

Create a Group
--------------

**Method**: `POST`  
**Endpoint**: `/api/content/v2/groups`

**body Parameters**:

*   `name` - Name for the group
*   `description` - Description for the group
*   `type` - can be 'closed', 'open', or 'dynamic'

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
    "name": "New Group",
    "description": "This is a new group",
    "type": "closed"
  }
}
```

**Response**:  
The created group’s ID.

```json
200:
{
  "id": "123123123",
}
```

* * *

Add People to a Group
---------------------

**Method**: `PUT`  
**Endpoint**: `/api/content/v2/groups/{group}/user/{userId}`

**Path Parameters**:

*   `group` - The ID of the group to which people will be added
    *   Param Type: String
    *   Required
*   `userId` - The ID of the person to add to the group
    *   Param Type: String
    *   Required

**Example**:

```json
{
  "method": "PUT",
  "url": "https://{instance}.domo.com/api/content/v2/groups/{group}/user/{userId}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
}
```

**Response**:  
Returns `true` if the call was successful.

* * *
Remove a Person from a Group
----------------------------

**Method**: `DELETE`  
**Endpoint**: `/api/content/v2/groups/{group}/removeuser/{userId}`

**Path Parameters**:

*   `group` - The ID of the group
    *   Param Type: String
    *   Required
*   `userId` - The ID of the person to remove
    *   Param Type: String
    *   Required

**Example**:

```json
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/content/v2/groups/{group}/removeuser/{userId}",
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
      "groupId": "1231231232",
      "removeMembers": [
        {
          "type": "USER",
          "id": "112321221"
        }
      ]
    }
  ]
}
```

**Response**:  
Returns `true` if the call was successful.
