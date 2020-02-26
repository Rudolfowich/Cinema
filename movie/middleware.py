import datetime
from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin


class TimeOutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        shouldlogout = False
        if not request.user.is_superuser and request.user.is_authenticated:
            if 'last_request' in request.session:
                time_has_passed = datetime.datetime.now().timestamp() - request.session['last_request']
                if time_has_passed > 60 * 5:
                    del request.session['last_request']
                    shouldlogout = True
            else:
                request.session['last_request'] = datetime.datetime.now().timestamp()
            if shouldlogout:
                logout(request)
        return self.get_response(request)
