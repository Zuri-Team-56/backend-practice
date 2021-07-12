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
* [Status](#status)
* [Contributing to the project](#contributing-to-the-project)
* [PJT-56 Contributors](#pjt-56-contributors)
* [Contact](#contact)
#
>## Project Overview
SchoolScout is a web-based application that enables individuals to gather and compare information about various institutions in Nigeria, in order to make informed decisions. 

![site image](https://drive.google.com/uc?export=view&id=16Otrf-DKRwjCBjYJhP587dFUIP3vF1Bu)

The platform would have a list of schools where users can view information about each school such as the history, programs offered, location, fees, and available scholarship opportunities. 

The site would also provide an option where you can chat with a representative on the site for help.

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

![Example screenshot](https://drive.google.com/uc?export=view&id=1wP4W7J4io1vX6J4RGYhdgM5I_OVDLs3n)

#
> ## Technologies
*Note: This project was setup and developed on a system running Windows 10.

The stacks used for the project backend include:

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

To setup the repo, First fork and clone the Zuriteam Team 56 backend repository to create a copy on the local machine. 

```bash
# git clone git@github.com:pauline-banye/school-scout-be-pjt-56.git
```
Change directory to the cloned repo and set the original Zuriteam Team 56 backend repository as the "upstream" and the forked Zuriteam Team 56 backend repository as the "origin" using gitbash.

```bash
# git remote add upstream git@github.com:zuri-training/school-scout-be-pjt-56.git
```
Edit the read.me file and add it to git to track changes. Create the first commit using the `git commit -m "updated readme.md"` command.

```bash
$ git commit -m "updated readme.md"
[main a4c9702] updated readme.md
1 file changed, 197 insertions(+), 2 deletions(-)
rewrite README.md (100%)
```

Using `git push origin main`, push the commit to the remote origin repository (the forked Zuriteam Team 56 backend repository). 

Finally, initiate a pull request to push the edits to the upstream repository. 

#
> ## Setting up the project'

First step requires the download and installation of Python 3.9 and a check to confirm that `pip` and the necessary dependencies are properly installed. 

After the installation of the Python program, setup the project environment with pip and virtualenv in the command prompt, powershell or gitbash terminal. Virtualenv helps to create an isolated Python environment containing all the packages necessary for the project.

*Note: 
- This project was setup using the gitbash terminal.Some of the commands used do not work wih command prompt or powershell.
- If a "pip command not found error" is encountered, download get-pip.py and run `phython get-pip.py` to install it. 

```bash
# pip install virtualenv
```
Navigate to the cloned local school-scout-be-pjt-56 project folder and run `virtualenv venv` to create a virtual environment folder. 

Activate the environment by running the following command in the gitbash terminal.

```bash
source venv/scripts/activate
```

Once the virtual environment is active, the next step is the Django installation. Django is an open source Python web application framework thats helps in the rapid development of secure websites.

```bash
(venv) pip install django
```
After installing Django, install Django REST framework in the gitbash terminal. 

The Django REST framework is a flexible toolkit for building Web based APIs. The REST framework was used for the creation of APIs, serialization and the authentication process for this project.
 
```bash
(venv) pip install djangorestframework
```


To be updated...............

#
> ## Setting up the PostgreSQL Database

Django's default database is Sqlite3 but it is quite limited, hence the decision to utilize PostgreSQL DB for this project.

To set it up and switch the database, download and install PostgreSQL interactive installer for Windows from postgresql.org/download. This installer installs the PostgreSQL database server, a terminal program called psql and pgAdmin.


To be updated...............
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

Pauline Banye
- Email - paulinebanye@gmail.com
- GitHub - https://github.com/pauline-banye

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


#
> Readme created by Pauline Banye

