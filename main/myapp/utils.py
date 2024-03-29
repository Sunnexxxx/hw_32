from django.core.signing import Signer


def add_notification(request, level, message):
    if not hasattr(request, '_notifications'):
        request._notifications = []
    request._notifications.append((level, message))


def sign_data(data):
    signer = Signer()
    signed_data = signer.sign(data)
    return signed_data


def unsign_data(signed_data):
    signer = Signer()
    try:
        data = signer.unsign(signed_data)
        return data
    except:
        return None
