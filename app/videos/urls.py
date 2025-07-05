from django.urls import path
from .views import VideoDetail, VideoList

#api/v1/video - VideoList
#api/v1/video/{video_id} - VideoDetail
urlpatterns = [
    path('', VideoList.as_view(), name='video-list'),
    path('<int:pk>', VideoDetail.as_view(), name='video-detail')
]