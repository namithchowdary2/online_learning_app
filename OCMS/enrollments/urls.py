from django.urls import path
from .views import *
urlpatterns = [
    path('enrollments/', enrollment_list),
    path('enrollments/<int:id>/', enrollment_detail),
    path('progress/', lectureprogress_list),
    path('progress/<int:id>/', lectureprogress_detail),
]