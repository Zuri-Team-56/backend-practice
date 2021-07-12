## School Endpoints
...

**I. END POINT:** /schools/new/

This endpoint is responsible for creating new schools.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "POST"
>
> **Required Headers:** *Authentication*
>
> **Content (Request):**
>
> * name
> * slug
> * overview
> * image
> * program
> * entry_requirements
> * faculty_name
> * world_ranking
> * number_of_students
> * tuition_information
> * financial_aid
> * hostel
> * has_hostel
> * location
> * school_news
> * saved_school
> * website
> * courses
> * email
> * password1
> * password2
> * first_name
> * last_name
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * pk
> * slug


**II. END POINT:** /schools/

This endpoint is responsible for reading/viewing all schools.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "GET"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
> * name
> * slug
> * overview
> * image
> * program
> * entry_requirements
> * faculty_name
> * world_ranking
> * number_of_students
> * tuition_information
> * financial_aid
> * hostel
> * has_hostel
> * location
> * school_news
> * saved_school
> * website
> * courses
> * email
> * password1
> * password2
> * first_name
> * last_name
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * pk
> * name
> * slug
> * overview
> * image
> * program
> * entry_requirements
> * faculty_name
> * world_ranking
> * number_of_students
> * tuition_information
> * financial_aid
> * hostel
> * has_hostel
> * location
> * school_news
> * saved_school
> * website
> * courses
> * email
> * password1
> * password2
> * first_name
> * last_name

**III. END POINT:** /schools/update/<slug goes here>/

This endpoint is responsible for updating a school data.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "PUT"
>
> **Required Headers:** *Authentication*
>
> **Content (Request):**
>
> * name
> * slug
> * overview
> * image
> * program
> * entry_requirements
> * faculty_name
> * world_ranking
> * number_of_students
> * tuition_information
> * financial_aid
> * hostel
> * has_hostel
> * location
> * school_news
> * saved_school
> * website
> * courses
> * email
> * password1
> * password2
> * first_name
> * last_name
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * pk
> * name
> * slug
> * overview
> * image
> * program
> * entry_requirements
> * faculty_name
> * world_ranking
> * number_of_students
> * tuition_information
> * financial_aid
> * hostel
> * has_hostel
> * location
> * school_news
> * saved_school
> * website
> * courses
> * email
> * password1
> * password2
> * first_name
> * last_name
> * success/error message

**IV. END POINT:** /schools/delete/<slug goes here>/

This endpoint is responsible for deleting school.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "DELETE"
>
> **Required Headers:** *Authentication*
>
> **Content (Request):**
>
> * name
> * slug
> * overview
> * image
> * program
> * entry_requirements
> * faculty_name
> * world_ranking
> * number_of_students
> * tuition_information
> * financial_aid
> * hostel
> * has_hostel
> * location
> * school_news
> * saved_school
> * website
> * courses
> * email
> * password1
> * password2
> * first_name
> * last_name
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * success/error message


**V. END POINT:** /schools/<slug goes here>/

This endpoint is responsible for reading/viewing/retrieving a schools.
>
> **Media Type:** *"application/json"*
>
> **Allowed Methods:** "GET"
>
> **Required Headers:** *None*
>
> **Content (Request):**
>
> * name
> * slug
> * overview
> * image
> * program
> * entry_requirements
> * faculty_name
> * world_ranking
> * number_of_students
> * tuition_information
> * financial_aid
> * hostel
> * has_hostel
> * location
> * school_news
> * saved_school
> * website
> * courses
> * email
> * password1
> * password2
> * first_name
> * last_name
> 
> **Return Type:** *"application/json"*
>
> **Content (Response):**
> * pk
> * name
> * slug
> * overview
> * image
> * program
> * entry_requirements
> * faculty_name
> * world_ranking
> * number_of_students
> * tuition_information
> * financial_aid
> * hostel
> * has_hostel
> * location
> * school_news
> * saved_school
> * website
> * courses
> * email
> * password1
> * password2
> * first_name
> * last_name

