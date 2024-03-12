from django.urls import path
from .views import *

urlpatterns = [
    path('', core),
    path('videos', videos, name='videos'),
    path('videos/<int:pk>', VideoDetailView.as_view(), name='video-detail'),
    path('mentors', mentors, name='mentors'),
    path('mentors/<int:pk>', mentor_details, name='mentor-detail'),
    path('category', category, name='category'),
    path('category/<int:pk>', category_details, name='category-detail'),

]
