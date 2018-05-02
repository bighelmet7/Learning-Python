from django.conf.urls import url

from views import UserList

urlpatterns = (
    url(r'^users/(?P<name>\w+)$', UserList.as_view(), name=UserList.name),
)
