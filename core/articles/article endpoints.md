# Welcome to SchoolScout Articles APIs Documentation


## LIST ENDPOINT:
- URL: http://schoolscoutapp.heroku.com/articles

This endpoint is responsible for retrieving the list of articles and allowing admins to create new articles

> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "GET, POST"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
> * author
> * title
> * slug \<editable \ auto-generated>
> * image
> * body
> * date
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
>
> * pk
> * author
> * title
> * slug
> * image
> * body
> * date

#

## DETAIL ENDPOINT:
- URL: http://schoolscoutapp.heroku.com/articles/`slug`
* Note: A `slug` is generated automatically if no input is specified

This endpoint is responsible for retrieving the detail page of articles and allowing admins to edit, update or delete the articles.
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
>
> * pk
> * author
> * title
> * slug
> * image
> * body
> * date