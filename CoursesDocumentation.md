## Courses Endpoints

**I. END POINT:** /courses/new/

This endpoint is responsible for creating new courses.
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
> * course_name
> * slug
> * school_name
> * image
> * course_requirements
> * program
> * name_of_department
> * school_location
> * tuition
> * tution_price
> * address
> * addressState
> * duration
> * durationYear
> * compare


> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * pk
> * slug


**II. END POINT:** /courses/

This endpoint is responsible for reading/viewing all courses.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "GET"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
>
> * pk
> * course_name
> * slug
> * school_name
> * image
> * course_requirements
> * program
> * name_of_department
> * school_location
> * tuition
> * tution_price
> * address
> * addressState
> * duration
> * durationYear
> * compare
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
>
> * pk
> * course_name
> * slug
> * school_name
> * image
> * course_requirements
> * program
> * name_of_department
> * school_location
> * tuition
> * tution_price
> * address
> * addressState
> * duration
> * durationYear
> * compare


**III. END POINT:** /courses/update/<slug goes here>/

This endpoint is responsible for updating a course data.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "PUT"
>
> **Required Headers:** *Authentication*
>
> **Content (Request):**
>
>
> * pk
> * course_name
> * slug
> * school_name
> * image
> * course_requirements
> * program
> * name_of_department
> * school_location
> * tuition
> * tution_price
> * address
> * addressState
> * duration
> * durationYear
> * compare
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
>
> * pk
> * course_name
> * slug
> * school_name
> * image
> * course_requirements
> * program
> * name_of_department
> * school_location
> * tuition
> * tution_price
> * address
> * addressState
> * duration
> * durationYear
> * compare
> * success/error message

**IV. END POINT:** /courses/delete/<slug goes here>/

This endpoint is responsible for deleting a course.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "DELETE"
>
> **Required Headers:** *Authentication*
>
> **Content (Request):**
>
>
> * pk
> * course_name
> * slug
> * school_name
> * image
> * course_requirements
> * program
> * name_of_department
> * school_location
> * tuition
> * tution_price
> * address
> * addressState
> * duration
> * durationYear
> * compare
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * success/error message


**V. END POINT:** /courses/<slug goes here>/

This endpoint is responsible for reading/viewing/retrieving a course.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "GET"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
>
> * pk
> * course_name
> * slug
> * school_name
> * image
> * course_requirements
> * program
> * name_of_department
> * school_location
> * tuition
> * tution_price
> * address
> * addressState
> * duration
> * durationYear
> * compare
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
>
> * pk
> * course_name
> * slug
> * school_name
> * image
> * course_requirements
> * program
> * name_of_department
> * school_location
> * tuition
> * tution_price
> * address
> * addressState
> * duration
> * durationYear
> * compare