# Speech-Analytics-API-Examples
Marsview Speech Analytics API
Python client end code for Marsview Speech Analytics APIs

## Step 1:
Signup on [Marsview portal](app.marsview.ai) and fetch API Key and API Token
Update these values in config.py


## Step 2:
A couple of sample configurations for using Speech Analytics APIs are provided in config.py

These configurations can be used as is or modified to meed specific requirements

Refer to [API docs](https://docs.marsview.ai/speech-analytics-api/compute-metadata/configuring-models) or more information on how to configure models.

## Step 3:
running main.py
Note: Modify the Recording file path and the Config.
Main.py has 4 stages
- Stage 1: Get Generate JWT Token
- Stage 2: Upload local file and get Transaction_ID (txn_id)
- Stage 3: Send a compute request on the Transaction_ID (txn_id)
- Stage 4: Long poll for the status of the compute request untill the model completes processing.
- Stage 5: Fetch Metadata on the Transaction_ID

