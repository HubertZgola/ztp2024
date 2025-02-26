```
pip install -r szu/requirements.txt
```

```
docker run --name postgres -e POSTGRES_PASSWORD=qwerty -e POSTGRES_DB=ztp2024 -p 5432:5432 -d postgres
```

```
python manage.py makemigrations
```

```
python manage.py migrate
```

```
python manage.py runserver
```
