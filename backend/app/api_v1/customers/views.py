from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from .dependencies import get_customer_id
from .shemas import CustomerBase, CustomerCreate, CustomerUpdate, CustomerUpdatePartial, Customer
from backend.app.database.models import db_helper


router = APIRouter(
    tags=["Customers"]
)


@router.get("/", response_model=list[Customer], status_code=status.HTTP_200_OK)
async def get_customers(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_customers(session=session)



@router.get("/{customer_id}", response_model=Customer, status_code=status.HTTP_200_OK)
async def get_customer(customer: Customer = Depends(get_customer_id)):
    return customer



@router.post("/", response_model=CustomerBase, status_code=status.HTTP_201_CREATED)
async def create_customer(new_customer: CustomerCreate,
                          session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_customer(
        new_customer=new_customer,
        session=session
    )



@router.put("/{customer_id}", response_model=CustomerBase)
async def update_customer(
        new_customer: CustomerUpdate,
        customer: Customer = Depends(get_customer_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_customer(
        upd_customer=new_customer,
        customer=customer,
        session=session
    )



@router.patch("/{customer_id}", response_model=Customer)
async def update_customer_partial(
        upd_customer: CustomerUpdatePartial,
        customer: Customer = Depends(get_customer_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_customer(
        upd_customer=upd_customer,
        customer=customer,
        session=session,
        partial=True
    )


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(
        customer: Customer = Depends(get_customer_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await crud.delete_customer(
        customer=customer,
        session=session
    )