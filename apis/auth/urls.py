from django.urls import path

from apis.auth.views import LoginSignupView

urlpatterns = [
    path('login/', LoginSignupView.as_view(), name='login-signup'),
]
