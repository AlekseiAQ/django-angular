from django.test import TestCase

from posts.factories import PostFactory
from posts.models import Post


class TestPost(TestCase):

    def test_get_api_url(self):
        post0 = PostFactory()
        post1 = PostFactory()
        self.assertEqual(post0.get_api_url(), '/api/posts/' + post0.slug + '/')
        self.assertEqual(post1.get_api_url(), '/api/posts/' + post1.slug + '/')
