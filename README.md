# Лабораторная работа №6. Веб-программирование на Python

Таптыгин Константин Вадимович, группа 221141, вариант 6, лабораторная №6.

- Среднее №6: FastAPI возвращает приветствие на `GET /`.
- Среднее №8: `GET /hello?name=Константин` принимает имя.
- Среднее №2: форма Flask выводит приветствие по введённому имени.
- Повышенное №4: форма Flask загружает .txt в `instance/uploads/`. Максимальный размер запроса — 2 МиБ.
- Повышенное №10: три теста FastAPI на pytest.

Из папки проекта на macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

Запуск Flask: `python -m flask --app web run --port 5001`. Формы доступны по адресу http://127.0.0.1:5001/.

Запуск FastAPI: `python -m uvicorn api:app`. Swagger доступен по адресу http://127.0.0.1:8000/docs.
