from rest_framework import serializers

from .models import EntryRequirement


class RequirementSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntryRequirement
        fields = [
            '__all__',
        ]
   