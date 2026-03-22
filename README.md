## 📦 Стек технологий
- **FastAPI** — backend-фреймворк  
- **PostgreSQL** — база данных  
- **SQLAlchemy / Alembic** — ORM и миграции  
- **Docker / Docker Compose** — контейнеризация  
- **Pydantic** — валидация данных  

---

## ⚙️ Установка и запуск

### 1️⃣ Клонирование репозитория
```bash
git clone https://github.com/m0r-h2/test_project.git
cd ServiceHub 
```

### ❗ Убитесь что переименовали или создали новый .env

### 2️⃣ Сборка и запуск контейнеров
```bash
docker compose up -d --build
```
### 3️⃣ Добавление тестовых пользователей

```bash
docker compose exec app uv run python -m seed
```
