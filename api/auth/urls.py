from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

app_name = 'auth'
urlpatterns = [
  path('obtain_token/', obtain_jwt_token),
  path('refresh_token/', refresh_jwt_token),
]