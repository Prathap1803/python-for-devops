import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://dummydotx.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0g2fMssngEncoxJNWbMT3zwmKf4g9RQc6K7wqwlU0-G3bpk-FiTlBLD7QX9ZZiVCqwcFApXlwBmmnQ4K_BHcmh4aIbWeuaXGq5Js7H7D3q7Yfbsl9PdEfAYj_VjBLJ9uCF2ikxtw3elye-qrjNkzmThaFHYvinK5sqh6-dp3bgfk=E8378ABB"
auth = HTTPBasicAuth("dummy.dotx@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    
  
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Demo first JIRA ticket.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    
    
    
    "issuetype": {
      "id": "10002"
    },
    
    "project": {
      "key": "SCRUM"
    },
    
    "summary": "Main order flow broken",
    
    
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(((response.text) ))