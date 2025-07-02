from django.db import models
from common.models import CommonModel

# Create your models here.
# - User: FK => subscriber (내가 구독한 사람)
# - User: FK => subscriber_to (나를 구독한 사람)

# User:Subscription => User(subscriber) =>  subscriber, subscriber, subscriber
# User:Subscription => User(subscribed_to) =>  subscribed_to, subscribed_to, subscribed_to

class Subscription(CommonModel):
    subscriber = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscribers')