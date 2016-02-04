import requests
import random
from time import time, sleep
from guerrillamail import *

post_url = 'https://tourbus.redbull.in/html/new_tourbus/new_campus/includes/up_vote.php?rbtb=56b28829e0ee1'
act = 'U0FWRV9WT1RF'
college_id =  151

def get_email():
    session = GuerillaMailSession()
    return session.get_session_state()['email_address']

def upvote():
    f_names = open('names', 'r')
    names = f_names.readlines()
    names = [each.strip().strip(' \xc2\xa0') for each in names]
    names *= 4
    random.shuffle(names)
    data = {}
    for index in xrange(0, 200):
        session = GuerrillaMailSession()
        sender = session.get_session_state()['email_address']
        data['mobile'] = random.randint(9099999999, 9999999999)
        data['act'] = act
        data['college'] = college_id
        data['name'] = names[index]
        data['email'] = sender
        assert(len(names) == 200)
        response = requests.post(post_url, data)
        if response.ok:
            sleep(6)
            redbull_id = session.get_email_list()[0].guid
            target_mail = session.get_email(redbull_id)
            print target_mail.subject
            if (target_mail.subject.find('Red Bull') >= 0):
                mail_body = target_mail.body
                target_link = mail_body.split('"')[1]
                final_response = requests.get(target_link)
                assert final_response.ok
                print "Successfully Voted By: " + sender

if __name__ != "":
    upvote()

