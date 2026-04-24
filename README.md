# Effective Mobile DevOps Test Task

Проект выполнен в рамках тестового задания на позицию DevOps.

Приложение состоит из двух Docker-контейнеров:

- backend
- nginx

Nginx принимает HTTP-запросы на порт 80 и проксирует их во внутренний backend-сервис на порт 8080.

## Схема работы

```text
User
 |
 v
localhost:80
 |
 v
Nginx container
 |
 v
Backend container:8080
```

## Использованные технологии

- Docker
- Docker Compose
- Python 3.12
- Python http.server
- Nginx

## Структура проекта

```text
├── backend/
│   ├── Dockerfile
│   └── app.py
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Как запустить проект

В корне проекта выполните команду:

```bash
docker compose up -d --build
```

## Как проверить результат

После запуска выполните:

```bash
curl http://localhost
```

Ожидаемый ответ:

```text
Hello from Effective Mobile!
```

Также можно открыть в браузере:

```text
http://localhost
```

## Как остановить проект

```bash
docker compose down
```

## Как работает схема

Backend-приложение слушает порт 8080 внутри Docker-сети.

Backend не публикует порт наружу, поэтому напрямую с хоста он недоступен.

Nginx доступен на порту 80 хоста и проксирует запросы во внутренний backend-сервис по адресу:

```text
http://backend:8080
```

## Проверка контейнеров

Посмотреть запущенные контейнеры:

```bash
docker compose ps
```

Посмотреть логи:

```bash
docker compose logs
```
