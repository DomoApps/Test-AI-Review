---
stoplight-id: wjqiqhsvpadon
---

# AI Service Layer API

Domo's AI Service Layer enables developers to build AI capabilities into their Domo Apps. In particular, the AI Service Layer currently supports two services from within Apps:

1. Text Generation
2. Text-to-SQL

Domo allows you to configure which models power each of the services. For more on how that works, [see this video](https://www.youtube.com/live/f4L7bc52snE?feature=share&t=549).

You can also see example usage of the the Text Generation and the Text-to-SQL in the AI Domo Bricks currently available to download for free in the Domo AppStore.

- [AI ChatGPT Brick](https://www.domo.com/appstore/app/ai-chatgpt-brick/overview)
- [ChatGPT Dataset Description Brick](https://www.domo.com/appstore/app/chatgpt-dataset-description-brick/overview)
- [ChatGPT Text-To-SQL Query Brick](https://www.domo.com/appstore/app/explain-sql-with-ai/overview)

### Text Generation

---

Generates a text response from a text prompt.

#### Code Example

The `body` variable in this post request is an example of a sample request body.

```javascript
const prompt = "Tell me a joke about data.";
const body = {
	input: prompt,
};

domo
	.post(`/domo/ai/v1/text/generation`, body)
	.then((response) => console.log(response));
```

#### Arguments

| Property Name  | Type   | Required | Description                                                                                                                   |
| -------------- | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| input          | String | Required | The prompt you are sending to the model                                                                                       |
| promptTemplate | Object | Optional | An override for the prompt template used in the service. It has one property `template`, which expects a string.              |
| parameters     | Object | Optional | Used with the `promptTemplate` for additional customization. You can pass any key, value pair of strings. See examples below. |
| model          | String | Optional | The id of the model you'd like to use if you don't want to use the default model.                                             |

#### HTTP Request

```text
POST /domo/ai/v1/text/generation HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### Request Body

The only required field in the request body is the `input` string, but you can provide additional properties in the request body to futher customize the text generation service. If you choose to use the `promptTemplate` property to override the default prompt template, you'll need to use `${input}` into the template string to pass through the input of your prompt.

```json
{
	"input": "Recap the 2021 superbowl",
	"promptTemplate": {
		"template": "${input}. You are a helpful assistant that gives answers in ${max_words} words or less"
	},
	"parameters": {
		"max_words": "30"
	},
	"model": "8dc5737d-0bc8-425b-ad0d-5d6ec1a99e72"
}
```

#### HTTP Response

Returns the prompt used and the responses from the model. If the a model was specified in the request, then `modelId` will return the model and `isCustomerModel` will be true.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "prompt": "Recap the 2021 superbowl",
    "choices": [
      {
        "output": "The 2021 Super Bowl, also known as Super Bowl LV, took place on February 7, 2021 and James Stadium ..."
      }
    ],
    "modelId": "8dc5737d-0bc8-425b-ad0d-5d6ec1a99e72",
    "isCustomerModel": true

}
```

### Text-to-SQL

---

Generates a SQL query based on a prompt and a DataSet's schema.

#### Code Example

The `body` variable in this post request is an example of a sample request body.

```javascript
const exampleDataSourceSchema = {
	dataSourceName: "Sales",
	description: "Sales Data",
	columns: [
		{
			name: "Date",
			type: "date",
		},
		{
			name: "Sales",
			type: "number",
		},
	],
};
const body = {
	input: "Show me the sales for the last 3 months.",
	dataSourceSchemas: [exampleDataSourceSchema],
};

domo
	.post(`/domo/ai/v1/text/sql`, body)
	.then((response) => console.log(response));
```

#### Arguments

| Property Name     | Type             | Required | Description                                                                                                                   |
| ----------------- | ---------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| input             | String           | Required | The prompt you are sending to the model                                                                                       |
| promptTemplate    | Object           | Optional | An override for the prompt template used in the service. It has one property `template`, which expects a string.              |
| parameters        | Object           | Optional | Used with the `promptTemplate` for additional customization. You can pass any key, value pair of strings. See examples below. |
| model             | String           | Optional | The id of the model you'd like to use if you don't want to use the default model.                                             |
| dataSourceSchemas | Array of Objects | Optional | The schemas of datasets that they service should take into account when generating the SQL query from the input prompt.       |

#### HTTP Request

```text
POST /domo/ai/v1/text/sql HTTP/1.1
Content-Type: application/json
Accept: application/json
```

#### Request Body

The only required field in the request body is the `input` string, but you can provide additional properties in the request body to futher customize the text generation service. If you choose to use the `promptTemplate` property to override the default prompt template, you'll need to use `${input}` into the template string to pass through the input of your prompt.

```json
{
	"input": "Create a sql query to show me total sales.",
	"promptTemplate": {
		"template": "${input}. Show me the ${measure} for the last ${timeframe}"
	},
	"parameters": {
		"measure": "sales",
		"timeframe": "3 months"
	},
	"model": "8dc5737d-0bc8-425b-ad0d-5d6ec1a99e72",
	"dataSourceSchemas": [
		{
			"dataSourceName": "Sales",
			"description": "Sales Data",
			"columns": [
				{
					"name": "Date",
					"type": "date"
				},
				{
					"name": "Sales",
					"type": "number"
				}
			]
		}
	]
}
```

#### HTTP Response

Returns the prompt used and the response options from the model. If the a model was specified in the request, then `modelId` will return the model and `isCustomerModel` will be true.

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
    "prompt": "You are a helpful assistant that generates SQL queries. Table `Voter Registration`, columns=[State:string, County:string, Party:string, Registered Voters: number, Total Votes:number]. Find the total votes by party in each county in the state of Utah. Use column aliases only for functions. Do not elaborate.",
    "choices": [
      {
        "output": "SELECT County, Party, SUM(`Total Votes`) AS TotalVotes FROM `Voter Registration` WHERE State = 'Utah' GROUP BY County, Party"
      }
    ],
    "modelId": "8dc5737d-0bc8-425b-ad0d-5d6ec1a99e72",
    "isCustomerModel": true
}
```
