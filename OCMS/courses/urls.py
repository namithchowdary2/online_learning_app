from django.urls import path
from .views import *
urlpatterns = [
    path('categories/', category_list),
    path('categories/<int:id>/', category_detail),
    path('courses/', course_list),
    path('courses/<int:id>/', course_detail),
    path('modules/', module_list),
    path('modules/<int:id>/', module_detail),
    path('lectures/', lecture_list),
    path('lectures/<int:id>/', lecture_detail),
]