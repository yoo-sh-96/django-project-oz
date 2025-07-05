from rest_framework.test import APITestCase
from users.models import User
from videos.models import Video
from django.urls import reverse # url -> name을 기반으로 url 값을 불러온다
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

class VideoAPITestCase(APITestCase):
    # 테스트코드 케이스가 실행 되기 전 가장 먼저 실행되는 함수
    # 테스트 전 데이터를 생성하는 역핳
    # (1) 유저 생성 및 로그인 -> (2) 비디오 생성
    def setUp(self):
        # 회원가입
        self.user = User.objects.create_user(
            email='seunghyeop@gmail.com',
            password='1q2w3e4r'
        )

        #로그인
        self.client.login(email='seunghyeop@gmail.com', password='1q2w3e4r')

        self.video = Video.objects.create(
            title='First video title',
            link='http://www.test.com',
            user=self.user
        )

    # api/v1/videos [GET], [POST]
    def test_video_list_get(self):
        url = reverse('video-list') # urls.py에 지정한 name울 뷸러옴
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.data) > 0)

        for video in res.data:
            self.assertIn('title', video)

    def test_video_list_post(self):
        url = reverse('video-list')


        data = {
            'title': 'My test video title',
            'link': 'http://www.test.com',
            'category': 'Development',
            'thumbnail':'http://www.test.com',
            'video_file': SimpleUploadedFile('test.mp4', b'file_content', 'video/mp4'),
            'user': self.user.pk
        }

        res = self.client.post(url, data) # VideoList [POST]

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'My test video title')

    # 특정 비디오 조회
    def test_video_detail_get(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    # 특정 비디오 업데이트
    def test_video_detail_put(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})

        data = {
            'title': 'Updated Video Title',
            'link': 'http://www.test.com',
            'category': 'Development',
            'thumbnail':'http://www.test.com',
            'video_file': SimpleUploadedFile('test.mp4', b'file_content', 'video/mp4'),
            'user': self.user.pk
        }

        res = self.client.put(url, data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['title'], 'Updated Video Title')

    # 특정 비디오 삭제
    def test_video_detail_delete(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
        res = self.client.delete(url)

        self.assertEqual(res.status_code, 204)

        res = self.client.get(url)
        self.assertEqual(res.status_code, 404)



