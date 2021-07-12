from django.test import TestCase
from core.schools.models import School

from .models import Scholarship


class TestScholarshipModel(TestCase):


    def setUp(self):

        self.new_school = School.objects.create(
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

        self.new_scholarship = Scholarship.objects.create(
            name = 'unilag scholarship',
            description = 'once in a lifetime',
            slug = 'lifetime',
            image = 'scholarship image',
            requirements = 'automatically awarded',
            snippets = 'automatic consideration',
            school = self.new_school,
            date = '2021-07-11',
            saved = 'False' 
        )


    def test_new_scholarship(self):

        data = self.new_scholarship
        self.assertTrue(isinstance(data, Scholarship))
        self.assertEqual(str(data), 'unilag scholarship')

    
    