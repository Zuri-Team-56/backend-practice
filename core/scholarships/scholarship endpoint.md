# Welcome to SchoolScout Scholarship APIs Documentation


## LIST ENDPOINT:**
- URL: http://schoolscoutapp.heroku.com/scholarships

This endpoint is responsible for retrieving the list of scholarships and allowing admins to create new scholarships.

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
> * image
> * description
> * snippets
> * school
> * website
> * whatsapp
> * instagram
> * facebook
> * twitter
> * date 
> 
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
>
> * pk
> * name
> * slug 
> * image
> * description
> * snippets
> * school
> * website
> * whatsapp
> * instagram
> * facebook
> * twitter
> * date 

#

## DETAIL ENDPOINT:** 
- URL: http://schoolscoutapp.heroku.com/scholarships/`slug`
* Note: A `slug` is generated automatically if no input is specified

This endpoint is responsible for retrieving the detail page of a scholarships and allowing admins to edit, update or delete the scholarships.
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
> * name
> * slug 
> * image
> * description
> * snippets
> * school
> * website
> * whatsapp
> * instagram
> * facebook
> * twitter
> * date
#