import sys
import names
import os
from webapp.models import User

users = []
for i in range(1,100):
    first_name, last_name = names.get_first_name(), names.get_last_name()
    users.append({"name": "{} {}".format(first_name, last_name), "email": "{}.{}@zuora.com".format(first_name, last_name).lower()})

for user in users:
    userEntry = User(name=user["name"], email=user["email"])
    userEntry.save()
