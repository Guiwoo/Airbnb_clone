# Airbnb Clone

Cloning Airbnb with Python, Django, Tailwind and more ...🧡

## pipenv shell

it's kind of npm start

1. django-admin startproject config
2. flake8, black formatter
3. python manage.py migrate//

# Why needs users applications ?

0. django-admin startproject users like this(Group of Function)
1. Needs to handle google or facebook login etc..
2. The application names should be plural
3. The file names which djago made it , you can't change the file name!!!

# Override django user

1. set a model , abstractUser from django.contrib.auth.models
2. python manage.py makemigrations

######## Don't forget have to play django-rule

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

| Models         |
| -------------- |
| RoomsModel ⬇️  |
| CoreModel ⬇️   |
| `models.Model` |

4. realationship

| RoomsModel ⬇️ |
| ------------- | :-------------: |
| CoreModel ⬇️  |                 |
| models.Model  | AbstractItem ⬇️ |
|               |    RoomType     |

| Many to Many && foreignKey |

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

## Gulp with Tailwind

"Just downgrade "
error "Postcss 8 blarblar"
npm uninstall tailwindcss postcss autoprefixer

npm install tailwindcss@npm:@tailwindcss/postcss7-compat @tailwindcss/postcss7-compat postcss@^7 autoprefixer@^9

## Translator

1. django needs to recognize new folder locale add on it
   ex) LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)
2. Go to template {% load i18n %}
3. {% trans "etc..." %}
   ->> Nothing to change yet
4. django-admin makemessages --locale="put language here"
5. Fill up in local > django.po file
   !! Don't add any extra line, should tag on template files first
6. django-admin compilemessages -> it will make .mo file
   ->> Nothing to change still , need to fix session
7. Made a url for the hitting database to change lang ->>base template
8. config.setting.py
   Put this middleware "django.middleware.locale.LocaleMiddleware",
   add LANGUAGE_COOKIE_NAME = "django_language"
9. on view side
   translation.activate(lang) "Get a current Lang"
   response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang) "Change lang as request "

# what if wanna tranlate text which has variable.

@use {% blocktrans %} and the variable outside of blocktrans
ex) {% blocktrans with current_page=page_obj.number %} {{current_page}} {% endblocktrans %}
######!!Eveytime add trans messages need to makemessages and compile

# code translate

In models.py ,gettext*lazy kind of reverse_lazy
tip) gettext_lazy as * "because it looks way better than gettext_lazy"

# Favorit List

get_or_create ==> it will return one object!
Make Template for lists => with templatetag

1. mkdir templatetag, touch **init**.py , what_ever_i_want.py-0
2. register tag "takes_context" ? = call template with dajngo req
   => it will return bunch of things especialy requset!
3. Own one url instead two urls for toggling
4. display lists with new url
5. OneToOne field is so gooood user profiles,user so good
   => user have only one list, configure as onetoone file on list modles

# Conversation

> How it's going ?

    - Go check those user have been chatting
    - Send to Chat Room

1. How to check 2people in the Room ?
   - Use filter chaining (\*`Not good` on database side)
   - Use Q object for filtering ex) Q(age>19) & Q(born>2000)
     - > mutilple chain (`(Q(age>19) & Q(born>2000))` | `Q(nationality=korean') & Q(live!=korea)`)
2. extend User model from model managers

3. Send to Chat room

4. nice variable in for loop on template

   > forloop.first

5. Chat for from
   > Do i need to use django forms ? for only one input ?
   - Not bad to use just plane input and form
     -Have to remember needto put name on input
   - Django forms will help that form way better
