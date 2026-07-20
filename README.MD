# Docker Flask PostgreSQL Full Stack Application

A production-style multi-container application built using **Docker Compose**, consisting of a **Frontend**, **Flask Backend**, and **PostgreSQL Database**. This project demonstrates containerization, Docker networking, persistent storage, REST APIs, environment variables, and frontend-backend communication.

---

# Architecture

```
                    Browser
                        │
                        ▼
              Frontend (Nginx)
                 Port: 8080
                        │
         HTTP Request (Fetch API)
                        │
                        ▼
              Flask Backend API
                 Port: 5000
                        │
           PostgreSQL Connection
                        │
                        ▼
              PostgreSQL Database
                 Port: 5432
```

---

# Tech Stack

- Docker
- Docker Compose
- Python
- Flask
- Flask-CORS
- PostgreSQL
- HTML
- CSS
- JavaScript

---

# Project Structure

```
project/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── init.sql
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   └── Dockerfile
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

# Components

## Frontend

The frontend is built using HTML, CSS, and JavaScript.

Responsibilities:

- Displays backend information
- Displays list of users
- Sends POST requests to save users
- Calls Flask REST APIs using Fetch API

Port:

```
8080
```

---

## Backend

The backend is developed using Flask.

Responsibilities:

- REST API development
- Database connectivity
- JSON responses
- User creation
- User retrieval
- CORS configuration

Port:

```
5000
```

API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Health Check |
| GET | /users | Get All Users |
| POST | /users | Save User |

---

## Database

Database used:

```
PostgreSQL 16
```

Responsibilities

- Store users
- Persistent storage using Docker Volumes
- Initialize schema using init.sql

Port

```
5432
```

---

# Docker Compose Services

## PostgreSQL Service

```
postgres:
```

Responsibilities

- Creates PostgreSQL container
- Creates demo database
- Executes init.sql automatically
- Stores data using Docker Volume

Environment Variables

```
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
```

---

## Backend Service

```
backend:
```

Responsibilities

- Builds Flask image
- Connects to PostgreSQL
- Exposes REST APIs

Environment Variables

```
DB_HOST
DB_NAME
DB_USER
DB_PASSWORD
```

Port Mapping

```
5000:5000
```

---

## Frontend Service

```
frontend:
```

Responsibilities

- Builds frontend image
- Serves HTML/CSS/JavaScript
- Calls backend APIs

Port Mapping

```
8080:80
```

---

# Docker Networking

Docker Compose automatically creates a bridge network.

Containers communicate using **service names**.

Backend connects to PostgreSQL using

```
DB_HOST=postgres
```

instead of

```
localhost
```

Communication Flow

```
Frontend
    │
    ▼
Backend
    │
    ▼
PostgreSQL
```

---

# Docker Volume

Persistent storage is provided using

```
postgres-data
```

Even if the PostgreSQL container is removed, database data remains stored inside the Docker volume.

---

# CORS Configuration

Frontend runs on

```
http://EC2-Public-IP:8080
```

Backend runs on

```
http://EC2-Public-IP:5000
```

Since frontend and backend use different ports, Cross-Origin Resource Sharing (CORS) is enabled in Flask using Flask-CORS.

---

# Running the Project

Clone the repository

```bash
git clone https://github.com/yourusername/docker-flask-postgresql-fullstack.git
```

Go to project directory

```bash
cd docker-flask-postgresql-fullstack
```

Build containers

```bash
docker compose up --build -d
```

Verify containers

```bash
docker ps
```

Open application

```
http://<EC2-Public-IP>:8080
```

---

# Useful Docker Commands

Build project

```bash
docker compose up --build
```

Run in background

```bash
docker compose up -d
```

Stop project

```bash
docker compose down
```

View logs

```bash
docker logs backend

docker logs postgres

docker logs frontend
```

List containers

```bash
docker ps
```

Connect to PostgreSQL

```bash
docker exec -it postgres psql -U postgres -d demo
```

List tables

```sql
\dt
```

View users

```sql
SELECT * FROM users;
```

---

# Learning Outcomes

Through this project I gained hands-on experience with:

- Docker Images
- Docker Containers
- Docker Compose
- Docker Networking
- Docker Volumes
- Flask REST APIs
- PostgreSQL Integration
- Environment Variables
- Port Mapping
- REST API Communication
- Frontend-Backend Integration
- CORS Configuration
- Multi-Container Architecture

---



# Author

**Yakshith R**

Aspiring DevOps Engineer passionate about Cloud, Docker, Kubernetes, Terraform, CI/CD, and Infrastructure Automation.
