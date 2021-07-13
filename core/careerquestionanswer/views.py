from rest_framework import generics, permissions
from core.careerquestionanswer.models import CareerQuestionAnswer
from core.careerquestionanswer.serializers import CareerQuestionAnswerSerializer


class CareerQuestionAnswerList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CareerQuestionAnswer.objects.all()
    serializer_class = CareerQuestionAnswerSerializer

    # def perform_create(self, serializer):
    #     student = self.request.user
    #     student_id = self.kwargs.get('pk')
    #     question = CareerQuestionAnswer.objects.get(pk=student_id)
    #     serializer.save(student=student, qustion=question)


class CareerQuestionAnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (IsAuthorOrReadOnly,) 
    queryset = CareerQuestionAnswer.objects.all()
    serializer_class = CareerQuestionAnswerSerializer