# Estudio de Django

Para inciar el visor de markdown se debe utilizar Ctrl+Shift+V

Para iniciar django

**django-admin startproject nombre-proyecto .**

para interactuar con manage.py se debe invocar con python
**python3 manage.py**

Para poder debugear por consola nuestra aplicación se puede utilizar el moduloo **pdb**

- esta línea debe ser incorporada justo antes de donde se dese debugear
**import pdb; pdb.set_tracce()**
- para poder salir desde la consola interactiva se debe enviar un **c** desde la consola


## Creación de aplicación con Django

Para crear aplicación con digango debemos ejecutar el siguiente comando con python

- python3 manage.py startapp **Nombre_apliacción**

```Python
DJANGO_APPS = (
    # Aca irian esas que estan desde el inicio del proyecto y vienen por defecto
)

THIRD_PARTY_APPS = (
    # Aca irian apps externas como Django Rest Framework, Celery, django debug toolbar, etc
)

LOCAL_APPS = (
    # Aca irian las apps de nuestros proyectos que vamoss a instalar, cosas como posts, perfiles, nosé
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
```

## Migraciones

- Para ejecutar las migraciones se debe realizar el siguiente comando
- **python3 manage.py migrate**
- Para crear una nueva migración se debe realizar el siguiente comando
- **Python3 manage.py makemigrations**
