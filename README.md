# <p align="center">django-db-only

This is just wrapper package on top of django framework, which creates django project with only standalone modules included.
  
You can check releases in [Releases](https://github.com/abrorbekuz/django_db_only/releases)<br>
Our community [Telegram Group](https://t.me/django_db_only)

## Howto
**1.** install django-db-only: 

`python setup.py install` or just type<br> `pip install django-db-only`

**2.** create standalone django models project:

```
django_db_only startproject myproject
cd myproject
```

**3.** migrate

```
python manage.py makemigrations <app_name>
python manage.py migrate <app_name>
```

**4.** run application with standalone django models:

```
python query_resolver.py
```


