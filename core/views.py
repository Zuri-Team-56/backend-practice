# from django.db.models.query import QuerySet
# from rest_framework import generics
# from .models import StudentAccount
# from .models import CareerQuestion
# from .serializers import StudentAccountSerializer
# from .serializers import CareerQuestionSerilalizer

# class ListStudentAccount(generics.ListCreateAPIView):
#     queryset = StudentAccount.objects.all()
#     serializer_class = StudentAccountSerializer

# class DetailStudentAccount(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StudentAccount.objects.all()
#     serializer_class = StudentAccountSerializer

# class ListCareerQuestion(generics.ListCreateAPIView):
#     QuerySet = CareerQuestion.objects.all()
#     serializer_class = CareerQuestionSerilalizer

# class DetailCareerQuestion(generics.RetrieveUpdateDestroyAPIView):
#     QuerySet = CareerQuestion.objects.all()
#     serializer_class = CareerQuestionSerilalizer

from rest_framework import viewsets

from .serializers import StudentAccountSerializer, CareerQuestionSerializer, CareerQuestionAnswerSerializer, SavedSchoolSerializer
from .models import SavedSchool, StudentAccount, CareerQuestion, CareerQuestionAnswer, SavedSchool
from rest_framework.permissions import IsAuthenticated

class StudentAccountViewSet(viewsets.ModelViewSet):
    queryset = StudentAccount.objects.all().order_by('user')
    serializer_class = StudentAccountSerializer

# class AuthenticatedStudentAccountViewSet(viewsets.ModelViewSet):
#     serializer_class = StudentAccountSerializer
#     permission_classes = [IsAuthenticated]
#     queryset = StudentAccount.objects.all()


class CareerQuestionViewSet(viewsets.ModelViewSet):
    queryset = CareerQuestion.objects.all().order_by('question')
    serializer_class = CareerQuestionSerializer

class CareerQuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = CareerQuestionAnswer.objects.all().order_by('question')
    serializer_class = CareerQuestionAnswerSerializer

class SavedSchoolViewSet(viewsets.ModelViewSet):
    queryset = SavedSchool.objects.all().order_by('school')
    serializer_class = SavedSchoolSerializer