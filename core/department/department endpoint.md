# Welcome to SchoolScout Department APIs Documentation


## LIST ENDPOINT:
- URL: http://schoolscoutapp.heroku.com/department

This endpoint is responsible for retrieving the list of departments and allowing admins to create new departments.

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
> * faculty 
> 
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
>
> * pk
> * name
> * slug
> * faculty  

#

## DETAIL ENDPOINT: 
- URL: http://schoolscoutapp.heroku.com/department/\<`slug`>
* Note: A `slug` is generated automatically if no input is specified

This endpoint is responsible for retrieving the detail page of a department and allowing admins to edit, update or delete the department.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** " GET, PUT, PATCH, DELETE"
>
> **Required Headers:** *None*
>
> **Content (Request):**
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
> * faculty
#