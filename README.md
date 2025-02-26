# Zaawansowane Techniki Programowania 2024
## Projekt zaliczeniowy

```
pip install -r requirements.txt
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

```
docker exec -it postgres psql -U postgres -d ztp2024
```
