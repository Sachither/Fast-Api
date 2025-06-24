# uncomment this code to enable migration endpoint 
# using render and trying to minimize cost that comes with proper migration


# from fastapi import APIRouter
# import subprocess

# router = APIRouter(
#     prefix="/migration",
#     tags=["migration"]
# )
# @router.get("/run-migrations")
# def run_migrations():
#     subprocess.run(["alembic", "upgrade", "head"])
#     return {"message": "Migrations applied"}
