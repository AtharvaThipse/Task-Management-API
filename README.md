# 🚀 Scalable Task Management API

A production-ready backend system built using **FastAPI**, featuring JWT authentication, Role-Based Access Control (RBAC), Redis caching, and Dockerized deployment on AWS.

---

## 📌 Features

* 🔐 JWT Authentication (OAuth2)
* 👥 Role-Based Access Control (Admin/User)
* ⚡ Redis Caching for performance optimization
* 📦 RESTful APIs with CRUD operations
* 🔍 Pagination, Filtering, and Search
* 🐳 Dockerized application
* ☁️ AWS EC2 deployment ready
* 🧱 Clean architecture (modular & scalable)

---

## 🛠 Tech Stack

* **Backend:** FastAPI (Python)
* **Database:** PostgreSQL
* **Cache:** Redis
* **Authentication:** JWT (OAuth2)
* **Containerization:** Docker
* **Cloud:** AWS EC2

---

## 📂 Project Structure

```
app/
 ├── api/            # API routes
 ├── core/           # config, security, redis
 ├── models/         # database models
 ├── schemas/        # pydantic schemas
 ├── services/       # business logic
 ├── db/             # database connection
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2️⃣ Setup Virtual Environment

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 🐳 Run with Docker

```
docker-compose up --build
```

---

## ▶️ Run Locally

```
uvicorn app.main:app --reload
```

---

## 🔐 Authentication

* Register a new user
* Login to get JWT token
* Use **Authorize 🔒 button in Swagger UI**

---

## 📡 API Documentation

```
http://localhost:8000/docs
```

---

## 👑 Admin Access

* Default role: `user`
* Change role in DB to `admin` for admin privileges

---

## ⚡ Redis Caching

* Frequently accessed endpoints cached
* Improves performance and reduces DB load

---

## ☁️ Deployment (AWS)

* Hosted on AWS EC2
* Dockerized for scalability
* Public API accessible via EC2 IP

---

## 📈 Future Improvements

* ✅ CI/CD Pipeline (GitHub Actions)
* ✅ Nginx + Domain + HTTPS
* ✅ Background jobs (Celery + Redis)
* ✅ Rate limiting & security enhancements

---

## 💼 Resume Highlight

> Built a scalable task management backend using FastAPI with JWT authentication, RBAC, Redis caching, and Dockerized deployment on AWS EC2.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Atharva Thipse**

---
