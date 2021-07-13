# Welcome to SchoolScout News APIs Documentation


## LIST ENDPOINT:
- URL: http://schoolscoutapp.heroku.com/news

This endpoint is responsible for retrieving the list of school news and allowing admins to create school news.

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
> * category
> * school
> * image
> * info
> * snippet
> * date   
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
>
> * pk
> * title
> * slug
> * category
> * school
> * image
> * info
> * snippet
> * date            

#

## DETAIL ENDPOINT:
- URL: http://schoolscoutapp.heroku.com/news/\<`slug`>
* Note: A `slug` is generated automatically if no input is specified

This endpoint is responsible for retrieving the detail page of school news and allowing admins to edit, update or delete the school news.
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
> * title
> * slug
> * category
> * school
> * image
> * info
> * snippet
> * date