from pathlib import Path
from uuid import uuid4

from flask import Flask, render_template, request

app = Flask(__name__)
app.config.update(
    MAX_CONTENT_LENGTH=2 * 1024 * 1024,
    UPLOAD_FOLDER=Path(app.instance_path) / "uploads",
)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/greet")
def greet():
    name = request.form.get("name", "").strip()
    if not 1 <= len(name) <= 80:
        return render_template("index.html", error="Введите имя от 1 до 80 символов."), 400
    return render_template("index.html", name=name)


@app.post("/upload")
def upload():
    file = request.files.get("file")
    if not file or Path(file.filename).suffix.lower() != ".txt":
        return render_template("index.html", error="Выберите файл .txt."), 400

    folder = Path(app.config["UPLOAD_FOLDER"])
    folder.mkdir(parents=True, exist_ok=True)
    file.save(folder / f"{uuid4().hex}.txt")
    return render_template("index.html", uploaded=file.filename)


@app.errorhandler(413)
def too_large(error):
    return render_template("index.html", error="Запрос превышает 2 МиБ."), 413
