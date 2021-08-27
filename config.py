#[Credentials]
BASE_URL = "https://api.marsview.ai/cb/v1"
API_KEY = ""
API_TOKEN = ""
USER_ID = ""

#[Configs]
'''
Given below are a couple of configuration examples based on different requirements
'''

# Speech To text with Keywords and Intents enabled 
SPEECH_TO_TEXT_CONFIG = {
        "txnId": "{txnId}",
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


ALL_AUDIO_MODELS_CONFIG = {
    "txnId": "{txnId}",
    "enableModels":[
        {
        "modelType":"speech_to_text",
        "modelConfig":{
            "automatic_punctuation" : True,
            "custom_vocabulary":["Marsview", "Communication"],
            "speaker_seperation":{
                "num_speakers":2
            },
            "enableKeywords":True
            }
        },
        {"modelType":"emotion_analysis"},
        {"modelType":"sentiment_analysis"},
        {"modelType":"speech_type_analysis"},
        {
            "modelType":"action_items",
            "modelConfig":{"priority": 1} 
        },
        {
            "modelType":"question_response",
            "modelConfig":{"quality" : 1}
        },
        {"modelType":"extractive_summary"},
        {"modelType":"meeting_topics"},
    ]
}

ALL_MODELS_CONFIG = {
    "txnId": "{txnId}",
    "enableModels":[
        {
        "modelType":"speech_to_text",
        "modelConfig":{
            "automatic_punctuation" : True,
            "custom_vocabulary":["Marsview", "Communication"],
            "speaker_seperation":{
                "num_speakers":2
            },
            "enableKeywords":True
            }
        },
        {"modelType":"emotion_analysis"},
        {"modelType":"sentiment_analysis"},
        {"modelType":"speech_type_analysis"},
        {
            "modelType":"action_items",
            "modelConfig":{"priority": 1} 
        },
        {
            "modelType":"question_response",
            "modelConfig":{"quality" : 1}
        },
        {"modelType":"extractive_summary"},
        {"modelType":"meeting_topics"},
        {
            "modelType":"screengrabs",
            "modelConfig":{"ocr":{"enable":True}}
        },
        {"modelType":"screen_activity"}

    ]
}


#[Tests]
assert API_KEY   != "", "Please add API Key"
assert API_TOKEN != "", "Please add API Token"
assert USER_ID   != "", "Please add API User ID"
