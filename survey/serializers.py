from rest_framework import serializers
from .models import User, Template, TemplateQuestion, TemplateQuestionChoice, TemplateQuestionControlChoice, QuestionType

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'fname', 'lname', 'username', 'password', 'email')

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('id', 'name', 'description', 'active')

class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ('id', 'name', 'description')

class TemplateQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateQuestion
        fields = ('id', 'description', 'question', 'image', 'index', 'template', 'questiontype')

class TemplateQuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateQuestionChoice
        fields = ('id', 'templatequestion', 'index', 'description', 'image')

class TemplateQuestionControlChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateQuestionControlChoice
        fields = ('id', 'templatequestionchoice', 'index', 'description', 'image')