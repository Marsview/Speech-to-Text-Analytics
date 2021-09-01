import requests
import magic
mime = magic.Magic(mime=True)
import time


class SpeechAnalyticsAPI:
    def __init__(self, apiKey, apiToken, userId, baseUrl="https://api.marsview.ai/cb/v1"):
        self.baseUrl = baseUrl
        self.apiKey = apiKey
        self.apiToken = apiToken
        self.userId = userId
        self.accessToken = None
        if self.accessToken is None:
            self.createAccessToken()
    
    def createAccessToken(self):
        #STEP 1
        url = "{baseUrl}/auth/create_access_token".format(baseUrl=self.baseUrl)
        payload = {
          "apiKey": "{}".format(self.apiKey),
          "apiSecret":"{}".format(self.apiToken),
          "userId":"{}".format(self.userId)
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, json=payload)
        self.accessToken = response.json()["data"]["accessToken"]

    class AuthUtils:
        @staticmethod
        def refreshToken(func):
            def wrapper(api,*args,**kwargs):
                print("NAME", func.__name__)
                #func()
                status_code, data =  func(api,*args, **kwargs)
                if status_code in {403, 401}:
                    api.createAccessToken()
                    status_code, data = func(api, *args, **kwargs)
                return status_code, data
            return wrapper

    @AuthUtils.refreshToken
    def uploadFile(self, file_path, title , description):
        #STEP 2
        FILE_PATH = file_path
        TITLE = title
        DESCRIPTION = description

        file_name = FILE_PATH.split("/")[-1]
        url = "{}/conversation/save_file".format(self.baseUrl)
        payload={
            'title': TITLE,
            'description': DESCRIPTION }

        files=[
            ('file',(file_name, open(FILE_PATH,'rb'), mime.from_file(FILE_PATH)))
        ]
        print(files)
        headers = {
            'authorization': "Bearer {}".format(self.accessToken)
        }
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        if response.status_code == 200:
            return response.status_code , response.json()
        else:
            return response.status_code, response.text


    @AuthUtils.refreshToken
    def sendComputeRequest(self, payload):
        url = "{}/conversation/compute".format(self.baseUrl)
        payload=payload
        headers = {'authorization': 'Bearer {}'.format(self.accessToken)}
        response = requests.request("POST", url , headers=headers, json=payload)
        if response.status_code == 200:
            return response.status_code , response.json()
        else:
            return response.status_code, response.text

    @AuthUtils.refreshToken
    def long_polling(self,transaction_id):
        url = "{baseURL}/conversation/get_txn/{tnx}".format(baseURL=self.baseUrl, tnx=transaction_id)
        payload={}
        headers = {
        'authorization': 'Bearer {}'.format(self.accessToken)
        }
        #ALL_DONE = False
        while True:
            response = requests.request("GET", url, headers=headers, data=payload)
            #print(response.text)
            #TODO: Handle token expiry
            model_total_count = len(response.json()["data"]["enableModels"])
            model_active_count = 0
            if model_total_count == 0:
                raise Exception('''
                    No Models requested to process !.
                    Please use https://api.marsview.ai/cb/v1/conversation/compute before Polling fo results
                    ''')
            for model in response.json()["data"]["enableModels"]: 
                    model_processing_status = model["state"]["status"]
                    print("{} : {}".format(model["modelType"],model_processing_status))
                    if model_processing_status in  {"processed","error"}:
                        model_active_count = model_active_count + 1
                    print("Models processing: ({}/{}) Models completed processing".format(model_active_count,model_total_count))
                    if model_active_count == model_total_count:
                        print("All the models have completed processing")
                        return
            time.sleep(60)

    @AuthUtils.refreshToken
    def get_metadata(self, transaction_id):
        metadata_url = "{}/conversation/fetch_metadata/{}".format(self.baseUrl, transaction_id)
        print(metadata_url)
        payload={}
        headers = {
        'authorization': 'Bearer {}'.format(self.accessToken)
        }
        response = requests.request("GET", metadata_url, headers=headers, data=payload)
        #print(response.text)
        if response.status_code == 200:
            return response.status_code , response.json()
        else:
            return response.status_code, response.text



