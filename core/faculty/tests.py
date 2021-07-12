from django.test import TestCase
from core.schools.models import School

from .models import Faculty


class TestFacultyModel(TestCase):


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

        self.faculty = Faculty.objects.create(
            name = 'faculty of computer science',
            slug = 'computer-science',
            image = 'computer image',
            school = self.school
        )


    def test_faculty(self):

        data = self.faculty
        self.assertTrue(isinstance(data, Faculty))
        self.assertEqual(str(data), 'faculty of computer science')


    
    
   