import requests
import pprint
import json
import slacker
import time
import slackweb
import schedule
import time

# slack = Slacker("rdqNYFKl1IHh60JJgXXHBuj9")
slack = slackweb.Slack(url="https://hooks.slack.com/services/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")

url = "http://localhost:8000/dates/2019-05-08/changes"
responce = requests.get(url)

print(type(responce))

print(responce.status_code)
responce.json()

x = requests.get(url)

# subject x
# slack.notify(text="a")
x = x.json
print(x)
print(type(x))
'''
def job():
    # slcak.chat.post_message('general')
    # print(x.text)
    slack.notify(text="あ")
    slack.notify(text=x)


schedule.every(0.2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
'''

# pp = pprint.PrettyPrinter(indent=4)
# pp.print()

# parameter = {
#     '' 
# }