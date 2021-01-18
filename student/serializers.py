from rest_framework import serializers
from .models import *

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ['id', 'name', 'age', 'roll_no', 'class_name', 'created_at','updated_at']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.class_name = validated_data.get('class_name', instance.class_name)
        instance.save()
        return instance
