# django-hallo-app

Для запуска проекта установите python версии 3.7 и выше, pip и virualenv

Поссле клонирования перейдите в склонированную папку и вывполните следующие команды:

Создайте виртуальное окружение командой
```bash
python3 -m virtualenv -p python3 venv
```

Активируйте виртуальное окружение командой
```bash
source venv/bin/activate
```

Перейдите в папку hello:
```bash
cd hello
```

Установите зависимости командой

```bash
pip install -r requirements.txt
```

Примените миграции командой
```bash
./manage.py migrate
```

Загрузите фикстурные теги командой
```bash
./manage.py loaddata fixtures/tags.json
```

Загрузите группы командой
```bash
./manage.py loaddata fixtures/groups.json
```

Загрузите пользователей командой
```bash
./manage.py loaddata fixtures/users.json
```

Загрузите фикстурные статьи командой
```bash
./manage.py loaddata fixtures/articles.json
```

Чтобы запустить сервер выполните:

```bash
./manage.py runserver
```

Для доступа в панель администратора перейдите по ссылке http://localhost:8000/admin


Username для администратора из фикстур: `admin`, пароль: `admin`

Username для автора из фикстур: `author`, пароль: `author`

Username для модератора из фикстур: `moderator`, пароль: `moderator`

Username для пользователя из фикстур: `user`, пароль: `user`
