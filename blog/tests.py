from django.test import TestCase
from blog.models import Post


class PostTest(TestCase):

    def setUp(self) -> None:
        self.blog = Post.objects.create(title='django', author='author')

    def test_post_model(self) -> None:
        self.assertTrue(isinstance(self.blog, Post))
        self.assertEqual(str(self.blog), 'django')
