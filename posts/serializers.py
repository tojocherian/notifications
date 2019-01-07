from rest_framework import serializers

class NotificationsSerializer(serializers.Serializer):

    post_id = serializers.CharField(max_length=200)
    like_notification = serializers.CharField(max_length=400)
    comment_notification = serializers.CharField(max_length=400)
