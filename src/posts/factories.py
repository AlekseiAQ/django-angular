import factory
from django.contrib.auth.models import User
from django.utils import timezone

from posts.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    
    username = factory.Sequence(lambda n: 'test_user_%s' % n)
    
    class Meta:
        model = User


class PostFactory(factory.django.DjangoModelFactory):
    
    user = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: 'title_%s' % n)
    content = factory.Sequence(lambda n: 'content_%s' % n)
    publish = factory.LazyFunction(timezone.now)
    
    class Meta:
        model = Post
