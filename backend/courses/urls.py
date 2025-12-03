from django.urls import path
from .views import CourseQuestionsView, SaveQuestionsView
from .views import SaveQuizResultView
from .views import SaveQuizToProgressView

from .views import (
    GetProgressView,
    UpdateProgressView,
     CompleteModuleView, 
    
)


    

urlpatterns = [
    path("api/courses/<int:course_id>/questions/", CourseQuestionsView.as_view(), name="course-questions"),
    path("api/courses/<int:course_id>/questions/save/", SaveQuestionsView.as_view(), name="save-questions"),
     path("api/courses/<int:course_id>/save-result/", SaveQuizResultView.as_view()),
     path("api/progress/<int:course_id>/", GetProgressView.as_view()),
path("api/progress/<int:course_id>/module/<int:module_index>/complete/", CompleteModuleView.as_view()),
path("api/progress/<int:course_id>/quiz/save/", SaveQuizToProgressView.as_view()),
    path("api/progress/<int:course_id>/update/", UpdateProgressView.as_view()),


]
