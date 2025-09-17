# FastAPI Social Media API

This is a robust REST API built with FastAPI for a social media application. The API includes features like user authentication, post management, and voting system.

## Features

- 🔐 **User Authentication** with JWT tokens
- 👤 **User Management** (Create, Read, Update, Delete)
- 📝 **Post Management** (Create, Read, Update, Delete)
- 👍 **Voting System** for posts
- 🔄 **Database Migrations** using Alembic
- ⚡ **CORS Middleware** enabled
- 📚 **SQLAlchemy ORM** for database operations

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs with Python
- **PostgreSQL**: Primary database
- **SQLAlchemy**: SQL toolkit and ORM
- **Alembic**: Database migration tool
- **PyJWT**: JSON Web Token implementation
- **Bcrypt**: Password hashing
- **Python 3.11+**: Programming language

## Prerequisites

- Python 3.11 or higher
- PostgreSQL database
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Sachither/Fast-Api.git
cd Fast-Api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables by creating a `.env` file in the root directory:
```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_password
DATABASE_NAME=your_db_name
DATABASE_USERNAME=your_username
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Run database migrations:
```bash
alembic upgrade head
```

## Running the Application

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

### Authentication
- `POST /login` - User login
- `POST /users/` - Create new user

### Posts
- `GET /posts` - Get all posts
- `POST /posts` - Create new post
- `GET /posts/{id}` - Get specific post
- `PUT /posts/{id}` - Update post
- `DELETE /posts/{id}` - Delete post

### Votes
- `POST /vote` - Vote/Unvote a post

### Users
- `GET /users/{id}` - Get user information
- `POST /users/` - Create new user

## Database Schema

The project uses several tables managed through SQLAlchemy models:
- `users` - User information and authentication
- `posts` - Post content and metadata
- `votes` - Post voting system

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- FastAPI documentation and community
- SQLAlchemy documentation
- Alembic documentation