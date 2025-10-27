
<!-- ============================================================= -->
<!-- COURSERA.PROJECT by NovusAevum (WMH) - Expense Tracker App    -->
<!-- ============================================================= -->

<div align="center">

# 📊 Expense Tracker App (Django)
_A sophisticated Django web solution for managing and visualizing book inventory and expenses with full CRUD automation and analytics._

[![Django](https://img.shields.io/badge/Django-5.2.7-0C4B33?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Education-green)](#license)
[![GitHub Repo](https://img.shields.io/badge/GitHub-NovusAevum-blue?logo=github)](https://github.com/NovusAevum)
[![Last Commit](https://img.shields.io/github/last-commit/NovusAevum/expense-tracker-app.svg?logo=git)](https://github.com/NovusAevum/expense-tracker-app/commits/main)
[![Stars](https://img.shields.io/github/stars/NovusAevum/expense-tracker-app.svg?style=social)](https://github.com/NovusAevum/expense-tracker-app/stargazers)
[![Forks](https://img.shields.io/github/forks/NovusAevum/expense-tracker-app.svg?style=social)](https://github.com/NovusAevum/expense-tracker-app/network/members)

</div>

---

## 🧭 Overview

**Expense Tracker** is a Django-based web application designed to provide clean user experience, real-time expense visualization with Chart.js, data import/export, and REST APIs.  
Built originally for **Rumi Press**, this project showcases full-stack implementation with MVC/MVT architecture and a continuous integration workflow for Python 3.11 + Django 5.x stack.

---

## 🌟 Features

| Category | Highlights |
|-----------|-------------|
| **Book Management** | Create, read, update, delete book entries |
| **Categorization** | Hierarchical category architecture |
| **Reporting** | Visual category-wise expense summaries |
| **Data Import/Export** | CSV Import / Excel & PDF Export (via xhtml2pdf, openpyxl) |
| **Authentication** | Login, logout, and Django Admin integration |
| **Visualization** | Real-time dynamic charts using Chart.js |
| **API Ready** | Full CRUD JSON endpoints (DRF integrated) |

---

## 🧱 Architecture

%%{init: {'theme':'neutral'}}%%
graph TD
A[User Interface] -->|HTTP Request| B[Views Controller]
B --> C[Django Models]
C --> D[(SQLite / PostgreSQL DB)]
B --> E[Templates (Bootstrap + HTML)]
E --> F[Chart.js Visualization]
G[REST Framework API] -->|JSON| B


---

## 🌀 Workflow

%%{init: {'theme':'forest'}}%%
sequenceDiagram
participant U as User
participant V as Django Views
participant M as Models / DB
participant T as Templates
U->>V: Request (Books, Reports, Categories)
V->>M: ORM Query (BookCategory, Book)
M-->>V: QuerySet (Data)
V->>T: Render (HTML + JS + Charts)
T-->>U: Response (Visualized Chart / Table)


---

## ⚙️ Installation & Setup (Quickstart)

### Prerequisites
- Python ≥ 3.8
- Git
- Django 5.x

### Commands

git clone https://github.com/NovusAevum/expense-tracker-app.git
cd expense-tracker-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8001


Visit:
- **Web App:** http://127.0.0.1:8001/books/  
- **Admin Panel:** http://127.0.0.1:8001/admin/  
- **Report:** http://127.0.0.1:8001/report/

---

## 📘 Usage

### Book CRUD
| Route | Description |
|--------|--------------|
| `/books/` | List all books |
| `/books/add/` | Create new book |
| `/books/<id>/edit/` | Edit a book |
| `/books/<id>/` | View book details |

### Category Management
| Route | Description |
|--------|--------------|
| `/categories/` | Manage categories |
| `/categories/add/` | Add category |

### Reports
| Route | Function |
|--------|----------|
| `/report/` | Expense visualization (Chart.js) |
| `/report/pdf/` | Export to PDF |
| `/report/excel/` | Export to Excel |

---

## 🧰 API Endpoints (via Django REST Framework)

| Method | Endpoint | Description |
|:-------|:----------|:-------------|
| GET | `/api/books/` | View all books |
| POST | `/api/books/` | Add new book |
| PUT/PATCH | `/api/books/<id>/` | Update book |
| DELETE | `/api/books/<id>/` | Delete entry |

---

## 📊 Directory Structure

expense-tracker-app/
├── books/
│ ├── admin.py
│ ├── api.py
│ ├── models.py
│ ├── urls.py
│ ├── views.py
│ └── templates/books/
│ ├── base.html
│ ├── book_list.html
│ ├── book_form.html
│ ├── book_detail.html
│ ├── category_list.html
│ ├── report.html
│ ├── report_pdf.html
│ └── category_form.html
├── expense_tracker/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── manage.py


---

## 🧠 Core Logic Highlights

- Class-based views (`ListView`, `CreateView`, `UpdateView`, `DetailView`)
- Django ORM with related models:
class BookCategory(models.Model):
name = models.CharField(max_length=100)
parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
class Book(models.Model):
title = models.CharField(max_length=200)
category = models.ForeignKey(BookCategory, on_delete=models.SET_NULL, null=True)
distribution_expenses = models.DecimalField(max_digits=10, decimal_places=2)

- Integrated chart rendering in `report.html`  
- API registered automatically with `DefaultRouter()`  
- Deployment ready with static/media directory separation.  

---

## 🔮 Future Enhancements

| Planned Feature | Description |
|-----------------|--------------|
| 🔍 Search & Filters | Integrated Django-filter module |
| 🔐 User Roles | Multi-auth and session isolation |
| 🧾 PDF Template Styling | Improved layouts for fiscal export |
| ☁️ Cloud Deployment | AWS / Render-ready configuration |
| 📸 Book Cover Upload | ImageField integration |
| 🧾 Auto Notifications | Email alerts on expense threshold exceedance |

---

## 🎨 Visual Demo

| Books Module | Expense Report | Category Listing |
|---------------|----------------|------------------|
| *(example screenshots can be added to docs/)* | *(Chart.js dynamic bar chart)* | *(Bootstrap layout for CRUD pages)* |

---

## 🧾 License
© 2025 — **Wan Mohamad Hanis Bin Wan Hassan (NovusAevum)**  
Licensed under *Educational / Showcase Use Only.*

---

## 👨‍💻 Credits

**Author:** [Wan Mohamad Hanis Bin Wan Hassan (WMH)](https://www.linkedin.com/in/wanmohamadhanis)  
**GitHub:** [NovusAevum](https://github.com/NovusAevum)  
**Platform:** Coursera Showcase Project  
**Security Focus:** [TryHackMe: wmhZeroSignal](https://tryhackme.com/p/wmhZeroSignal)

---

> “Crafted with precision, optimized for clarity, documented for mastery.”  
> — *WMH (NovusAevum)*

---
