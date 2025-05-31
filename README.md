
# 🧪 QA Automation Project (Python + Pytest)

A complete QA automation project built with **Python** and **Pytest**, focusing on testing CRUD operations for a course management system. Includes CI/CD integration via **GitHub Actions** and generates detailed HTML reports.

## 📦 Project Structure

```

api-automation-project/
│
├── api-server/              # Optional: your backend app (Node.js or Flask)
│   └── app.py
│
├── tests/                   # Automated tests using pytest
│   ├── test\_courses.py
│   └── conftest.py
│
├── reports/                 # HTML test reports
│   └── report.html
│
├── .github/workflows/       # CI pipeline
│   └── ci.yml
│
├── requirements.txt         # Python dependencies
├── pytest.ini               # Pytest configuration
├── README.md
└── .gitignore

````

## ✅ Features

- Test coverage for Add / Edit / Delete / List endpoints
- Assertion of status codes, redirects, and content
- Pytest-based structure with clean, modular test functions
- HTML reports via `pytest-html`
- Fully automated CI pipeline with GitHub Actions

## 🚀 Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/api-automation-project.git
cd api-automation-project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest --html=reports/report.html
````

## 🔄 CI/CD – GitHub Actions

The project runs all tests automatically on every push via GitHub Actions.
The workflow file is located at:

```
.github/workflows/ci.yml
```

It:

* Installs Python
* Installs dependencies
* Runs pytest
* Fails build on test failure

## 🧪 Sample Test Code

```python
def test_add_course():
    res = requests.post("http://localhost:3030/Crs/Add", data={"name": "Python QA Course"})
    assert res.status_code in [200, 302]
```

