import json
import requests
token = "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"
headers = {
    "Authrorization" : "token {}".format(token),
    "Accept" : "Application/vnd.github.sailor-v-preview+json"

}

#username = input("Enter your github username :")
u = "Prathap1803"
r = "java-maven-soanrqube-jenkins"
#RepoName = input("Enter your Repo name :")
url = "https://api.github.com/repos/{}/{}/issues".format(u,r)

response = requests.request(
    "GET",
    url,
    #json.dump(data),
    headers=headers
)

output = json.loads(response.text)
print(output[0]["title"])
print (output[0]["body"])