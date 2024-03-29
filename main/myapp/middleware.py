from django.contrib import messages


class NotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if hasattr(request, '_notifications'):
            for level, message in request._notifications:
                messages.add_message(request, level, message)
            del request._notifications
        return response
