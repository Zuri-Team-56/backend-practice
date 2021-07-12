from django.test import TestCase
from core.faculty.models import Faculty
from core.schools.models import School

from .models import Department


class TestDepartmentModel(TestCase):


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

        self.department = Department.objects.create(
            name = 'department of artificial intelligence',
            slug = 'artificial-intelligence',
            image = 'computer image',
            faculty = self.faculty
        )


    def test_department(self):

        data = self.department
        self.assertTrue(isinstance(data, Department))
        self.assertEqual(str(data), 'department of artificial intelligence')


    
    
   