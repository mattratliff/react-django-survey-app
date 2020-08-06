React/DRF Survey App

https://www.valentinog.com/blog/drf/#django-rest-with-react-preparing-the-frontend-app


Leave off: Django REST with React: preparing the frontend app

Running the application:

> python manage.py runserver


Database Design:

                Question Type   
                       |                                  
Template -----< Template Question ------< Template Question Choice -------< Template Question Control Choice
    |               |                       ^                                       ^        
    |               |     |-----------------|                                       |
    |               |     |                                                         |
    |               |     |                                                         |
    |               |     |                                                         |
Survey -------< Survey Response ------< Survey Control Response ---------------------

Template: Template for a survey

Template Question: Question for a template

Template Question Choice:  Choice for a question (Multiplce Choice)

Template Question Control Choice:  Choice for part of a control question

Question Type: Type of question (T/F, MC, Short Answer, Control)

Survey: Instance of a Template

Survey Response: User answer of a question

Survey Control Response:  Answer of a part of a question (if control)

