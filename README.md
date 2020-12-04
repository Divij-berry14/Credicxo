# **CREDICXO TASK**



**To create a superuser:**

python manage.py createsuperuser

**Some Important URLs:**

->To create a user:

/users/

Method: POST

Required Fields: username, email, password



-> To receive email with reset password link:

/users/reset_password/

Mehod: GET

Required Fields: email


->To Login/generate JWT:

/jwt/create/

Method: POST

Required Fields: username, password


->To add the user to the specified group:

/addgroup/

Method: POST

Required Fields: group


->To get a list of all students for the teachers:

/students

Method: GET


->To get a ist of all the users for Super-admins:

/allusers

Method: GET