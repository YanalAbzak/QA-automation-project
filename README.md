# API Automation Project

## 🧪 Features

- Flask-based REST API
- Full CRUD operations on `/users`
- Automated tests using `pytest` + `requests`
- HTML test reports
- GitHub Actions CI pipeline

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the API server

```bash
python api-server/app.py
```

### 3. Run the tests

```bash
pytest
```

## ✅ Sample Endpoints

- `POST /users`
- `GET /users`
- `GET /users/<id>`
- `PUT /users/<id>`
- `DELETE /users/<id>`

## 📊 HTML Report

Generated after test run at `reports/report.html`.

## 🛠️ GitHub Actions CI

On each push/pull request:
- Installs dependencies
- Runs pytest
- Generates HTML test report