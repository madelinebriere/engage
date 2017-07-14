import requests
import json
import datetime

from webapp.models import Charity, User, Donation

# def make_charity(date):

#     names = ["kids for kangaroos", "Fidget spinners for humanity", "Blue cross", "Red aid", "Mothers against Mcdonalds"]

#     if (date == '2017-06-14'):
#         charity = Charity.objects.get(name = names[0])
#         return charity
#     elif (date == '2017-05-05'):
#         charity = Charity.objects.get(name = names[1])
#         return charity
#     elif (date == '2017-03-16'):
#         charity = Charity.objects.get(name = names[2])
#         return charity 
#     else:
#         charity = Charity.objects.get(name = names[3])
#         return charity 

headers = {"Accept": "application/json"}
hostName = "172.16.33.2"
port = "8080"
zuora_email = "donations@zuora.com"

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


        z_amount = 1.00 - amount;

        print(pay)
        print(amount)

        names = ["kids for kangaroos", "Fidget spinners for humanity", "Blue cross", "Red aid", "Mothers against Mcdonalds"]
        date = payroll['paymentDate']

        if (date == '2017-06-14'):
            z_charity = Charity.objects.get(name = names[0])
        elif (date == '2017-05-05'):
            z_charity = Charity.objects.get(name = names[1])
        elif (date == '2017-03-16'):
            z_charity = Charity.objects.get(name = names[2])
        else:
            z_charity = Charity.objects.get(name = names[3])

        print(z_charity)

        paymentDate = datetime.datetime.strptime(payroll['paymentDate'] , '%Y-%m-%d').date()
        print(paymentDate)

        # create new Donation Object and Save it
        donation = Donation(user = User.objects.get(email = username), date = paymentDate, amount = amount, charity = z_charity)
        donation.save()

        zuora = Donation(user = User.objects.get(email = zuora_email), date = paymentDate, amount = z_amount, charity = z_charity)
        zuora.save()




    else:
        myResponse.raise_for_status()