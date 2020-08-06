from django.urls import path
from . import views

urlpatterns = [
    path('api/user/', views.UserListCreate.as_view() ),
    path('api/template/', views.TemplateListCreate.as_view() ),
    path('api/templatequestion/', views.TemplateQuestionListCreate.as_view() ),
    path('api/templatequestionchoice/', views.TemplateQuestionChoiceListCreate.as_view() ),
    path('api/templatequestioncontrolchoice/', views.TemplateQuestionControlChoiceListCreate.as_view() ),
    path('api/questiontype/', views.QuestionTypeListCreate.as_view() ),
]