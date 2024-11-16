## Export to S3

Export a dataset to an S3 bucket.

Export your datasets to an S3 device of your choosing. This is an asynchronous call. You can see the status of your export by calling /api/query/v1/export/{datasetId}. You can have only one actively running export for a given dataset at a time. If you make a request to export a dataset and the data in the dataset hasn’t changed since the last export this endpoint will return the export information for that previous export, a new download will not be created. You should use temporary AWS credentials whenever possible. If the credentials are temporary you must also provide an AWS session token.

If is important that the customer consider the security of the data they are exporting. In order to export a datasource the consumer must have at least read access to the dataset, also any PDP policies that exist will be applied to the upload. But once the data is uploaded the only security around the data is what is provided by the AWS S3 bucket. This means the customer must carefully consider the security of the upload location. A customer should not upload data to an S3 location that others can view who should not have access to the data that is contained in the upload.

For example, a customer has a dataset that contains compensation information. They have carefully limited those who have access to the dataset in the DOMO system. They have also applied PDP policies so that managers can only see the compensation information in the dataset for their reporting structure. Then an administrator initiates an export to an S3 location. However, the admin provides an S3 location that the entire company has access to. Now the entire company can see the compensation information tracked in this dataset. The security provided by the DOMO system is now voided.

Cross region exports are unsupported at this time. The ‘REGION’ setting in the payload must match the region of the S3 bucket you want to copy data to. If your bucket is in the `eu-west-3` region, the region value should be ‘eu-west-3’.


**Method**: `POST`  
**Endpoint**: `api/query/v1/export/<DATASOURCE_ID>`

**Example**:

```json http
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/query/v1/export/<DATASOURCE_ID>",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json",
    "Charset": "UTF-8"
  },
  "body": { 
   "awsAccessKey":"<AWS_KEY>",
   "awsAccessSecret":"<AWS_SECRET>",
   "bucket":"<BUCKET>",
   "path":"<PATH>",
   "region":"<REGION>",
   "queryRequest":{ 
      "includeBOM":true,
      "useCache":true,
      "query":{ 
         "columns":[ 
            { 
               "column":"Customer ID",
               "exprType":"COLUMN"
            },
            { 
               "column":"Cardholder ID",
               "exprType":"COLUMN"
            },
            { 
               "column":"Sex of Patient",
               "exprType":"COLUMN"
            },
            { 
               "column":"Date Filled",
               "exprType":"COLUMN"
            },
            { 
               "column":"Label Name",
               "exprType":"COLUMN"
            },
            { 
               "column":"Metric Quantity",
               "exprType":"COLUMN"
            },
            { 
               "column":"Days Supply",
               "exprType":"COLUMN"
            }
         ],
         "groupByColumns":[ 

         ],
         "orderByColumns":[ 

         ]
      }
   }
}

Responses

200	
An export job has been successfully created. Note: you must check the status of the export job on the return or when calling the status endpoint. A created export may have an error preventing it from completing the download of data.

Example Value
Model
{ 
   "bucket":"string",
   "compression":"none",
   "errorCode":"string",
   "exportFormat":"csv",
   "exportId":"97d1244b-8ec4-45f8-a721-ae9602a9fa77",
   "exportStatus":"none",
   "finished":"2019-09-19T15:09:10.086Z",
   "message":"string",
   "started":"2019-09-19T15:09:10.086Z",
   "tempUrlRowCountMap":{ 
      "additionalProp1":0,
      "additionalProp2":0,
      "additionalProp3":0
   },
   "urlRowCountMap":{ 
      "additionalProp1":0,
      "additionalProp2":0,
      "additionalProp3":0
   }
}

201	
Created

400	
The request is invalid and an export cannot be created.

401	
Access is denied. Your token is invalid or expired.

403	
To access this endpoint you must have READ rights on the dataset, or have dataset administrative authority (dataset.admin).

404	
If the dataset id cannot be found in the customer instance.

500	
An unexpected error happened.
```

**Example Body – Filter by Region column:**
```
"body": { 
   "awsAccessKey":"<AWS_KEY>",
   "awsAccessSecret":"<AWS_SECRET>",
   "bucket":"<BUCKET>",
   "path":"<PATH>",
   "region":"<REGION>",
   "queryRequest":{ 
      "includeBOM":true,
      "useCache":true,
      "query":{ 
         "columns":[ 
            { 
               "column":"Product Container",
               "exprType":"COLUMN"
            },
            { 
               "column":"Product Category",
               "exprType":"COLUMN"
            },
            { 
               "column":"Order ID",
               "exprType":"COLUMN"
            },
            { 
               "column":"Order Date",
               "exprType":"COLUMN"
            },
            { 
               "column":"Order Priority",
               "exprType":"COLUMN"
            },
            { 
               "column":"Region",
               "exprType":"COLUMN"
            },
            { 
               "column":"Ship Mode",
               "exprType":"COLUMN"
            }
         ],
         "groupByColumns":[ 

         ],
         "orderByColumns":[ 

         ],
         "where":{ 
            "exprType":"EQUALS",
            "leftExpr":{ 
               "column":"Region",
               "exprType":"COLUMN"
            },
            "rightExpr":{ 
               "value":"West",
               "exprType":"STRING_VALUE"
            }
         }
      }
   }
}
```

## Get the export status for all existing exports on this datasource.

**Method**: `GET`  
**Endpoint**: `api/query/v1/export/<DATASOURCE_ID>`

**Example**:

```json http
{
  "method": "GET",
  "url": "https://{instance}.domo.com/api/query/v1/export/<DATASOURCE_ID>",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json",
    "Charset": "UTF-8"
  },
  "body": {}

Responses

200
Returns the status of all existing exports on this datasource. A given export is not available for download until the exportStatus is 'success’.

[ 
   { 
      "bucket":"string",
      "compression":"none",
      "errorCode":"string",
      "exportFormat":"csv",
      "exportId":"97d1244b-8ec4-45f8-a721-ae9602a9fa77",
      "exportStatus":"none",
      "finished":"2019-09-19T15:06:46.112Z",
      "message":"string",
      "started":"2019-09-19T15:06:46.112Z",
      "tempUrlRowCountMap":{ 
         "additionalProp1":0,
         "additionalProp2":0,
         "additionalProp3":0
      },
      "urlRowCountMap":{ 
         "additionalProp1":0,
         "additionalProp2":0,
         "additionalProp3":0
      }
   }
]

401	
Access is denied. Your token is invalid or expired.

403	
To access this endpoint you must have READ rights on the dataset, or have dataset administrative authority (dataset.admin).

404	
If the dataset id cannot be found in the customer instance.

500	
An unexpected error happened.
```
