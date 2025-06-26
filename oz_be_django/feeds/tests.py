from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Feed
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class FeedAPITestcase(APITestCase):
    # setup 메서드는 각각의 테스트 메서드가 실행되기 전에 호출된다.
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="password")
        refresh = RefreshToken.for_user(self.user)
        self.token = refresh.access_token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.feed1 = Feed.objects.create(user = self.user, title = "Test Feed1", content = "Test Feed")
        self.feed2 = Feed.objects.create(user = self.user, title="Test Feed2", content="Test Feed")

    def test_get_all_feeds(self):
        url = reverse("all_feeds")
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)  # 2개의 피드가 반환되어야 합니다.

    def test_get_feed_detail(self):
        url = reverse('feed_detail', kwargs={'feed_id': 1})  # 'user_feeds'는 url 패턴 이름입니다.
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'], self.feed1.title)
        self.assertEqual(res.data['content'], self.feed1.content)
        # self.assertEqual(len(response.data), 2)  # 해당 유저의 2개 피드가 반환되어야 합니다.


    def create_feed(self):
        self.client.login(username="test_user", password="password")

        url = reverse("all_feeds")
        data = {'title': 'New Feed', 'content': 'This is a new feed.'}
        res = self.client.post(url, data)
        print('res', Feed.objects.all())

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feed.objects.count(), 3)  # 게시글 수가 3개여야 합니다.
        self.assertEqual(Feed.objects.latest('id').content, 'New Feed Content')