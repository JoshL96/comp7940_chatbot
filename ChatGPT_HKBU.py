import configparser
import requests
import os
class HKBU_ChatGPT():

    def __init__(self, os_module):
        self.os_module = os_module


    def submit(self,message):   
        conversation = [{"role": "user", "content": message}]

        url = self.os_module.environ['BASICURL'] + "/deployments/" + self.os_module.environ['MODELNAME'] + "/chat/completions/?api-version=" + self.os_module.environ['APIVERSION']
        headers = { 'Content-Type': 'application/json', 'api-key': self.os_module.environ['ACCESS_TOKEN1'] }
        payload = { 'messages': conversation }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return 'Error:', format(response.text)


if __name__ == '__main__':
    ChatGPT_test = HKBU_ChatGPT()

    while True:
        
        user_input = input("Typing anything to ChatGPT:\t")
        response = ChatGPT_test.submit(user_input)
        print(response)

