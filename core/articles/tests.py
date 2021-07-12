from django.test import TestCase
# from django.http import response
# from rest_framework.test import APITestCase
from django.urls import reverse
# from rest_framework import status
from django.contrib.auth.models import User
from django.test import Client

from .models import Article


class TestArticleModel(TestCase):

    def setUp(self):

        self.testuser = User.objects.create_user(
            username='sarah', 
            password='2345678wert'
            )

        self.article = Article.objects.create(
            author = self.testuser,
            title = 'school scout',
            slug = 'school-scout',
            image = 'school image',
            body = 'this is the name of my project',
            snippet = 'name of my project',
            date = '2021-07-11'           
        )

    # def test_article_content(self):
    #    article =  self.article.get(id=1),
    #    author = f'{article.author}'
    #    title = f'{article.title}'
    #    slug = f'{article.slug}'
    #    body = f'{article.body}'
    #    date = f'{article.date}'


    def test_new_article(self):

        data = self.article
        self.assertTrue(isinstance(data, Article))
        self.assertEqual(str(data), 'school scout')
        self.assertEqual(str(self.testuser), 'sarah')



# class ArticleTest(APITestCase):

#     def test_view(self):

#         url = reverse('articles:list')
#         response = self.client.get(url, format='json')


#class Test_create_article(TestCase):

    #@classmethod
    #def setUpTestData(cls):

    #    test_user = User.objects.create_user(
    #        username='django', password='2345678wert'
    #    )
    #    test_article = Article.objects.create(
    #        author='django',
    #        title='database',
    #        slug='database',
    #        body='Our API views dont do anything particularly special at the moment, beyond serving json responses',
    #        date='2021-06-02'
    #    )

    #def test_article_content(self):
    #    article =  Article.articleobjects.get(id=1)
    #    author = f'{ar:ticle.author}'
    #    title = f'{article.title}'
    #    slug = f'{article.slug}'
    #    body = f'{article.body}'
    #    date = f'{article.date}'

    #    self.assertEqual(author, 'django')
    #    self.assertEqual(title, 'database')
    #    self.assertEqual(slug, 'database')
    #    self.assertEqual(body, 'Our API views dont do anything particularly special at the moment, beyond serving json responses')
    #    self.assertEqual(date, '2021-06-02')
    #    self.assertEqual(str(article), 'article.title')
    #    self.assertEqual(str(User), 'article.author')



    #    return super().setUpTestData()
