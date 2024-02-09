import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://dummydotx.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0omDUAZ8q09K93XW2mOFDjtJfstOF0IBg9n_jvTV1pRtPFFgjLsCifiCVDuypPr8lA_ph_KPuAkWFfmk2Q8ux-BpIAfbPQTKETAXjcw0A4viwb4iKTnwyStC8D2dN-Sia-4x046DgHe8Ia2urPLLTMfvNeHUgDjUmR6xa0GLbrQc=A1205DC5"
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
      "id": "10019"
    },
    
    "project": {
      "key": "MD"
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