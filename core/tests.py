from .models import StudentAccount

class StudentAccountModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        StudentAccount.objects.create(user='John', telephone='a telephone here', mobile='a mobile', gender='sex')
   
    def test_user_content(self):
        studentaccount = StudentAccount.objects.get(id=1)
        expected_object_name = f'{studentaccount.user}'
        self.assertEqual(expected_object_name, 'John')
    
    def test_telephone_content(self):
        studentaccount = StudentAccount.objects.get(id=1)
        expected_object_name = f'{studentaccount.telephone}'
        self.assertEqual(expected_object_name, 'a telephone here')

    def test_mobile_content(self):
        studentaccount = StudentAccount.objects.get(id=1)
        expected_object_name = f'{studentaccount.mobile}'
        self.assertEqual(expected_object_name, 'a mobile')

    def test_gender_content(self):
        studentaccount = StudentAccount.objects.get(id=1)
        expected_object_name = f'{studentaccount.gender}'
        self.assertEqual(expected_object_name, 'sex')