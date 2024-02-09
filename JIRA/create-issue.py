import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://dummydotx.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0DnVsEpZmlqx5S2zgOJsax1wcX1qyOGwoFt5GsrYIiAtSC6EJHWjjbfMyAOM6CMfh6_a5LgW3wf4uPlEDeY_Iel9Tojxyv5hznJV2COjo0HOOht3b_KoKIQG7N8usXSXiYIdHreIJa-9AlUcJmKfrjGvIWnLx3nFJdAneUK5MF4Y=5981BF7E"
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