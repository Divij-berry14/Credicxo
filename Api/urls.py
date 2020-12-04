from django.urls import path, include

urlpatterns = [
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt'))
]




"""
Some important djoser urls
To create a user:                           /users/
To update the authenticated user:           /users/me/
To set a new password for existing users:   /users/set_password/
To receive email with reset password link:  /users/reset_password/
To Login/generate JWT:                      /jwt/create/
To refresh the JWT:                         /jwt/refresh/
To Verify the JWT:                          /jwt/verify/
"""