from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.api_v1.customers.shemas import CustomerUpdate, CustomerCreate, CustomerUpdatePartial
from backend.app.database.models import Customer


async def get_customers(session: AsyncSession) -> list[Customer]:
    stmt = select(Customer).order_by(Customer.customer_id)
    result: Result = await session.execute(stmt)
    customers = result.scalars().all()
    return list(customers)


async def get_customer(customer_id: int, session: AsyncSession) -> Customer | None:
    return await session.get(Customer, customer_id)


async def create_customer(new_customer: CustomerCreate, session: AsyncSession) -> Customer:
    customer = Customer(**new_customer.model_dump())
    session.add(customer)
    await session.commit()
    return customer


async def update_customer(
        customer: Customer,
        upd_customer: CustomerUpdate | CustomerUpdatePartial,
        session: AsyncSession,
        partial: bool = False
) -> Customer:
    for name, value in upd_customer.model_dump(exclude_unset=partial).items():
        setattr(customer, name, value)
    await session.commit()
    return customer


async def delete_customer(customer: Customer, session: AsyncSession) -> None:
    await session.delete(customer)
    await session.commit()


