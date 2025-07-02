from django.db import models
from common.models import CommonModel

class Comments(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)
    content = models.TextField() 
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    # 대댓글
    # Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)