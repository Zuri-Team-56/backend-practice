# Welcome to SchoolScout Faculty APIs Documentation


##  LIST ENDPOINT:
- URL: http://schoolscoutapp.heroku.com/schools/`slug`/faculty

This endpoint is responsible for retrieving the list of faculties and allowing admins to create new faculties.

> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "GET, POST"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
> * name
> * slug \<editable \ auto-generated>
> * school 
> 
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
>
> * pk
> * name
> * slug
> * school 

#

## DETAILS ENDPOINT:
- URL: http://schoolscoutapp.heroku.com/schools/`slug`/faculty/`slug`
* Note: A `slug` is generated automatically if no input is specified

This endpoint is responsible for retrieving the detail page of a faculty and allowing admins to edit, update or delete the faculty.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** " GET, PUT, PATCH, DELETE"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
> 
> * slug 
> 
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
>
> * pk
> * name
> * slug 
> * school 
#