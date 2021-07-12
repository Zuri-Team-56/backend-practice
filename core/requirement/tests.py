from django.test import TestCase
from core.schools.models import School

from .models import Requirements


class TestRequirementsModel(TestCase):


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

        self.new_requirements = Requirements.objects.create(
            title = 'unilag requirements',
            slug = 'unilag-requirements',
            school = self.new_school,
            program = 'Doctorate Degree',
            description = 'you need your secondary school transcripts'    
        )


    def test_new_requirements(self):

        data = self.new_requirements
        self.assertTrue(isinstance(data, Requirements))
        self.assertEqual(str(data), 'unilag requirements')

    
    