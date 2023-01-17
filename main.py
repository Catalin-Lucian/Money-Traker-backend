from fastapi import FastAPI

from api.deposit import deposits
from api.operation import operations
from database.db_manager import create_db
from api.users import users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create the database
create_db()

# add route to users
app.include_router(users)

# add route to deposits
app.include_router(deposits)

# add route to operations
app.include_router(operations)

