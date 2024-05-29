from requests.auth import HTTPBasicAuth
import json
app = Flask(__name__)

@app.route("/createJira",methods=['POST'])
def createJira():

    url = "https://dummy-dot5.atlassian.net/rest/api/3/issue"
    API_TOKEN = "ATATT3xFfGF0tlPrqYy2tyhceKJttXJ25zEMtF7Un3n0c7zDbfonkzsnaivw9dFb8o4hEjvLDJHaWbV2HdoBsOQBq-WFUpZMHjjCrWcakEpiFphnnqf0WFpUKkN3Z284vqYzfz5WYN8Xxpa08AHD3Bt2ZQMzTEm9F2kvJp_vVl09pRJXBPL_cs4=1C3B1049"
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
    data1 = json.loads(request.data)

    if (data1["comment"]["body"])== "/jira" :
        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )
        #print (request.headers['X-GitHub-Event'])
        #print (type(data1))
        return((response.text))
    else:
        print ("Please enter valid comments  : ")
app.run('0.0.0.0')
