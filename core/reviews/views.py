from core.reviews.serializers import ReviewSerializer
from rest_framework.generics import ListCreateAPIView
from .models import Review
# from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.schools.models import School

class ReviewAPIListView(ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()    
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

    # def get_queryset(self):
    #     # queryset = Review.objects.filter(sch_id=self.kwargs.get('pk'))
    #     queryset = Review.objects.filter(sch_id=self.kwargs.get('slug'))
    #     return queryset

    # def perform_create(self, serializer):
    #     author = self.request.user
    #     # sch_id = self.kwargs.get('pk')
    #     sch_id = self.kwargs.get('slug')
    #     # sch = School.objects.get(pk=sch_id)
    #     sch = School.objects.get(slug=sch_id)
    #     serializer.save(author=author, sch=sch)

    
