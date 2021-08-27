# Speech-Analytics-API-Examples
Marsview Speech Analytics API
Python client end code for Marsview Speech Analytics APIs

## Step 1:
Signup on [Marsview portal](app.marsview.ai) and fetch API Key and API Token
Update these values in config.py
![IM-1](https://gblobscdn.gitbook.com/assets%2F-MaxSab-_c4clZreM9ft%2F-McUJSnRlslrM7wCcAdb%2F-McUJx4lF7WPJBxCsk4o%2FScreenshot%202021-06-18%20at%207.02.35%20PM.png?alt=media&token=c466bae4-6b04-4b85-b1eb-4ed02a169538)


## Step 2:
A couple of sample configurations for using Speech Analytics APIs are provided in config.py
![image](https://user-images.githubusercontent.com/89631839/131158660-69d1f169-80a8-4113-b55c-2bba482bab92.png)

Shown above is the configuration for running speech-to-text with topics ans suggested-intents enabled.

These configurations can be used as is or modified to meed specific requirements. Refer to [API docs](https://docs.marsview.ai/speech-analytics-api/compute-metadata/configuring-models) or more information on how to configure models.

## Step 3:
running main.py
Note: Modify the Recording file path and the Config.
Main.py has 4 stages
- Stage 1: Get Generate JWT Token
- Stage 2: Upload local file and get Transaction_ID (txn_id)
- Stage 3: Send a compute request on the Transaction_ID (txn_id)
- Stage 4: Long poll for the status of the compute request untill the model completes processing.
- Stage 5: Fetch Metadata on the Transaction_ID

## Step 4:
Visualise the output using the **'experienceUrl'** in the metadata or by visiting [Marsview portal](app.marsview.ai)

![image](https://user-images.githubusercontent.com/89631839/131159474-1600043f-4a30-4a9a-ab92-47a418bc275b.png)
