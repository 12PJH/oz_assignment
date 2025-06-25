from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView, TokenVerifyView)
# users/urls.py
urlpatterns = [
    path('', views.Users.as_view()),
    path("myinfo/", views.MyInfo.as_view()),

    # Authentication
    path("getToken", obtain_auth_token), # DRF token
    path("login/", views.Login.as_view()), # Django Session Login
    path("logout/", views.Logout.as_view()), # Django Session Logout

    # JWT Authentication
    path("login/jwt", views.JWTLogin.as_view()),
    path("login/jwt/info", views.UserDetail_classes.as_view()),


    # Simple JWT Authentication
    path("login/simpleJWT",TokenObtainPairView.as_view() ),
    path("login/simpleJWT/refresh",TokenRefreshView.as_view() ),
    path("login/simpleJWT/verify",TokenVerifyView.as_view() ),

]

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MjAzNDMxMCwiaWF0IjoxNzUwODI0NzEwLCJqdGkiOiI3MDM1ODEyODdkYjU0ZjQ5OWRmMjE3ZDQ0MGE5ZDk0MiIsInVzZXJfaWQiOjF9.oA-avxTdsspDBhr22p9EmbFsP28glvG9YAP_2cNdH1k",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUwODI4MzEwLCJpYXQiOjE3NTA4MjQ3MTAsImp0aSI6ImZlODkwZTM0NDZjZDRlZmViNjBiOTAxZmNhZmNlMjU0IiwidXNlcl9pZCI6MX0.LGO5QPX-adH4xlBdMWcgfQIrmwCc0-l0Iy81xJFAbu4"
# }