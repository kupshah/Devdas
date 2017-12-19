import os
#from bottle import route, run, post, request, app
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import random

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    # member_ids = ['236636135', '236636136', '236636137', '236636138', '236636139', '236636140', '236636141',
    #               '236636142', '236636143', '236636144', '236636145', '236636146', '236636147', '236636148',
    #               '236636149', '236636150', '236636151', '236636152', '236636153', '236636154', '236636155',
    #               '236636156', '277319712', '277319713', '277319714', '277319715', '277319716', '277319717',
    #               '277319718', '277319719']

    members = ['Suhas Narendrula', 'Anusha Bhaskarla', 'Sachin Seetharam', 'Karthik Eluri', 'Jagdeep Singh Bhinder', 'Keshav Muralitharan', 'Medha Lingawar', 'Kunaal Shah', 'Minal Patel', 'Jasmine Patel', 'Nivi the Mafi', 'Rahee Patel', 'Tulsi Patel', 'Shreya Kaza', 'Devika Davda', 'Neehar Sachdeva', 'Sid Chawla', 'Penny Bola', 'Shakshi Sambwani', 'Kiran Rajan', 'Amani Karim', 'Gazal Kathuria', 'Mahak Jain', 'Varun Alse', 'Nishant Medicharla', 'Venu Bangla', 'Vedant Chawla', 'Paloma Bhugra', 'Tesh Patel', 'Dhvani Shah']


    # We don't want to reply to ourselves!
    #if data['name'] != 'Flappy-ISA':
    if "devdas" in data["text"].lower() and data['name'] != "Devdas":
        msg = '{}, you sent "{}".'.format(data['name'], data['text'])
        send_message("Hello " + data["name"] +"!")


    elif "@everyone" in data["text"]:
        mention_everyone()

    elif data["text"] == "!random_person":
        pick_random_person(members)

    return "ok", 200


def send_message(msg):
    url  = 'https://api.groupme.com/v3/bots/post'

    data = {
          'bot_id': os.getenv('GROUPME_BOT_ID'),
          'text': msg,
         }
    req = Request(url, urlencode(data).encode())
    json = urlopen(req).read().decode()


def mention_everyone(members):
    url = 'https://api.groupme.com/v3/bots/post'
    vkid = ["2248954", "25561506"]
    vk = {"Vasu Sheel", "Kunaal Shah"}

    string = ""
    for item in vk:
        string +="@" +item + " "

    data = {
        'bot_id': os.getenv('GROUPME_BOT_ID'),
        'attatchments': {
            'loci': [[0,11], [12,11]],
            'type':'mentions',
            'user_ids': vkid,
        },
        'text' : string
    }
    req = Request(url, urlencode(data).encode())
    json = urlopen(req).read().decode()

def pick_random_person(members):

    choice = random.choice(members)
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': os.getenv('GROUPME_BOT_ID'),
        'text': "Randomly picked " + choice,
    }
    req = Request(url, urlencode(data).encode())
    json = urlopen(req).read().decode()



#run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
