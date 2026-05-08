# devops-test-work-https-handler

В рамках тестового задания создано приложение, которое выполняет HTTP-запросы к сервису https://httpstat.us и обрабатывает ответы следующим образом.

Для запуска локально:

```
uv run main.py
```

Для запуска в Docker:

```
docker build -t http-handler .
docker run --name http-handler http-handler
```

Так как внутри прейбука есть задачи, которые требуют прав суперпользователя, то для запуска на localhost успользуется команда, которая запросит пароль sudo

```
ansible-playbook playbook.yml --ask-become-pass
```