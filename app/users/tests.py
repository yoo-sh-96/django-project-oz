from django.test import TestCase
from django.contrib.auth import get_user_model

# TDD : Test Drvien Development (테스트 주도 개발)
class UserTestCase(TestCase):

    # 일반유저 생성 테스트 함수
    def test_create_user(self):
        email = 'seunghyeop@gamil.com'
        password = '1q2w3e4r'

        user = get_user_model().objects.create_user(email=email, password=password)

        # 유저가 정상적으로 잘 만들어졌는지?
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password)) #self.assertEqual(user.check_password(password), True)
        self.assertFalse(user.is_superuser) #self.assertEqual(user.is_superuser, False)
    
    # 슈퍼유저 생성 테스트 함수
    def test_create_superuser(self):
        email = 'you_super@gmail.com'
        password = '1q2w3e4r'

        user = get_user_model().objects.create_superuser(
            email = email,
            password=password
        )

        # 슈펴유저
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

        # docker-compose run --rm app sh -c 'python manage.py test users'
        # docker-compose run --rm app sh -c 'python manage.py migrate'   
        # docker-compose run --rm app sh -c 'python manage.py makemigrations' 