import asyncio
from decimal import Decimal
from datetime import datetime, timedelta

from sqlalchemy import select

from backend.app.database.models import Company, Worker, Task, db_helper
from backend.app.core import hash_password

async def seed_db():

    async with db_helper.session_factory() as db:

        # ----------------
        # COMPANIES
        # ----------------
        companies = [
            Company(
                name="ООО Удачный ремонт",
                email="test@gmail.ru",
                password=hash_password("hashed"),
                phone="+79001001001",
                city="Москва",
                rating=Decimal("4.6"),
                sum_reviews=45,
                comment="Ремонт квартир и бытовой техники"
            ),

            Company(
                name="Быстрая доставка",
                email="delivery@servicehub.ru",
                password=hash_password("hashed"),
                phone="+79001001002",
                city="Москва",
                rating=Decimal("4.4"),
                sum_reviews=33,
                comment="Доставка по городу"
            ),
            Company(
                name="Мастер сервис",
                email="master@servicehub.ru",
                password=hash_password("hashed"),
                phone="+79001001003",
                city="Санкт-Петербург",
                rating=Decimal("4.7"),
                sum_reviews=51,
                comment="Сантехника и электрика"
            ),
        ]

        db.add_all(companies)
        await db.commit()

        # ----------------
        # WORKERS
        # ----------------
        workers = [

            Worker(
                name="Алексей Смирнов",
                phone="+79100000001",
                company_name="ООО Удачный ремонт",
                job_title="Босс",
                status="Свободен"
            ),

            Worker(
                name="Иван Петров",
                phone="+79100000002",
                company_name="ООО Удачный ремонт",
                job_title="Техник",
                status="На выезде"
            ),

            Worker(
                name="Дмитрий Кузнецов",
                phone="+79100000003",
                company_name="ООО Удачный ремонт",
                job_title="Администратор",
                status="Свободен"
            ),

            Worker(
                name="Сергей Иванов",
                phone="+79100000004",
                company_name="Быстрая доставка",
                job_title="Босс",
                status="Свободен"
            ),

            Worker(
                name="Андрей Волков",
                phone="+79100000005",
                company_name="Быстрая доставка",
                job_title="Босс",
                status="На выезде"
            ),

            Worker(
                name="Максим Орлов",
                phone="+79100000006",
                company_name="Быстрая доставка",
                job_title="Водитель",
                status="Свободен"
            ),

            Worker(
                name="Никита Павлов",
                phone="+79100000007",
                company_name="Мастер сервис",
                job_title="Босс",
                status="Свободен"
            ),

            Worker(
                name="Олег Морозов",
                phone="+79100000008",
                company_name="Мастер сервис",
                job_title="Техник",
                status="На выезде"
            ),

        ]

        db.add_all(workers)
        await db.commit()

        # ----------------
        # Получаем id компаний
        # ----------------
        result = await db.execute(select(Company))
        company_list = result.scalars().all()

        company_map = {c.name: c.id for c in company_list}

        # ----------------
        # TASKS
        # ----------------
        tasks = [

            Task(
                title="Ремонт стиральной машины",
                phone="+74952002001",
                work="Ремонт",
                city="Москва",
                address="ул. Тверская 12",
                required="Инструменты",
                text="Стиральная машина не сливает воду",
                price=Decimal("3500"),
                company_id=None,
                technical="Иван Петров",
                status="В работе",
                progress=40,
                end_date=datetime.now() + timedelta(days=1)
            ),

            Task(
                title="Доставка мебели",
                phone="+74952002002",
                work="Доставка",
                city="Москва",
                address="ул. Арбат 15",
                required="Грузовой транспорт",
                text="Доставить диван и шкаф",
                price=Decimal("2500"),
                company_id=None,
                driver="Андрей Волков",
                status="В работе",
                progress=20,
                end_date=datetime.now() + timedelta(hours=5)
            ),

            Task(
                title="Ремонт розетки",
                phone="+78123003001",
                work="Ремонт",
                city="Санкт-Петербург",
                address="Невский проспект 45",
                required="Электроинструменты",
                text="Не работает розетка",
                price=Decimal("1500"),
                company_id=None,
                technical="Олег Морозов",
                status="Заявка создана",
                progress=0
            ),

            Task(
                title="Сборка шкафа",
                phone="+78123003002",
                work="Сервисное Обслуживание",
                city="Санкт-Петербург",
                address="ул. Ленина 8",
                required="Инструменты",
                text="Собрать шкаф IKEA",
                price=Decimal("3000"),
                company_id=None,
                technical="Олег Морозов",
                status="В работе",
                progress=15
            ),

        ]

        db.add_all(tasks)
        await db.commit()

        print("Seed успешно загружен")


if __name__ == "__main__":
    asyncio.run(seed_db())