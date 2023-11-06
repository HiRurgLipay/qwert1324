# Инструкция по развертыванию проекта

Этот README предоставляет пошаговую инструкцию по установке и настройке проекта.

## Шаг 1: Установка необходимых компонентов

Установите следующие пакеты на сервере:

- Python 3.11
- PostgreSQL и PostgreSQL-contrib
- Nginx
- Poetry
- Flask
- Flask-JSON
- psycopg2

## Шаг 2: Создание базы данных PostgreSQL

Создайте базу данных PostgreSQL, которая будет использоваться проектом.

## Шаг 3: Клонирование проекта на сервер

Склонируйте проект на сервер c GitHub.

## Шаг 4: Установка зависимостей проекта

Установите Poetry в качестве пакетного менеджера в проекте:

<pre>
poetry init
</pre>

Затем выполните следующую команду для установки зависимостей проекта:

<pre>
poetry install
</pre>

## Шаг 5: Активация виртуального окружения и установка Gunicorn

Убедитесь, что виртуальное окружение активировано и установите Gunicorn:

<pre>
poetry shell
poetry add gunicorn
</pre>

## Шаг 6: Настройка файлов проекта

В файле app/____init____.py вашего проекта установите нужные IP-адреса или доменные имена, включая "localhost" для конфигурации с базой данных.

## Шаг 7: Создание файла сокета для Gunicorn

Создайте файл сокета для Gunicorn:

<pre>
sudo nano /etc/systemd/system/gunicorn.socket
</pre>

Содержимое файла:

<pre>
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
</pre>

## Шаг 8: Создание служебного файла systemd для Gunicorn

Создайте служебный файл systemd для Gunicorn:

<pre>
sudo nano /etc/systemd/system/gunicorn.service
</pre>

Содержимое файла:

<pre>
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=user_name # имя юзера для запуска
Group=www-data
WorkingDirectory=/home/user_name/tadd43723
ExecStart=*здесь указывается путь к виртуальному окружению проекта* \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          tadd43723.wsgi:application

[Install]
WantedBy=multi-user.target
</pre>

## Шаг 9: Запуск и активация сокета Gunicorn

Запустите и активируйте сокет Gunicorn:

<pre>
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
</pre>

## Шаг 10: Создание и настройка серверного блока Nginx

Создайте и настройте серверный блок Nginx:

<pre>
sudo nano /etc/nginx/sites-available/tadd43723
</pre>

Содержимое файла:

<pre>
server {
    listen 80;
    server_name *IP-адрес сервера или доменное имя*;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/user_name/tadd43723;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
</pre>

## Шаг 11: Активация файла Nginx

Активируйте файл серверного блока Nginx:

<pre>
sudo ln -s /etc/nginx/sites-available/tadd43723 /etc/nginx/sites-enabled
</pre>

## Шаг 12: Перезапуск Nginx

Перезапустите Nginx:

<pre>
sudo systemctl restart nginx
</pre>

## Шаг 13: Настройка брандмауэра

Разрешите трафик для Nginx:

<pre>
sudo ufw allow 'Nginx Full'
</pre>

Теперь проект должен быть развернут и доступен на сервере.
