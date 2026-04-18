# 🚀 FastAPI Backend Evolution Project (Updated Version)

This project is an upgraded backend system built with **FastAPI**, evolving from a simple JSON-based API into a structured, database-driven, and asynchronously optimized backend system.

It demonstrates real-world backend engineering concepts including:
- CRUD operations
- SQLAlchemy ORM integration
- Relational database design
- Async concurrency with FastAPI
- Data validation using Pydantic
- API structuring and routing design

---

# 🧠 Project Evolution Overview

## 🔹 Phase 1: JSON-Based API (Initial Version)
- Stored data in local `.json` files
- Manual read/write operations
- Basic CRUD endpoints:
  - Create user
  - Add order
  - Update data
  - Delete records
  - Fetch by ID

### Key Learning:
- File handling in Python
- Basic FastAPI routing
- Data structuring using dictionaries

---

## 🔹 Phase 2: Database Integration (SQLAlchemy Upgrade)
- Replaced JSON storage with **SQLite database**
- Introduced ORM models using SQLAlchemy
- Separated:
  - Models (Database structure)
  - Schemas (API validation)
  - Storage layer (Session management)

### Key Improvements:
- Persistent storage
- Structured relational data
- Better scalability foundation

### Core Concepts Implemented:
- SQLAlchemy `Base`, `SessionLocal`, `engine`
- Table models (User, Order)
- CRUD using ORM queries
- Foreign key relationships (user_id → orders)

---

## 🔹 Phase 3: Data Validation & Schema Control
- Implemented **Pydantic schemas**
- Added strict validation rules:
  - Age constraints
  - Amount constraints
  - String length validation
- Used:
  - `Field()`
  - `Enum`
  - `field_validator`

### Key Learning:
- Input validation layer separation
- Data integrity enforcement
- Schema vs Model distinction

---

## 🔹 Phase 4: Async Programming Integration
- Introduced **async/await in FastAPI**
- Implemented concurrent request handling
- Used:
  - `asyncio.gather()`
  - `asyncio.to_thread()`

### Features:
- Concurrent dashboard endpoint
- Parallel execution of user + order fetching
- Simulated external API calls

### Key Concept:
- Improved response efficiency under I/O-bound operations

---

# ⚙️ System Architecture (Final State)

C:.
├───.history
│   ├───app
│   │   ├───database
│   │   ├───router
│   │   ├───schema
│   │   └───storage
│   └───Data
├───app
│   ├───database
│   │   ├───.history
│   │   └───__pycache__
│   ├───middleware
│   ├───router
│   │   └───__pycache__
│   └───schema
│       └───__pycache__
└───__pycache__




---

# 📦 Core Features

## 👤 User Management
- Create user
- Fetch user by ID
- Delete user (with safety checks)

## 🍽️ Order System
- Create order linked to user
- Fetch order by user + order ID
- Delete order
- Validate order constraints

## 📊 Dashboard (Async Feature)
- Fetch user data + orders concurrently
- Optimized response time using async execution

---

# 🧪 Validation System
- Age limits enforced (1–120)
- Amount constraints
- Enum-based status control
- Custom field validators

---

# ⚡ Async Features

- Concurrent execution using `asyncio.gather()`
- Thread-based DB execution using `asyncio.to_thread()`
- Simulated API latency handling

---

# 🗄️ Database Design

### User Table
- id (Primary Key)
- name
- age
- country

### Order Table
- id (Primary Key)
- user_id (Foreign Key concept)
- restaurant
- food
- amount
- status

---

# 🧠 Key Learnings

- Difference between **schema vs model**
- Why relational databases matter
- Proper API design structure
- Async vs sync execution trade-offs
- Importance of request validation
- Handling database integrity errors

---

# ⚠️ Known Challenges Encountered

- SQLite database locking issues under concurrent access
- Response validation errors due to schema mismatch
- Integrity constraints (duplicate IDs, missing fields)
- Async + sync mixing complexity

---

# 🚀 Final Outcome

This project now represents a **real backend system foundation**, capable of:
- Handling structured data
- Supporting relational queries
- Scaling logic through async execution
- Enforcing strict validation rules

---

# 📌 Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Python asyncio

---

# 🔥 Future Improvements (Planned)
- Migration to PostgreSQL
- True async database (AsyncSession)
- Authentication system (JWT)
- Role-based access control
- Docker deployment
- Production-grade architecture layering

---

# 👤 Author
Built as part of a structured backend engineering learning system focused on real-world software engineering mastery.