# Welcome to School Scout Backend APIs Documentation

## User Registration and Authentication Endpoints
...

**I. END POINT:** /auth/registration/

This endpoint is responsible for registering new users.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "POST"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
> * username
> * email
> * password1
> * password2
> * first_name
> * last_name
> 
> Note: 
> 1. The password must be atleast 8 characters and not more than 150 characters
> 1. It can not be entirely numeric 
> 1. It can only contain letters, digits and @/./+/-/_ 
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * key

...

**II. END POINT:** /auth/login/

This endpoint is responsible for authenticating a user.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "POST"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
> * username \<optional>
> * email
> * password
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * key

...

**III. END POINT:** /auth/user/

This endpoint is responsible for retrieving and updating user details.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "GET", "PUT", "PATCH"
>
> **Required Headers:** *Authentication*
>
> **Content (Request):**
>
> * username \<optional>
> * first_name \<optional>
> * last_name \<optional>
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * pk
> * username
> * email
> * first_name
> * last_name

...

**IV. END POINT:** /auth/password/change/

This endpoint is responsible for updating/changing a user's password.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "POST"
>
> **Required Headers:** *Authentication*
>
> **Content (Request):**
>
> * new_password1
> * new_password2
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
>
> * success/error message

...

**V. END POINT:** /auth/accounts/password/reset/

This endpoint is responsible for resetting a user's password. It receives a user's email and sends a password reset link to the email
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "POST"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
> * email
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
>
> * success/error message
