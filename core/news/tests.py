from django.test import TestCase
from core.schools.models import School

from .models import News


class TestNewsModel(TestCase):


    def setUp(self):

        self.school = School.objects.create(
            name = 'university of lagos',
            slug = 'unilag',
            overview = 'this is a school in lagos',
            program = "Bachelor's Degree",
            image = 'unilag image',
            ranking =  '678',
            website = 'www.unilag.com',
            students = '5000',
            financial_aid = 'no scholarships available',
            hostel = 'different hostels are available',
            has_hostel = 'True',
            location = 'lagos'    
        )

        self.news = News.objects.create(
            title = 'unilag news',
            slug = 'unilag-news',
            category = 'corona virus update',
            school = self.school,
            image = 'news image',
            info = 'make sure you get tested',
            snippet = 'get tested',
            date = '2021-07-11'
        )


    def test_news(self):

        data = self.news
        self.assertTrue(isinstance(data, News))
        self.assertEqual(str(data), 'unilag news')

   