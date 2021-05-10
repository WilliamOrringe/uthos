from backend.Utils.http_method_handler import handle_methods
from backend.Utils.user_validation import user_login_required


# Auth.

def start(request):
    return handle_methods(
        request,
        POST= 1,
        )


# Comments.
