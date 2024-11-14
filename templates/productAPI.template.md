# API Markdown Template

## Create

**Method**: `POST`  
**Endpoint**: `/api/<endpoint>`

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/<endpoint>",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {}
}
```

**Response**:  
Description of the Response with an example of the data

```json
200:
{}

```

---

## Read

**Method**: `GET`  
**Endpoint**: `/api/<endpoint>/{param 1}`  
**Path Parameters**:

- `param 1` - Provide description of the param
  - Param Type [String, Integer, Boolean, etc.]
  - Required or Optional

**Query Parameters**:

- `queryParam1`
  - Param Type [String, Integer, Boolean, etc.]
  - Required or Optional
  - Param Options
    - Option 1
    - Option 2
    - Option 3

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/<endpoint>/{param 1}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:  
Description of the Response with an example of the data

```json
200:
{}

```

---

## Update

**Method**: `PUT`  
**Endpoint**: `/api/<endpoint>`  
**Path Parameters**:

- `param 1` - (Param Type [String, Integer, Boolean, etc.], Required or Optional) - Provide description of the param

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/<endpoint>/{param 1}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {}
}
```

**Response**:  
Description of the Response with an example of the data

```json
200:
{}

```

---

## Delete

**Method**: `DELETE`  
**Endpoint**: `/api/<endpoint>/{param 1}`  
**Path Parameters**:

- `param 1` - Provide description of the param
  - Param Type [String, Integer, Boolean, etc.]
  - Required or Optional

**Example**:

```json http
{
  "method": "DELETE",
  "url": "https://{instance}.domo.com/api/<endpoint>/{param 1}",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  }
}
```

**Response**:  
Description of the Response with an example of the data

```json
200:
{}

```
