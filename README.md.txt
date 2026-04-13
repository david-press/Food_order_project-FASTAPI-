# 🍽️ Food Order API (FastAPI Project)

## 📌 Overview

This project is a backend API built with FastAPI that simulates a simple food ordering system. It allows users to create profiles, place food orders, update them, retrieve data, and delete records — all stored in a JSON file acting as a lightweight database.

---

## 🎯 What This Project Covers

* Creating and managing user data
* Placing food orders linked to users
* Updating existing records dynamically
* Retrieving data by unique ID
* Deleting records safely
* Basic data persistence using JSON files

---

## 🧠 Core Concepts Learned

* REST API design (CRUD operations)
* Request validation using Pydantic schemas
* Response modeling for clean API output
* Enum usage for controlled values (status handling)
* Custom validation logic using field validators
* Handling optional fields for partial updates
* Unique ID generation using UUID
* File-based data storage (JSON persistence)

---

## ⚙️ How It Works

1. User data is created and stored in a JSON file
2. Each user is assigned a unique ID
3. Food orders are linked to that ID
4. Data is updated or retrieved using the ID as reference
5. All changes are persisted back into the JSON file

---

## ⚠️ Challenges Faced & Fixed

* Incorrect use of list vs dictionary operations
* Data overwriting instead of proper appending/updating
* Schema mismatch causing validation errors
* Incorrect constraint usage on integer fields
* Datetime serialization issues
* Response model mismatch errors
* Data corruption due to incorrect save logic

---

## 🧠 Key Takeaways

* API structure must be consistent and predictable
* Schema design controls data integrity
* File storage requires strict handling of data structure
* Validation must be enforced at schema level, not only inside routes
* Response models must match returned data exactly

---
project structure:
C:.
├───.history
│   ├───app
│   │   ├───router
│   │   ├───schema
│   │   └───storage
│   └───Data
├───app
│   ├───middleware
│   ├───router
│   │   └───__pycache__
│   ├───schema
│   │   └───__pycache__
│   └───storage
│       └───__pycache__
├───Data
└───__pycache__
---
## 🚀 Conclusion

This project builds a strong foundation in backend development using FastAPI by combining validation, routing, and persistent storage into a working system. It prepares for more advanced concepts like async programming and scalable architecture.
