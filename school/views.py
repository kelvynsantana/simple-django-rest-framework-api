from rest_framework import viewsets

from school.models import Student
from school.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer