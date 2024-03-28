try:
    from django.conf.urls import url, include
except ImportError:
    from django.urls import re_path as url, include

urlpatterns = [
    url(r'^', include('notify.urls', namespace='notifications')),
]
