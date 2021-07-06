from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import StudentAccountSerializer, CareerQuestionSerializer, CareerQuestionAnswerSerializer, SavedSchoolSerializer, UserSerializer, SavedCourseSerializer, SavedScholarshipSerializer, CareerQuestionOptionSerializer

from .models import SavedSchool, StudentAccount, CareerQuestion, CareerQuestionAnswer, SavedSchool, SavedCourse, SavedScholarship, CareerQuestionOption

from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentAccountViewSet(viewsets.ModelViewSet):
    queryset = StudentAccount.objects.all().order_by('user')
    serializer_class = StudentAccountSerializer

class CareerQuestionViewSet(viewsets.ModelViewSet):
    queryset = CareerQuestion.objects.all().order_by('question')
    serializer_class = CareerQuestionSerializer

class CareerQuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = CareerQuestionAnswer.objects.all().order_by('question')
    serializer_class = CareerQuestionAnswerSerializer

class CareerQuestionOptionViewSet(viewsets.ModelViewSet):
    queryset = CareerQuestionOption.objects.all().order_by('question')
    serializer_class = CareerQuestionOptionSerializer

class SavedSchoolViewSet(viewsets.ModelViewSet):
    queryset = SavedSchool.objects.all().order_by('school')
    serializer_class = SavedSchoolSerializer

class SavedCourseViewSet(viewsets.ModelViewSet):
    queryset = SavedCourse.objects.all().order_by('course')
    serializer_class = SavedCourseSerializer

class SavedScholarshipViewSet(viewsets.ModelViewSet):
    queryset = SavedScholarship.objects.all().order_by('scholarship')
    serializer_class = SavedScholarshipSerializer

