from django.test import TestCase
from django.contrib.auth.models import User
from core.articles.models import Article

# from django.http import response
# from rest_framework.test import APITestCase
# from django.urls import reverse
# from rest_framework import status

from .models import Comment


class TestCommentModel(TestCase):


    def setUp(self):
        self.testuser = User.objects.create_user(username='sarah', password='2345678wert')
        self.testcommenter = User.objects.create_user(username='david', password='790@#ytiD')

        self.new_article = Article.objects.create(
            author = self.testuser,
            title = 'school scout',
            slug = 'school-scout',
            image = 'school image',
            body = 'this is the name of my project',
            snippet = 'name of my project',
            date = '2021-07-11'           
        )

        self.new_comment = Comment.objects.create(
            article = self.new_article,
            commenter = self.testcommenter,
            image = 'commenter image',
            body = 'great job',
            date = '2021-07-11'           
        )


    def test_new_comment(self):

        data = self.new_comment
        self.assertTrue(isinstance(data, Comment))
        self.assertEqual(str(self.new_article), 'school scout')
        self.assertEqual(str(self.testcommenter), 'david')
        self.assertEqual(str(data), 'david')

        

