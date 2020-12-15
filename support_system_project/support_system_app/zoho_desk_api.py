import requests
import os
import django
import json
from django.conf import settings


headers = {
    "orgId": settings.ORGANIZATION_ID,
    "Authorization": settings.API_KEY,
    "contentType": "application/json; charset=utf-8"
}

params = "sortBy=dueDate&limit=15"


def create_new_ticket(department=None, category=None, subject=None, description=None, priority=None, name=None, email=None):
    try:
        ticket_data = {
            'category': category,
            'subject': subject,
            'description': description,
            'priority': priority,
            'email': email,
            'departmentId': '7189000000010772',
            'contactId': '7189000003189162'
        }
        # print(json.dumps(ticket_data))
        request = requests.post('https://desk.zoho.in/api/v1/tickets', headers=headers, data=json.dumps(ticket_data))

        if request.status_code == 200:
            print("Request Successful,Response:")
            print(request.content)
            return request.content
        else:
            print("Request not successful,Response code ", request.status_code, " \nResponse : ", request.content)
    except Exception as e:
        print('Exception', e)


def get_all_tickets():
    try:
        request = requests.get('https://desk.zoho.in/api/v1/tickets?include=contacts', headers=headers)

        if request.status_code == 200:
            print("Request Successful,Response:")
            return request.json()
        else:
            print("Request not successful,Response code ", request.status_code, " \nResponse : ", request.content)
    except Exception as e:
        print('Exception', e)
