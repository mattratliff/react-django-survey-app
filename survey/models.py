from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

class Template(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

class QuestionType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class TemplateQuestion(models.Model):
    description = models.CharField(max_length=100)
    question = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    index = models.IntegerField()
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    questiontype = models.ForeignKey(QuestionType, on_delete=models.DO_NOTHING)

class TemplateQuestionChoice(models.Model):
    templatequestion = models.ForeignKey(TemplateQuestion, on_delete=models.CASCADE)
    index = models.IntegerField()
    description = models.CharField(max_length=100, default=None, blank=True, null=True)
    image = models.ImageField(upload_to='images/', default=None, blank=True, null=True)

class TemplateQuestionControlChoice(models.Model):
    templatequestionchoice = models.ForeignKey(TemplateQuestionChoice, on_delete=models.CASCADE)
    index = models.IntegerField()
    description = models.CharField(max_length=100, default=None, blank=True, null=True)
    image = models.ImageField(upload_to='images/', default=None, blank=True, null=True)

# Instance of a Template
class Survey(models.Model):
    template = models.ForeignKey(Template, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    createdate = models.DateTimeField(auto_now=True)

# Answer to a question (T/F, Multiple Choice, Shortanswer)
class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    templatequestion = models.ForeignKey(TemplateQuestion, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    answershort = models.CharField(max_length=250, default=None, blank=True, null=True)
    answerbool = models.BooleanField(default=None, blank=True, null=True)
    templatequestionchoice = models.ForeignKey(TemplateQuestionChoice, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)

# Answer to a control question
class SurveyControlResponse(models.Model):
    surveyresponse = models.ForeignKey(SurveyResponse, on_delete=models.CASCADE)
    controlchoice = models.ForeignKey(TemplateQuestionChoice, on_delete=models.DO_NOTHING)