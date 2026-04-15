from django.utils.deprecation import MiddlewareMixin


class DisableCSRFMiddleware(MiddlewareMixin):
    """Отключает CSRF проверку для всех запросов"""

    def process_request(self, request):
        # Отключаем проверку CSRF
        setattr(request, '_dont_enforce_csrf_checks', True)