**CREDICXO TASK**


**To create a superuser:**
python manage.py createsuperuser

**Some Important URLs:**

1. To create a user:

/users/
Method: POST
Required Fields: username, email, password


2. To receive email with reset password link:
/users/reset_password/
Method: GET
Required Fields: email

3. To Login/generate JWT:

/jwt/create/
Method: POST
Required Fields: username, password

4.To add the user to the specified group:

/addgroup/
Method: POST
Required Fields: group

5.To get a list of all students for the teachers:

/students
Method: GET

6.To get a ist of all the users for Super-admins:

/allusers
Method: GET