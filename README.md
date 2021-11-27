# Airbnb Clone

Cloning Airbnb with Python, Django, Tailwind and more ...🧡

## pipenv shell

it's kind of npm start

1. django-admin startproject config
2. flake8, black formatter
3. python manage.py migrate//

# Why needs users applications ?

---

0. django-admin startproject users like this(Group of Function)
1. Needs to handle google or facebook login etc..
2. The application names should be plural
3. The file names which djago made it , you can't change the file name!!!

# Override django user

1. set a model , abstractUser from django.contrib.auth.models
2. python manage.py makemigrations

# Don't forget have to play django-rule

# admin.py

1. I can show specific lists on display
   Ex) list_display = ("username", "gender", "language", "currency", "superhost")
2. Possible to filter
   Ex) list_filter = ("language", "superhost", "currency")
3. Manage by fildsets

## Room Application

1. Make a core apps (for the comman filed)
2. add on setting.py (Installed_Apps)
3. models.Model => coreModel => roomsModle

| RoomsModel ⬇️ |
| ------------- |
| CoreModel ⬇️  |
| ------------  |
| models.Model  |

4. realationship

---

| RoomsModel ⬇️         |
| --------------------- | --------------- |
| CoreModel ⬇️ -------- |
|                       |                 |
| models.Model          | AbstractItem ⬇️ |
|                       | RoomType        |

| Many to Many && foreignKey |
| -------------------------- |

@ondelete=Models.CASCADE if i delete User ? will delete also room
@for the foreignKey

## Reviews Model

@Foreignkey => connected model to model
ex) def **str**(self):
--review.user.username like this

## User.objects

QuerySet Api--
=> QuerySet ? List of objects
something.model_set.all()=>means get all connected by Foreinkey!!
