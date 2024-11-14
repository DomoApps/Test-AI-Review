# Users API

## Create

**Method**: `POST`  
**Endpoint**: `/api/identity/v1/users`

**Request Body**:  
Description of the Request body and its contents along with an example of the data if it is not multi-part form data

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/identity/v1/users",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "displayName": "User Display Name",
    "emailAddress": "User Email",
    "roleId": user Role Id (Integer)
}
}
```

**Response**:

```json
200:
{
  "attributes": [List of user profile attributes ],
  "id": user id (Integer),
  "displayName": "display name",
  "userName": "user email",
  "roleId": provided role id (Integer),
  "emailAddress": "user email"
}

400:
{
    "status": 400,
    "statusReason": "Bad Request",
    "message": "",
    "toe": ""
}
```

---

## Get User By Id

**Method**: `GET`  
**Endpoint**: `/api/identity/v1/users/{id}`  
**Path Parameters**:

- `id`- Id of the user requested.
  - Integer
  - Required

**Optional Query Parameters**:

- `parts`
  - Options
    - MINIMAL
    - SIMPLE
    - DETAILED
    - GROUPS
    - ROLE
  - Example
    - `/api/identity/v1/users/{id}?parts=DETAILED`

**Example**

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/identity/v1/users/{id}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:

```json
200:
{
  "users": [Array containing information for specified user]
}
```

---

## Get All Users

**Method**: `GET`  
**Endpoint**: `/api/identity/v1/users`

**Optional Query Parameters**:

- `parts`
  - Options
    - MINIMAL
    - SIMPLE
    - DETAILED
    - GROUPS
    - ROLE
  - Example
    - `/api/identity/v1/users?parts=DETAILED`

**Example**

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/identity/v1/users",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:

```json
200:
{
  "users": [Array containing information for all users]
}
```

---

## Update User

**Method**: `PATCH`
**Endpoint**: `/api/identity/v1/users/{id}`
**Path Parameters**:

- `id` - Id of the user requested.
  - Integer
  - Required

**Request Body**:
Object containing properties to update

**Example**

```json http
{
  "method": "PATCH",
  "url": "https://{instance}.domo.com/api/identity/v1/users",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json",
    "body": {
      "roleId": 5
    }
  }
}
```

**Response**:  
200: Returns updated user object

400: Bad Request - Validate your provided JSON

---

## Delete

**Method**: `DELETE`  
**Endpoint**: `/api/<endpoint>/{param 1}`  
**Path Parameters**:

- `param 1` (<datatype, String, Number, Boolean etc. >, <Required | Optional>) - Description of the param.

**Response**:  
Description and example of the response
