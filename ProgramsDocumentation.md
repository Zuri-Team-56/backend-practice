## Programs Endpoints
**I. END POINT:** /programs/new/

This endpoint is responsible for creating program.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "POST"
>
> **Required Headers:** *Authentication*
>
> **Content (Request):**
>
> * pk
> * title
> * name
> * slug
> * school


> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * pk
> * slug


**II. END POINT:** /programs/

This endpoint is responsible for reading/viewing program.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "GET"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
> * pk
> * title
> * name
> * slug
> * school
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * pk
> * title
> * name
> * slug
> * school


**III. END POINT:** /programs/update/<slug goes here>/

This endpoint is responsible for updating programs.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "PUT"
>
> **Required Headers:** *Authentication*
>
> **Content (Request):**
>
> * pk
> * title
> * name
> * slug
> * school
> 
> **Return Type:** *"application/json"*
>
> * pk
> * title
> * name
> * slug
> * school
> * success/error message

**IV. END POINT:** /programs/delete/<slug goes here>/

This endpoint is responsible for deleting programs.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "DELETE"
>
> **Required Headers:** *Authentication*
>
> **Content (Request):**
>
> * pk
> * title
> * name
> * slug
> * school
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * success/error message


**V. END POINT:** /programs/<slug goes here>/

This endpoint is responsible for reading/viewing/retrieving programs.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "GET"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
> * pk
> * title
> * name
> * slug
> * school
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * pk
> * title
> * name
> * slug
> * school