import requests
from django.conf import settings


headers = {
    "Authorization": settings.API_KEY,
    "orgId": settings.ORGANIZATION_ID,
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
    pass