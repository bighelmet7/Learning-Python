from django.conf.urls import url

from views.user import UserList

urlpatterns = (
    url(r'^users/$', UserList.as_view(), name=UserList.name),
)
