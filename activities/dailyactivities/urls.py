from django.urls import path
from .views import ( PostListView, PostDetailView, PostCreateView, 
                    PostUpdateView, PostDeleteView, UserPostListView, 
                    interviewquestions,requirementunderstanding, notes, 
                    journey, fitness, dailyevents)
from . import views


urlpatterns = [
    path('',views.home, name='dailyactivities-home' ),
    path('user/<str:username>',UserPostListView.as_view(), name='user_thoughts' ),
    path('journey/',journey.as_view(), name='dailyactivities-journey'),
    path('interviewquestions/',interviewquestions.as_view(), name='dailyactivities-interviewquestions'),
    path('notes/',notes.as_view(), name='dailyactivities-notes'),
    path('requirementunderstanding/',requirementunderstanding.as_view(), name='dailyactivities-requirementunderstanding'),    
    path('fitness/',fitness.as_view(), name='dailyactivities-fitness'),
    path('thoughts/',PostListView.as_view(), name='dailyactivities-thoughts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
	path('post/new/',PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('dailyevents/',dailyevents.as_view(), name='dailyactivities-dailyevents'),
    path('RNN/',views.RNN, name='dailyactivities-RNN'),
]


#path('interviewquestions/',views.interviewquestions, name='dailyactivities-interviewquestions'),
#path('requirementunderstanding/',views.requirementunderstanding, name='dailyactivities-requirementunderstanding'),    
#path('notes/',views.notes, name='dailyactivities-notes'),
#path('journey/',views.journey, name='dailyactivities-journey'),
#path('fitness/',views.fitness, name='dailyactivities-fitness'),