from marsview.speechAnalytics import SpeechAnalyticsAPI
import config
#--
import json
from pprint import pprint


if __name__ == "__main__":
    #step 1 (Create JWT Token)
    sapi = SpeechAnalyticsAPI(
        apiKey = config.API_KEY,
        apiToken = config.API_TOKEN,
        userId = config.USER_ID
    )
    
    #step 2 (Upload file)
    _, data = sapi.uploadFile(file_path = "/home/rahul/Downloads/Recruitment_Meeting.mp4",
                              title= "Recruitment Meeting",
                              description= "A sample recruitment meeting file."
                             )
    pprint(data)
    transaction_id = data["data"]["txnId"]

    #step 3 (Upload Compute Request)
    compute_payload = {
        "txnId": transaction_id,
        "enableModels":[
            {
            "modelType":"speech_to_text",
                "modelConfig":{
                    "automatic_punctuation" : True,
                    "custom_vocabulary":["Marsview", "Communication"],
                    "speaker_seperation":{
                        "num_speakers":2
                    },
                    "enableKeywords":True,
                    "enableTopics":False,
                    "enableSuggestedIntents":True
                    }
                }
            ]
        }
    _ , compute_data = sapi.sendComputeRequest(payload=compute_payload)
    pprint(compute_data)

    #step 4 (Long Polling)
    #NOTE: This step is used to wait for the uploaded request to complete
    sapi.long_polling(transaction_id)
    

    #step 5 (Fetch Metadata)
    metadata = sapi.get_metadata(transaction_id)
    pprint(metadata)
    with open("./speechAnalytics Output TID-{}.json".format(transaction_id), 'w') as metaFile:
        metaFile.write(json.dumps(metadata))
