from django.shortcuts import render, redirect
from .utils import add_notification, sign_data
from django.contrib import messages


def example_view(request):
    add_notification(request, messages.INFO, "Notification")
    data = {'key': 'value'}
    signed_data = sign_data(data)

    return render(request, 'example_template.html', {'signed_data': signed_data})

