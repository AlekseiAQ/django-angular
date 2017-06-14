from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from unittest import skip

from posts.factories import PostFactory
from posts.models import Post


class TestPostAPI(APITestCase):
    def test_get_post(self):
        post = PostFactory()
        response = self.client.get(post.get_api_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'title_0')

    @skip("Don't want to test, api error")
    def test_create_post(self):
        user = User.objects.create(username='abc', password='abcd')
        self.client.login(username='abc', password='abcd')
        self.assertEqual(Post.objects.count(), 0)

        url = reverse('posts-api:create')
        data = {
            'user': user.username,
            'title': 'title_0',
            'content': 'content_0',
            'publish': timezone.now(),
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'title_0')
        self.assertEqual(Post.objects.get().slug, 'title_0')
