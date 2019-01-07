import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Activity
from .serializers import NotificationsSerializer
from .utils import Notifications




class NotificationsListView(ListView):
    """
    Get method to fetch a list of activities
    """
    model = Activity

    def get(self, request, *args, **kwargs):
        if not Activity.objects.count():
            Notifications.load_json_to_db()
        else:
            print('JSON already loaded to DB')
        return super(NotificationsListView, self).get(request, *args, **kwargs)


class NotificationDetail(APIView):

    @staticmethod
    def truncate(string, width):
        """ truncates a string with a certain width limit """
        if len(string) > width:
            string = string[:width-3] + '...'
        return string

    @classmethod
    def generate_notification(cls, users, post_title, action_description):
        """ generates notifications based on the number of users and activity"""
        activity_count = len(users)
        if activity_count > 2:
            # more than two people are involved
            notification_message = users.pop() + ', ' + \
                                        users.pop() + ' and ' + \
                                        str(activity_count-2) + \
                                        ' others ' + action_description + 'your post: "' + \
                                        cls.truncate(post_title, 30) + '"'
        elif activity_count == 2 :
            # only two people are involved
            notification_message = users.pop() + ' and ' + \
                                        users.pop() + action_description + 'your post: "' + \
                                        cls.truncate(post_title, 30) + '"'
        elif activity_count == 1:
            # only one person is involved
            notification_message = users.pop() + action_description + 'your post: "' + \
                                        cls.truncate(post_title, 30) + '"'
        else:
            # nobody reacted to this 
            notification_message = ''
        return notification_message

    @classmethod
    def process_notifications(cls, post_id, activity_type):
        """ Processes an activity and eventually creates notifications """
        users_involved = set()
        notification_message = ''
        # fetching data from db based on post_id and activity type
        notification_objects = Activity.objects.filter(
                                                     post_id=post_id, 
                                                     activity_type=activity_type)
        if notification_objects:
            post_title = notification_objects[0].post_title
            for activity in notification_objects:
                # collecting names of all users involved
                users_involved.add(activity.user_name)
            # choosing the right action description
            if activity_type == 'Like':
                action_description = ' liked '
            else:
                action_description = ' commented on '
            notification_message = cls.generate_notification(
                                                                users_involved,
                                                                post_title,
                                                                action_description
                                                                )
        return notification_message
        

    def get(self, request, post_id):
        """ GET request to fetch all notifications for a particular post_id """
        like_notification_message = self.process_notifications(post_id, 'Like')
        comment_notification_message = self.process_notifications(post_id, 'Comment')
        # Both like and comment notifications are ready now
        notification = Notifications(post_id, like_notification_message, comment_notification_message)
        # serializing response object to be passed as JSON
        serializer = NotificationsSerializer(notification)
        return Response(serializer.data)




