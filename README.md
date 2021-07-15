> # SchoolScout

> ## Table of contents
* [Project Overview](#project-overview)
* [Target Audience](#target-audience)
* [Goals of the project](#goals-of-the-project)
* [Project Features](#project-features)
* [Technologies for Backend](#technologies-for-backend)
* [Backend Team To-do list](#backend-team-to-do-list)
* [Backend Repo Setup](#backend-repo-setup)
* [Setting up the project](#setup)
* [Setting up the PostgreSql Database](#setting-up-the-postgresql-database)
* [Backend Deliverables](#backend-deliverables)
* [Testing](#testing)
* [Status](#status)
* [Contributing to the project](#contributing-to-the-project)
* [PJT-56 Contributors](#pjt-56-contributors)
* [Contact](#contact)
#
>## Project Overview
<p align="justify">
SchoolScout is a web-based application that enables individuals to gather and compare information about various institutions in Nigeria, in order to make informed decisions.
</p> 

![site image](https://drive.google.com/uc?export=view&id=1vIxJbb01AfxhZcPSp-LHF8oU1zh6v9OX)

<p align="justify">
The platform would have a list of schools where users can view information about each school such as the history, programs offered, location, fees, and available scholarship opportunities.
</p> 

<p align="justify">
The site would also provide an option where you can chat with a representative on the site for help.
</p>

#
> ## Target Audience
Prospective undergraduates and postgraduates students who intend to further their studies.
#
> ## Goals of the project
- To create a user-centred website that provides information about institutions.
- Allow users to generate a comparative analysis of Institutions based on key features.
- Provide information about available scholarships.
- Enable Students to view available internship and assistantship opportunities within the institution.
- Provide students with advice on suitable careers.
- Allow prospective students to add favorite schools to their wishlist.

#
> ## Project Features
- School profile page.

- Chat function on the Home page and School profile page.

- Search and filter options.

- Comparative analysis of schools.

- Articles about scholarships and assistantships/internships

- Ability to Comments on articles

- Adverts either from schools or people offering educational - services i.e. JAMB classes. 

- Career advisor.

- School wishlist feature.

- Authentication for users and universities.
</p>


![Example screenshot](https://drive.google.com/uc?export=view&id=1wP4W7J4io1vX6J4RGYhdgM5I_OVDLs3n)


#
> ## Technologies

<p align="justify">
*Note: This project was setup and developed on a system running Windows 10. The stacks used for the project backend include:
</p>


| <b><u>Stack</u></b> | <b><u>Usage</u></b> |
| :---         | :---         |
| **`Python 3.9`** | Programming language. |
| **`Django`** | General backend |
| **`DBML`** | Datamodels |
| **` Django Rest framework`** | APIs. |
| **`Django Rest Auth`** | Authentication. |
| **`PostgreSql`** | Database. |


#
> ## Backend Team To-do list

- Create the data models.

- API Setup.

- Database and repo setup.

- User testing.

- Authentication controls.

- Documentation of the backend process.

- Troubleshoot and debug the project.

- Integrate a live chat feature. 

#
> ## Backend Repo Setup

<p align="justify">
To setup the repo, first fork and clone the Zuriteam Team 56 backend repository to create a copy on the local machine.
</p>

```bash
# git clone git@github.com:pauline-banye/school-scout-be-pjt-56.git
```
<p align="justify">
Change directory to the cloned repo and set the original Zuriteam Team 56 backend repository as the "upstream" and the forked Zuriteam Team 56 backend repository as the "origin" using gitbash.
</p>

```bash
# git remote add upstream git@github.com:zuri-training/school-scout-be-pjt-56.git
```
Edit the readme.md file, add it to git to track changes and create the first commit.

```bash
$ git commit -m "updated readme.md"
[main a4c9702] updated readme.md
1 file changed, 197 insertions(+), 2 deletions(-)
rewrite README.md (100%)
```


Using `git push origin main`, push the commit to the remote origin repository (the forked Zuriteam Team 56 backend repository). 

Finally, initiate a pull request to push the edits to the upstream repository. 

#
> ## Setting up the project
<p align="justify">
The first step requires the download and installation of Python 3.9 and a check to confirm that pip and the necessary dependencies are properly installed.
</p>

<p align="justify">
After the installation of the Python program, setup the project environment with pip and virtualenv in the command prompt, powershell or gitbash terminal. Virtualenv helps to create an isolated Python environment containing all the packages necessary for the project.
</p>

*Note: 
- This project was setup using the gitbash terminal. Some of the commands used do not work with command prompt or powershell.
- If a "pip command not found error" is encountered, download get-pip.py and run `phython get-pip.py` to install it. 

```bash
# pip install virtualenv
```

Navigate to the cloned local school-scout-be-pjt-56 project folder and run `virtualenv folder-name` to create a virtual environment folder.

Activate the environment by running the following command in the gitbash terminal.


```bash
# source folder-name/scripts/activate
```

<p align="justify">
Once the virtual environment is active, the next step is the Django installation. Django is an open source Python web application framework thats helps with the rapid development of secure websites.
</p>

```bash
# (venv) pip install django
```
<p align="justify">
After installing Django, install Django REST framework in the gitbash terminal. The Django REST framework is a flexible toolkit for building Web based APIs. The REST framework was used for the creation of APIs, serialization and the authentication process for this project.
</p>
 
```bash
# (venv) pip install djangorestframework
```
Install all the necessary dependencies for the project. A few of them are listed below.

| <b><u>Modules</u></b> | <b><u>Usage</u></b> |
| :---         | :---         |
| **`django-cors-headers`** | Cross Origin Resource Sharing |
| **`gunicorn`** | WSGI HTTP server |
| **`psycopg2`** | PostgreSQL database adapter |
| **`requests-oauthlib`** | Authentication support for requests |
| **`whitenoise`** | Static files |
| **`chardet`** | Encoding detector |
| **`Markdown`** | Markup language |
| **`django-environ`** | Environment configuration |


An exhaustive list can be found in the requirements.txt file included in this project. The modules can be 'batch installed' using the  `pip install -r requirements.txt` command.


#
> ## Setting up the PostgreSQL Database

<p align="justify">
Django's default database is Sqlite3 and it was used in the local development stage of this project. PostgreSQL is an object relational database with features for the safe storage and scaling of complicated data workloads hence decision to utilize it for the deployment of this project.
</p>

<p align="justify">
The process of setting up PostgreSQL can be done in a couple of ways. One way requires the download and installation of  PostgreSQL interactive installer for Windows. This installer installs the PostgreSQL database server, a terminal program called psql and pgAdmin, which is configured and its values such as the username, password, port are inserted into the django settings.py file.
</p>

The method used for this project however involved the download and installation of the **dj-database-url module** using the command *`pip install dj-database-url`* and the configuration of the settings.py file located in the SchoolScout folder.


<p align="justify">
This module provides a Django database connection dictionary, populated with all the data specified in your URLs. This is especially useful for deployment on sites like Heroku
</p>

To setup, simply import the module using `import dj_database_url` at the top of the document and configure your database as shown below.

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3")),
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
```

#

> ## Backend Deliverables

The backend team on this project were responsible for providing the endpoints of the SchoolScout web API. 

An API or Application Programming Interface Endpoint is the specific location where requests for information are sent. Simply put, it refrences the URL which is used to communicate with the server.

The endpoints for the SchoolScout API include:


| <b><u>Name</u></b> | <b><u>List Endpoints </u></b> | <b><u>Detail Endpoints </u></b> |
| :---         | :---         | :---         |
| `Articles`  | *articles/* | *articles/\<slug>*/
| `Scholarship` | *scholarships/* | *scholarships/\<slug>*/
| `School` |*schools/* | *schools/\<slug>*/
| `Comments`  | *comments/* | *comments/\<pk>*/
| `Courses` | *courses/* | *courses/\<slug>*/
| `Tuition` | *fees/* | *fees/\<slug>*


-  `Registration` */auth/registration/* - User registration
```bash

Media Type: "application/json"

Allowed Methods: "POST"

Content (Request):

# username \<string, unique, required>
# email \<string, unique, required>
# password1 \<string, required>
# password2 \<string, required>
# first_name \<string, required>
# last_name \<string, required> 
 
Note: The password must be atleast 8 characters and not more than 150 characters, can not be entirely numeric and can only contain letters, digits and @/./+/-/_ 
 
Return Type: "application/json"

Content (Response):
key \<string>
```
-  `Sign in`  */auth/login/* - User authentication.

```bash
Media Type: "application/json"

Allowed Methods: "POST"

Content (Request):

# username \<string, optional>
# email \<string, required>
# password \<string, required>
 
Return Type: "application/json"

Content (Response): "key\<string>"
```

**Note**
- CRUD - Create / Retrieve / Update /Destroy
- `pk` - Also known as primary key. Unique identifier for records in the database. 
- `slug` - A short unique label. Usualy used as a valid url for websites.  
- Descriptive lists of some of the individual APIs for the SchoolScout project can be found in a few folders, such as the *articles folder*.
- A complete list of all the APIs for the SchoolScout project can be found in the `endpoints_list.md` file.
#

> ## Testing
Testing codes is important to detect errors and inconsistencies in the code. This is done to ensure the quality of the project before deployment.

There are multiple ways to test your codes and one important tool called `Coverage` is often utilized to analyze the extent to which your code has been tested. 

To test this project, coverage was installed and run using the following command.  

```bash
$ coverage run --omit='*/venv/*' manage.py test 
```
- Note: `--omit='*/venv/*'` is required to exclude all the files relating to the virtual environment.

Coverage generates a report in a folder called **htmlcov**, which provides an index of the files that are tested and a percentage coverage. Any files with less than a *100%* coverage, potentially requires further testing. 

#

> ## Status
This project is in progress. 

#
> ## Contributing to the project

If you find something worth contributing, please fork the repo, make a pull request and add valid and well-reasoned explanations about your changes or comments.

Please note:

- `It should be inviting and clear.`

- `Any additions should be relevant.`

- `It should be easy to contribute to.`

Urls marked **\*** are temporarily unavailable. Don't delete it without confirming that it has permanently expired.

Before adding a pull request, please remember:

```bash
This repository is not meant to contain everything. Only good quality verified information.
```

All **`suggestions`** are welcome!

#
> ## PJT-56 Contributors

This project exists thanks to all the people who contributed to making this a success.

![PJT-56](https://drive.google.com/uc?export=view&id=1xOyycH3R_B0EOkGQHuMMegFwLKSC-sCg)

#
> ## Contacts

Zuri PJT-56 Backend Team- feel free to contact us!

Ikechukwu Ugwuanyi
- Email - ik.ugwuanyi@gmail.com
- GitHub - https://github.com/iconnell

Blaise Mubangizi
- Email - mubangiziblaise@gmail.com
- GitHub - https://github.com/blaise-m

Paul Egboh
- Email - egbohpaul@gmail.com
- GitHub - https://github.com/poshpeck

Hezekiah Samuel
- Email - bassahezekiah@gmail.com
- GitHub - https://github.com/hbassa

Pauline Banye
- Email - paulinebanye@gmail.com
- GitHub - https://github.com/pauline-banye

#
> Readme created by Pauline Banye

