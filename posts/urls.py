from django.urls import path
from django.views.generic.base import TemplateView
from .views import NotificationsListView, NotificationDetail

app_name = 'posts'

urlpatterns = [
    path('notifications/', NotificationsListView.as_view(), name='list'),
    path('notifications/<slug:post_id>/', NotificationDetail.as_view(), name='detail'),

]


