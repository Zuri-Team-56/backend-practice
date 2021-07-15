from rest_framework import generics, permissions
from core.advisor.models import CareerQuestion #CareerQuestionAnswer, CareerQuestionOption
from core.advisor.serializers import CareerQuestionSerializer #CareerQuestionAnswerSerializer, CareerQuestionOptionSerializer, 
# from .permissions import IsAuthorOrReadOnly

class CareerQuestionList(generics.ListCreateAPIView):
    queryset = CareerQuestion.objects.all()
    serializer_class = CareerQuestionSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class CareerQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    # permission_classes = (IsAuthorOrReadOnly,) 
    queryset = CareerQuestion.objects.all()
    serializer_class = CareerQuestionSerializer



