from core.reviews.serializers import ReviewSerializer
from rest_framework.generics import ListCreateAPIView
from .models import Review
from rest_framework import permissions
from core.schools.models import School

class ReviewAPIListView(ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Review.objects.filter(sch_id=self.kwargs.get('pk'))
        return queryset

    def perform_create(self, serializer):
        author = self.request.user
        sch_id = self.kwargs.get('pk')
        sch = School.objects.get(pk=sch_id)
        serializer.save(author=author, sch=sch)