# API Markdown Template

The following represents best practices for documenting Product APIs in the Domo Developer Portal. Please include all information available based on the below template.

In addition, here are a few best practice rules to follow:

1. Don't include a table on contents in the markdown file. In the developer portal, this gets created automatically based on the header structure. Please use h1 for the title of the article and h2 for the title of each endpoint.
2. Please use a table with the following structure for any parameters that the endpoint takes. Here is an example:

| Property Name | Type                       | Required          | Description                                                                                   |
| ------------- | -------------------------- | ----------------- | --------------------------------------------------------------------------------------------- |
| count         | Number                     | no. default is 10 | How many results to return                                                                    |
| offset        | Number                     | no. default is 0  | The results offset. The count and offset can only be used to return a total of 10,000 records |
| query         | String                     | yes               | The query term. Use \* for wildcard                                                           |
| filters       | Array of [Filter](#filter) | no                | Search results must match ALL filters.                                                        |
| orFilters     | Array of [Filter](#filter) | no                | Search results must match ANY filter.                                                         |
| notFilters    | Array of [Filter](#filter) | no                | Search results must NOT match any filter.                                                     |

3. Please do not use http keyword tag for code snippets (e.g. ```http). Instead use the "text" or "json" keywords to format the code snippet.
4. In examples, please use sample data rather than just noting the type of the data expected.
5. Some parameters can only receive a limited set of options. In cases, where there is a limit, please include a list of valid options.

## Create

**Method**: `POST`  
**Endpoint**: `/api/<endpoint>`

**Example**:

```json
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
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
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

```json
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

- `param 1` - Provide description of the param
  - Param Type [String, Integer, Boolean, etc.]
  - Required or Optional

**Example**:

```json
{
	"method": "PUT",
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
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
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

```json
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
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  {}

```
