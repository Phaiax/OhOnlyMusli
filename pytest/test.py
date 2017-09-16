import requests
from requests.auth import HTTPDigestAuth
import urllib

# headers = {"Ocp-Apim-Subscription-Key": apiKey}

def moveRobot(arm,action):
    # http://23.101.77.124/rw/rapid/symbol/data/RAPID/T_ROB_L/Remote/stName?action=set  value="NoClue"

    url = 'http://23.101.77.124/rw'
    auth = HTTPDigestAuth('Default User', 'robotics')

    session = requests.session()

    r0 = session.get(url + '/rapid/symbol/data/RAPID/'+arm+'/Remote/bStart?json=1',
                       auth=auth)
    print(r0)
    print(r0.text)

    r02 = session.get(url + '/rapid/symbol/data/RAPID/'+arm+'/Remote/bRunning?json=1',
                       )
    print(r02)
    print(r02.text)


    payload={'value':'"'+action+'"'}
    headers = {u'content-type': u'application/x-www-form-urlencoded'}
    r1 = session.post(url + '/rapid/symbol/data/RAPID/'+arm+'/Remote/stName?action=set',
                       data=payload,
                       headers=headers)
    print(r1)
    print(r1.text)

    r2 = session.post(url + '/rapid/symbol/data/RAPID/'+arm+'/Remote/bStart?action=set',
                       data={'value':'true'},
                       )
    print(r2)

    return;



moveRobot('T_ROB_R','NoClue')