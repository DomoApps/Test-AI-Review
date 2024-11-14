# Users API

## Create

**Method**: `POST`  
**Endpoint**: `/api/identity/v1/users`

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
    "displayName": string,
    "emailAddress": string,
    "roleId": number
}
}
```

**Response**:

```json
200:
  {
    "attributes": [
      {
        "key": string,
        "values": number|string[]
      },
    ],
    "id": number,
    "displayName": string,
    "userName": string,
    "roleId": number,
    "emailAddress": string
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
  "users": [
    {
      "attributes": [
        {
          "key": string,
          "values": number|string[]
        },
      ],
      "id": number,
      "displayName": string,
      "userName": string,
      "roleId": number,
      "emailAddress": string
    }
  ]
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
  "users": [
    {
      "attributes": [
        {
          "key": string,
          "values": number|string[]
        },
      ],
      "id": number,
      "displayName": string,
      "userName": string,
      "roleId": number,
      "emailAddress": string
    }
  ]
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

**Example**:

```json http
{
  "method": "PATCH",
  "url": "https://{instance}.domo.com/api/identity/v1/users/{id}",
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

```json
200:
  {
    "attributes": [
      {
        "key": string,
        "values": number|string[]
      },
    ],
    "id": number,
    "displayName": string,
    "userName": string,
    "roleId": number,
    "emailAddress": string
  }
```

---

## Delete User

**Method**: `DELETE`  
**Endpoint**: `/api/identity/v1/users/{id}`  
**Path Parameters**:

- `id` - Id of the user requested.
  - Integer
  - Required

**Example**:

```json http
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/identity/v1/users/{id}",
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

```json
200: 1 (represents number of deleted records)

404:
  {
      "status": 404,
      "statusReason": "string",
      "message": "string"
      "toe": "string"
  }
```
