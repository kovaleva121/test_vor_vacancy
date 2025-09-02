# Тестовое задание на вакансию Разработчик 'Django/Django Rest Framework' в компанию Qortex
## Описание проекта
REST API для управления плейлистом, реализованное на Django и Django REST Framework. Система предоставляет функционал для управления артистами, альбомами, песнями и треками.

## 🚀 Функциональность
## Основная часть (обязательная по ТЗ):
#### ✅ CRUD для артистов
#### ✅ CRUD для альбомов
#### ✅ CRUD для песен
#### ✅ CRUD для треков
#### ✅ CRUD операции описаны через ViewSet классы
#### ✅ Описаны сериализаторы для каждой модели
#### ✅ Создана автоматическая документация API (Swagger)
#### ✅ Реализована сборка и установка образов через Docker-compose

## Технологический стек
#### Backend: Django 4.2 + Django REST Framework

#### База данных: PostgreSQL

#### Контейнеризация: Docker + Docker Compose

#### Документация: DRF Spectacular 

## 📂 Установка и запуск

Клонировать репозиторий:
```
 git clone https://github.com/yourname/test_for_vacancy.git`

```

Создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
Создать файл .env на основе .env.example:
```
cp .env.example .env
```
Запустить сервисы:
```
docker-compose up -d --build
```

Создать суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```


## Доступ к сервисам
### API: http://localhost:8000/api/

### Админка: http://localhost:8000/admin/

## Документация API:

### Swagger UI: http://localhost:8000/api/schema/swagger-ui/



