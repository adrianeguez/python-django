# python-django

```bash
conda create --name myDjangoEnv django
conda activate myDjangoEnv
conda deactivate
```

```bash
conda info --envs
```

```bash
django-admin startproject ejemplo
```


En settings editar django cojer el virtual environment y crear la nueva configuracion


```bash
django-admin startapp app_ejemplo
```


```bash
python manage.py createsuperuser
python manage.py migrate
python manage.py makemigrations 
python manage.py migrate
```