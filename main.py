import requests
from send_email import send_email

api_key = "116e6baec6f24dc5b3b3781b99d17658"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=" \
      "116e6baec6f24dc5b3b3781b99d17658"


## you make the request to the url here...
request = requests.get(url)

# here you get the actual content from the url website in the form of a dictionary with "json" here...
content = request.json()

## Access the article titles and description....

body = ""
for article in content["articles"]:
      if article['title'] is not None:
            body = body + article["title"] + "\n" + article["description"] + 2*"\n"


body = body.encode("UTF-8")
send_email(message=body)