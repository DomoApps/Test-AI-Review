---
stoplight-id:
---

# Alerts API

Summary

## Get an alert

Gets an existing alert by id.

#### Code Example

```js
function getAlert(alertId) {
  const url = `/api/social/v4/alerts/${alertId}`;
  const response = await fetch(url);
  return await response.json();
}
```

#### Path Parameters

| Property Name | Type    | Description                         |
| ------------- | ------- | ----------------------------------- |
| alertId       | Integer | The id of the alert you want to get |

#### Query Parameters

| Property Name | Type   | Required | Description |
| ------------- | ------ | -------- | ----------- |
| fields        | String | Optional |             |

#### HTTP Request

```text
GET /api/social/v4/alerts/{alertId} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the alert.

```text
HTTP/1.1 200 OK
TODO
```

## Delete an alert

Deletes an existing alert by id.

#### Code Example

```js
function deleteAlert(alertId) {
  const url = `/api/social/v4/alerts/${alertId}`;
  const response = await fetch(url, {
    method: 'DELETE'
  });
  return await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                            |
| ------------- | ------- | -------- | -------------------------------------- |
| alertId       | Integer | Required | The id of the alert you want to delete |

#### HTTP Request

```text
DELETE /api/social/v4/alerts/{alertId} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the parameter of success or error based on the alert id being valid.

```text
HTTP/1.1 200 OK
```

## Subscribe user to an alert

This endpoint subscribes a Domo user to an existing alert.

#### Code Example

```js
function subscribeToAlert(alertId, userId) {
  const url = `/api/social/v4/alerts/${alertId}/subscriptions`;
  const response = await fetch(url, {
    body: JSON.stringify({ subscriberId: userId, type: 'USER' })
  });
  return await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                                           |
| ------------- | ------- | -------- | ----------------------------------------------------- |
| alertId       | Integer | Required | The id of the alert you want to subscribe the user to |

#### HTTP Request

```text
POST /api/social/v4/alerts/{alertId}/subscriptions HTTP/1.1
Accept: application/json
```

#### Request Body

The request body includes the user id and a 'USER' type param.

```json
{
  "subscriberId": 12345,
  "type": "USER"
}
```

#### HTTP Response

Returns the parameter of success or error based on the alert id being valid.

```text
HTTP/1.1 200 OK
```

## Unsubscribe user from an alert

This endpoint unsubscribes a Domo user from an existing alert.

#### Code Example

```js
function unsubscribeFromAlert(alertId, userId) {
  const url = `/api/social/v4/alerts/${alertId}/subscriptions?subscriberId=${userId}&type=USER`;
  const response = await fetch(url, {
    method: 'DELETE'
  });
  return await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                                           |
| ------------- | ------- | -------- | ----------------------------------------------------- |
| alertId       | Integer | Required | The id of the alert you want to subscribe the user to |

#### Query Parameters

| Property Name | Type    | Required | Description                                                       |
| ------------- | ------- | -------- | ----------------------------------------------------------------- |
| subscriberId  | Integer | Required | The id of the entity unsubscribing from the alert                 |
| type          | String  | Required | The entity type, can be USER, GROUP, BUZZ, DAILY, WEEKLY, or AUTO |

#### HTTP Request

```text
POST /api/social/v4/alerts/{alertId}/subscriptions?subscriberId={subscriberId}&type={type} HTTP/1.1
Accept: application/json
```

#### HTTP Response

Returns the parameter of success or error based on the alert id being valid.

```text
HTTP/1.1 200 OK
```

## Share an alert

This endpoint shares an existing alert with a Domo user.

#### Code Example

```js
function shareAlert(alertId, userId, message, email) {
  const url = `/api/social/v4/alerts/${alertId}/share`;
  const payload = {
    userMessage: message,
    alertSubscriptions: [{ subscriberId: userId, type: 'USER' }],
    sendEmail,
    metaData: {}
  };
  const response = await fetch(url, {
    body: JSON.stringify(payload)
  });
  return await response.json();
}
```

#### Arguments

| Property Name | Type    | Required | Description                                           |
| ------------- | ------- | -------- | ----------------------------------------------------- |
| alertId       | Integer | Required | The id of the alert you want to subscribe the user to |

#### HTTP Request

```text
POST /api/social/v4/alerts/{alertId}/share HTTP/1.1
Accept: application/json
```

#### Request Body

| Property Name      | Type     | Required | Description                                                                 |
| ------------------ | -------- | -------- | --------------------------------------------------------------------------- |
| userMessage        | String   | Required | The message you want to send to the person                                  |
| alertSubscriptions | Object[] | Required | The entities you want to share the alert with. See above for entity params. |
| sendEmail          | Boolean  |          | Whether or not to send an email to the person once the alert is shared      |
| metaData           | Object   |          |                                                                             |

```json
{
  "userMessage": "I think you'll find this alert useful",
  "alertSubscriptions": [{ "subscriberId": 12345, "type": "USER" }],
  "sendEmail": true,
  "metaData": {}
}
```

#### HTTP Response

Returns the parameter of success or error based on the alert id being valid.

```text
HTTP/1.1 200 OK
```
