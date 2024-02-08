# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://dummydotx.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0g2fMssngEncoxJNWbMT3zwmKf4g9RQc6K7wqwlU0-G3bpk-FiTlBLD7QX9ZZiVCqwcFApXlwBmmnQ4K_BHcmh4aIbWeuaXGq5Js7H7D3q7Yfbsl9PdEfAYj_VjBLJ9uCF2ikxtw3elye-qrjNkzmThaFHYvinK5sqh6-dp3bgfk=E8378ABB"
auth = HTTPBasicAuth("dummy.dotx@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
#print (type(output))
for i in range (len(output)):
    print(output[i]["name"])