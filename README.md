# Task Manager API

This is a Task Manager API built with FastAPI. It provides endpoints for managing tasks, including creating, updating, and listing tasks.

## Table of Contents

- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/task_manager.git
    cd task_manager
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:

    Ensure you have PostgreSQL installed and running. Create a database for the project.

    ```sh
    createdb swift_task_mgr_db
    ```

5. Configure the database URL in your environment variables:

    ```sh
    export DATABASE_URL="postgresql://postgres:@localhost:5432/swift_task_mgr_db"
    ```

## Running the Application

1. Start the FastAPI server:

    ```sh
    uvicorn main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`.

3. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Task Endpoints

- `GET /tasks/`: List all tasks for the current user.
- `POST /tasks/`: Create a new task.
- `PUT /tasks/{task_id}`: Update an existing task.

### Authentication Endpoints

- `POST /api/auth/register`: Register a new user.
- `POST /api/auth/login`: Login a user.

## Testing

1. Install the testing dependencies:

    ```sh
    pip install pytest httpx
    ```

2. Run the tests:

    ```sh
    pytest
    ```

## Project Structure
```sh
task_manager/
│── __init__.py   <-- Required!
│── main.py
│── core/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   ├── security.py
│── db/
│   ├── __init__.py
│   ├── base_model.py
│   ├── session.py
│── models/
│   ├── __init__.py
│   ├── task.py
│   ├── user.py
│── repositories/
│   ├── __init__.py
│   ├── task.py
│   ├── user.py
│── routes/
│   ├── __init__.py
│   ├── auth.py
│   ├── tasks.py
│── services/
│   ├── __init__.py
│   ├── task.py
│── dtos/
│   ├── __init__.py
│   ├── task.py
│   ├── user.py
```