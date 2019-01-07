from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from posts.views import NotificationsListView
from posts.utils import Notifications
from posts.models import Activity

class TestViews(TestCase):

    def setUp(self):
        print('\nsetting up test environment...')
        self.list_url = reverse('posts:list')
        self.post_detail_api = reverse('posts:detail', args=['b1638f970c3ddd528671df76c4dcf13e'])

    def test_json_data_in_db(self):
        print('testing whether the the JSON is being properly loaded...')
        Notifications.load_json_to_db()
        self.assertEquals(23, Activity.objects.all().count())


    def test_activity_list_GET(self):
        print('testing whether activity GET request is working properly...')
        response = self.client.get(self.list_url)
        self.assertContains(response, 'Acme Inc dynamically scales niches worldwide')
        self.assertContains(response, 'How to professionally administrate seamless growth')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/activity_list.html')

    def test_post_notifications_GET(self):
        print('testing whether API endpoint for posts is working...')
        Notifications.load_json_to_db()
        response = self.client.get(self.post_detail_api)
        self.assertEquals(response.data['comment_notification'],
                            'Suoma Narjus commented on your post: "Acme Inc dynamically scales..."')
        response = self.client.get(reverse('posts:detail', 
                            args=['7d78ff348647sdfsdb782cb3027d836single-like']))
        self.assertEquals(response.data['like_notification'],
                            'Eugenio Bertè liked your post: "How to professionally admin..."')
