import requests
import json

from webapp.models import User, Donation

headers = {"Accept": "application/json"}
hostName = "172.16.33.2"
port = "8080"

usernames = User.objects.values_list('email', flat=True)

for username in usernames:


    url = "http://{}:{}/payroll?username={}".format(hostName, port, username)
    myResponse = requests.get(url, headers = headers)

    if (myResponse.ok):

        # parse the json and load into corresponding tables 
        payroll = json.loads(myResponse.content)

        # do some stuff
        pay = payroll['pay']
        amount = round((float(pay) % 1.0), 2)

        print(pay)
        print(amount)

        # create new Donation Object and Save it
        donation = Donation(user = User.objects.get(email = username), date = payroll['paymentDate'], amount = amount)
        donation.save()

    else:
        myResponse.raise_for_status()