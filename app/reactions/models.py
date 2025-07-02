from django.db import models
from common.models import CommonModel
# Create your models here.

# - User: FK
# - Video: FK
# - reaction(like, dislike, cancel) => 실제 youtube rest api


class Reaction(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = ( # 상수변수이기에 대문자로 표시
        (LIKE, 'Like'),
        (DISLIKE, 'DisLike'),
        (NO_REACTION, 'No Reaction')
    )

    # LIKE(1), DISLIKE(-1), NO_REACTION(0)
    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION
    )