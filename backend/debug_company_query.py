import asyncio
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from models.company import Company
from database import SessionLocal

async def main():
    async with SessionLocal() as db:
        try:
            result = await db.execute(select(Company).options(selectinload(Company.jobs)))
            companies = result.scalars().all()
            print('COMPANY COUNT', len(companies))
            for c in companies[:5]:
                print('COMPANY', c.id, c.name, 'jobs', len(c.jobs))
                for j in c.jobs[:5]:
                    print(' JOB', j.id, j.title, j.company_id)
        except Exception as e:
            import traceback
            traceback.print_exc()

asyncio.run(main())
