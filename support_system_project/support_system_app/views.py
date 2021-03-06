from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.http.response import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
import json

from support_system_app.forms import LoginForm, CreateTicketForm
from support_system_app.zoho_desk_api import create_new_ticket, get_all_tickets


class LoginView(FormView):
    template_name = "support_system_app/login/login.html"
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # logout if user already logged in
            print("logging out current user")
            logout(request)
        return render(request, self.template_name, context=self.get_context_data())

    def form_valid(self, form):
        if self.request.method == "POST":
            form = self.form_class(self.request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user_obj = User.objects.filter(email=email).first()
                if user_obj is not None:
                    user = authenticate(username=user_obj.username, password=password)
                    if user is not None:
                        login(self.request, user=user)  # save user to session to access inner pages
                        return HttpResponseRedirect(reverse('create_ticket_view'))
            context = self.get_context_data()
            context['error'] = 'Email or Password invalid !'
            return render(self.request, self.template_name, context=context)
        return super().form_valid(form)


class CreateTicketView(LoginRequiredMixin, FormView):
    template_name = "support_system_app/ticket/create_ticket.html"
    form_class = CreateTicketForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = self.form_class(initial={'name': self.request.user.username, 'email': self.request.user.email})
        return context

    def form_valid(self, form):
        if self.request.method == "POST":
            form = self.form_class(self.request.POST)
            if form.is_valid():
                department = form.cleaned_data['department']
                category = form.cleaned_data['category']
                subject = form.cleaned_data['subject']
                description = form.cleaned_data['description']
                priority = form.cleaned_data['priority']
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']

                result = create_new_ticket(department, category, subject, description, priority, name, email)
                if result is not None:
                    messages.success(self.request, 'Ticket Created Successfully')
                else:
                    messages.warning(self.request, 'Ticket Not Created.')
                return HttpResponseRedirect(reverse('manage_ticket_view'))
        return super().form_valid(form)


class ManageTicketView(LoginRequiredMixin, TemplateView):
    template_name = "support_system_app/ticket/ticket_list.html"


def manage_tickets_ajax(request):
    data = {'ticket_list': []}
    result = get_all_tickets()
    if result is not None and 'data' in result:
        for datas in result['data']:
            if datas['email'] == request.user.email:
                data['ticket_list'].append({
                    'subject': datas['subject'] if 'subject' in datas else '',
                    'description': datas['description'] if 'description' in datas else '',
                    'priority': datas['priority'] if 'priority' in datas else '',
                    'ticket_status': datas['status'] if 'status' in datas else '',
                    'ticket_number': datas['ticketNumber'] if 'ticketNumber' in datas else '',
                })
    return JsonResponse(data=data)

