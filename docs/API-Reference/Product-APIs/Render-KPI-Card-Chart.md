Render KPI Card Chart/Table
-------------------------------

### Authentication
Requests to the endpoints in this document should be authenticated using an access token.  The token should be passed using the `X-DOMO-Developer-Token` header.  For information about generating an access token see https://domo-support.domo.com/s/article/360042934494?language=en_US.

### HTTP Method: `PUT`

### URL

`/api/content/v1/cards/kpi/{urn}/render`

### Tags

*   `card-kpi-resource`

### Summary

This endpoint renders a KPI card chart or table based on the specified `urn`. It supports various parameters that allow the user to customize the output, such as locale and specific parts of the chart to render.

### Parameters

#### Path Parameters

*   **`urn`** (required):  
    The unique resource name (URN) of the KPI card that you want to render.
    *   **Schema:** `$ref: '#/components/schemas/CardURNParam'`

#### Query Parameters

*   **`locale`** (optional):  
    The locale in which to render the KPI card.
    
    *   **Type:** `string`
*   **`parts`** (required):  
    A list of specific parts of the chart to render. This allows for a targeted response that can include only the needed components.
    
    *   **Type:** `array` (unique items)
    *   **Items:** `string`
    *   **Enum:**
        *   `title`
        *   `chartType`
        *   `queryResult`
        *   `data`
        *   `image`
        *   `imagePDF`
        *   `graph`
        *   `dynamic`
        *   `summary`
        *   `summaryImage`
        *   `dataSource`
        *   `pdp`
        *   `annotations`
        *   `extendedDateInfo`
        *   `table`

### Request Body

The request body must be in JSON format and should conform to the `ChartRequest` schema.

*   **Content-Type:** `application/json`
*   **Schema:** `$ref: '#/components/schemas/ChartRequest'`

### Responses

#### 200 OK

The request was successful, and the KPI card chart has been rendered according to the specified parameters.

*   **Content-Type:** `application/json`
*   **Schema:** `$ref: '#/components/schemas/ChartResponse'`

#### 403 Forbidden

The request was not authorized. The client does not have the necessary permissions to access this resource.

#### 409 Conflict

The request could not be completed due to a conflict with the current state of the target resource.
