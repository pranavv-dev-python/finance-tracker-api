# Finance Tracker API

A RESTful API built using Django REST Framework to manage personal finances, including income and expense tracking, category-based organization, and financial summaries with secure user authentication.

---

## 🚀 Features

- User Authentication (JWT-based login & registration)
- Add, update, and delete income & expense records
- Categorize transactions (e.g., Food, Travel, Bills)
- Filter transactions by category and date
- Monthly financial summary (income vs expenses)
- Secure user-specific data access

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- JWT Authentication

---

## 📌 API Endpoints

### Authentication
- `POST /api/register/` → Register a new user  
- `POST /api/login/` → Login and get access token  

### Transactions
- `GET /api/transactions/` → Get all transactions  
- `POST /api/transactions/` → Add new transaction  
- `PUT /api/transactions/{id}/` → Update transaction  
- `DELETE /api/transactions/{id}/` → Delete transaction  

### Filters & Summary
- `GET /api/transactions/?category=Food`  
- `GET /api/transactions/?date=2026-03`  
- `GET /api/summary/` → Monthly summary  

---

## ▶️ How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/yourusername/finance-tracker-api.git
