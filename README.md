![django-logo-negative](https://github.com/user-attachments/assets/050680f3-a2ea-40c3-b563-71e717ff2a64)

<br>

# Django
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Thanks for checking it out.

<br>
<br>

# Installation and organization
```python
pip install django

pip install -r requirements.txt
```

<br>

```python
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DEFAULT_DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        'HOST' : os.environ.get('DEFAULT_DATABASE_HOST', ""),
        'NAME': os.environ.get('DEFAULT_DATABASE_NAME', BASE_DIR / 'db.sqlite3'),
        'PORT': os.environ.get('DEFAULT_DATABASE_PORT', ""),
        'PASSWORD': os.environ.get('DEFAULT_DATABASE_PASSWORD', ""),
        'USER': os.environ.get('DEFAULT_DATABASE_USER', ""),
        
    }
}
```

<br>
<br>

# Goal

- The target of this project is to provide minimalistic django project template that everyone can use, which just works out of the box and has the basic setup you can expand on.

<br>
<br>

# Default usage

- If your project is already in an existing python3 virtualenv first install `django` and `requirements` then running this project.

<br>
<br>

## About
<p>This web project already set up on django and actually is my first real project thst is so close to the reality one!</p>


<br>

## Structures & Recommendations :

1. python
2. django
3. Postgresql
4. Html
5. Css
6. Javascript


- FrontEnd ( `Html`, `Css`, `Js`)
    - Bootstrap, React.js

<br>

- BackEnd ( `Python`, `Django`, `Postgresql`)
    -  Sqlite, Mongodb, Mariadb



<br>

## About Project :

[Django Documentation](https://docs.djangoproject.com/en/5.0/)

[Zalcoders Django Cource](https://zalcoders.com/courses/python-django-bootcamp/)
