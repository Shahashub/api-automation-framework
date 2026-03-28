# API Automation Framework

SDET-style API Automation Framework built using Python, Pytest, and Requests.

---

## 📌 Features

* Reusable API Client
* Pytest Fixtures for setup
* GET API Test Cases
* Clean and scalable structure

---

## 🛠️ Tech Stack

* Python
* Pytest
* Requests

---

## 📂 Project Structure

api-automation-framework/
│
├── client.py
├── conftest.py
├── test_api.py
├── pytest.ini
└── requirements.txt

---

## ▶️ How to Run

pip install -r requirements.txt
pytest -v

---

## ✅ Sample Test

def test_get_user(client):
response = client.get("/users/1")
assert response.status_code == 200

---

## 🚀 Future Improvements

* Add POST & DELETE test cases
* Add negative testing
* Add logging
* Add config file for environment handling
