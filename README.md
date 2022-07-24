# <p align="center">django-db-only

This is just wrapper package on top of django framework, which creates django project with only standalone modules included.
  
You can check releses in [Releases](https://github.com/abrorbekuz/django_db_only/releases)

## Howto
**1.** install django-models-standalone: 

`python setup.py install`

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


