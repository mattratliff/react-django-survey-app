from .models import User, Template, TemplateQuestion, QuestionType
from .serializers import UserSerializer, TemplateSerializer, TemplateQuestionSerializer, QuestionTypeSerializer
from rest_framework import generics

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TemplateListCreate(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

class TemplateQuestionListCreate(generics.ListCreateAPIView):
    queryset = TemplateQuestion.objects.all()
    serializer_class = TemplateQuestionSerializer

class QuestionTypeListCreate(generics.ListCreateAPIView):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer