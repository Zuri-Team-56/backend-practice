from rest_framework import generics, permissions
from core.advisor.models import CareerQuestion #CareerQuestionAnswer, CareerQuestionOption
from core.advisor.serializers import CareerQuestionSerializer #CareerQuestionAnswerSerializer, CareerQuestionOptionSerializer, 
# from .permissions import IsAuthorOrReadOnly

class CareerQuestionList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CareerQuestion.objects.all()
    serializer_class = CareerQuestionSerializer


class CareerQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (IsAuthorOrReadOnly,) 
    queryset = CareerQuestion.objects.all()
    serializer_class = CareerQuestionSerializer


# class CareerQuestionOptionList(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = CareerQuestionOption.objects.all()
#     serializer_class = CareerQuestionOptionSerializer


# class CareerQuestionOptionDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated,) 
#     # permission_classes = (IsAuthorOrReadOnly,) 
#     queryset = CareerQuestionOption.objects.all()
#     serializer_class = CareerQuestionOptionSerializer


# class CareerQuestionAnswerList(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = CareerQuestionAnswer.objects.all()
#     serializer_class = CareerQuestionSerializer

#     # def perform_create(self, serializer):
#     #     student = self.request.user
#     #     student_id = self.kwargs.get('pk')
#     #     question = CareerQuestionAnswer.objects.get(pk=student_id)
#     #     serializer.save(student=student, qustion=question)


# class CareerQuestionAnswerDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     # permission_classes = (IsAuthorOrReadOnly,) 
#     queryset = CareerQuestion.objects.all()
#     serializer_class = CareerQuestionAnswerSerializer