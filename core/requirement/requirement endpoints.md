# Welcome to SchoolScout Requirement APIs Documentation


## LIST ENDPOINT:
- URL: http://schoolscoutapp.heroku.com/requirement

This endpoint is responsible for retrieving the list of schoolrequirement and allowing admins to create new school requirements.

> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "GET, POST"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
> * title
> * slug \<editable \ auto-generated>
> * school
> * program
> * description
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
>
> * pk
> * title
> * slug 
> * school
> * program
> * description     

#

## DETAIL ENDPOINT:
- URL: http://schoolscoutapp.heroku.com/requirement/\<`slug`>
* Note: A `slug` is generated automatically if no input is specified

This endpoint is responsible for retrieving the detail page of school requirement and allowing admins to edit, update or delete the school requirement.
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
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * pk
> * pk
> * title
> * slug 
> * school
> * program
> * description     