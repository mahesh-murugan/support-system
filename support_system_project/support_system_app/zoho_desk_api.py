import requests
import os
import django
from django.conf import settings


headers = {
    "orgId": settings.ORGANIZATION_ID,
    "Authorization": settings.API_KEY,
    "contentType": "application/json; charset=utf-8"
}

params = "sortBy=dueDate&limit=15"


def create_new_ticket():
    request = requests.get('https://desk.zoho.com/api/v1/tickets?' + params, headers=headers)

    if request.status_code == 200:
        print("Request Successful,Response:")
        print(request.content)
    else:
        print("Request not successful,Response code ", request.status_code, " \nResponse : ", request.content)


def get_all_tickets():
    try:
        print(headers)
        request = requests.get('https://desk.zoho.com/api/v1/tickets' , headers=headers)

        if request.status_code == 200:
            print("Request Successful,Response:")
            print(request.content)
        else:
            print("Request not successful,Response code ", request.status_code, " \nResponse : ", request.content)
    except Exception as e:
        print('Exception', e)
