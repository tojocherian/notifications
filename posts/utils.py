import json
from notifications.settings import STATIC_ROOT
from .models import Activity

class Notifications(object):
    """
    Initialize with post_id, like_notification and comment_notification
    method load_json_to_db loads all the json data to DB
    """
    def __init__(self, post_id, like_notification, comment_notification):
        """ Initialises the instance with these data """
        self.post_id = post_id
        self.like_notification = like_notification
        self.comment_notification = comment_notification


    @staticmethod
    def load_json_to_db():
        """ Takes JSON data in static file and loads it to DB """
        json_data = open(STATIC_ROOT + '/notifications-feed.json')
        # Loading data from JSON file
        notifications_list = json.load(json_data)
        json_data.close()
        for activity in notifications_list:
            # creating a new instance for each acitivity
            if not activity['user']['name']:
                # adding username as its empty
                activity['user']['name'] = 'User'
            activity_type = activity['type']
            if not 'comment' in activity:
                # adding empty values for comments as its a like activity
                activity['comment'] = {'id':'', 'commentText':''} 
            # creating a db entry for each activity
            Activity.objects.create(
                        activity_type=activity_type,
                        post_id=activity['post']['id'],
                        post_title=activity['post']['title'],
                        user_id=activity['user']['id'],
                        user_name=activity['user']['name'],
                        comment_id=activity['comment']['id'],
                        comment=activity['comment']['commentText'],
                        )
