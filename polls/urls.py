from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('polls', views.PollViewSet, basename='polls')


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("polls/", views.PollList.as_view(), name="poll_list"),
    path("polls/<int:pk>/", views.PollDetail.as_view(), name="poll_detail"),
    path("polls/<int:pk>/choices/", views.ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", views.CreateVote.as_view(), name="create_vote"),
    path("users/", views.UserCreate.as_view(), name="user_create"),
]


urlpatterns += router.urls
