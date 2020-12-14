from django.conf.urls import url

from support_system_app.views import LoginView, CreateTicketView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="login_view"),
    url(r'^new_ticket/$', CreateTicketView.as_view(), name="create_ticket_view"),
]
