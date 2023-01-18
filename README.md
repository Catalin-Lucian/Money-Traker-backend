# Money Tracker

Money Tracker is a web-based application that allows you to keep track of your finances by recording deposits and withdrawals. The application consists of a backend built using FastAPI and a frontend built using React.

## Installation

### Backend

1. Clone the backend repository from [Money-Traker-backend](https://github.com/Catalin-Lucian/Money-Traker-backend)
2. Create a virtual environment and activate it.
3. Run `pip install -r requirements.txt` to install the necessary packages.
4. Run `uvicorn main:app --reload` to start the server

### Frontend

1. Clone the frontend repository from [Money-Traker-frontend](https://github.com/Catalin-Lucian/Money-Traker-frontend)
2. Run `npm install` to install the necessary packages.
3. Run `npm start` to start the development server.
4. Open <http://localhost:3000> in your browser to access the application.

## Dependencies

The backend depends on the following packages:

- fastapi
- pydantic
- SQLAlchemy
- passlib
- pyJWT
- uvicorn
- bcrypt

The frontend depends on the following packages:

- @chakra-ui/react
- axios
- formik
- react-router-dom

## Configuration

The backend uses SQLAlchemy to interact with a database. You can use any database supported by SQLAlchemy, but the application has been tested with PostgreSQL.

The frontend is configured to connect to the backend running on <http://localhost:8000>. If you wish to connect to a different backend, you can modify the baseURL variable in the jwt.interceptor.js file.

## Usage

Once the application is running, you can register a new account or log in with an existing one. Once logged in, you will be able to add new operations (deposits or withdrawals), view your existing operations and navigate between pages.

You can also edit or delete existing operations by clicking on the respective buttons.

## Bibliography

[FastAPI documentation](https://fastapi.tiangolo.com)
[React documentation](https://reactjs.org)
[SQLAlchemy documentation](https://docs.sqlalchemy.org/en/14/)
[passlib documentation](https://passlib.readthedocs.io/en/stable/)
[pyJWT documentation](https://pyjwt.readthedocs.io/en/latest/)
[uvicorn documentation](https://www.uvicorn.org)
[bcrypt documentation](https://pypi.org/project/bcrypt/)
