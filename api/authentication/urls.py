from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

app_name = 'authentication'
urlpatterns = [
  path('obtain_token/', obtain_jwt_token, name='obtain_jwt_token'),
  path('refresh_token/', refresh_jwt_token, name='refresh_jwt_token'),
]