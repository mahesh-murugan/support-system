from django.conf.urls import url

from support_system_app.views import LoginView, CreateTicketView, ManageTicketView, manage_tickets_ajax

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="login_view"),
    url(r'^new_ticket/$', CreateTicketView.as_view(), name="create_ticket_view"),
    url(r'^manage_tickets/$', ManageTicketView.as_view(), name="manage_ticket_view"),
    url(r'^manage_tickets/ajax/$', manage_tickets_ajax, name="manage_ticket_ajax_view"),
]
