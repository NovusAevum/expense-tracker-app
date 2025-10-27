
<!-- ===================================================================== -->
<!--   EXPENSE TRACKER APP - BY WAN MOHAMAD HANIS                          -->
<!-- ===================================================================== -->

<div align="center">

# 📊 Expense Tracker App (Django)

_“A modern, analytics-focused Django application for tracking book distribution expenses and inventory metrics.”_

[![Django](https://img.shields.io/badge/Django-5.2.7-blue?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-lightblue?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](#license)
[![GitHub last commit](https://img.shields.io/github/last-commit/NovusAevum/expense-tracker-app.svg?logo=git)](https://github.com/NovusAevum/expense-tracker-app/commits/main)
![Status](https://img.shields.io/badge/Status-Active-success)
![Built With 💚 by WMH](https://img.shields.io/badge/Built%20With-%F0%9F%92%9A%20by%20WMH-success)

</div>

---

## 🧭 Overview

This **Expense Tracker App** is a fully functional **Django web application** that allows tracking of book expenses, categorization, reporting, and visualization — tailored for **Rumi Press** as a Coursera showcase project.  

It demonstrates **real-world engineering principles**, including REST APIs, ORM logic, CSV ingestion automation, and Chart.js frontend integration.

---

## 🌐 Live Representation  
> [GitHub Repository → Expense Tracker App](https://github.com/NovusAevum/expense-tracker-app)

---

## 🌟 Features

| Feature | Capability |
|----------|-------------|
| **Book Management** | CRUD operations for book entries (with details like author, price, date, and category). |
| **Category Hierarchies** | Establish parent-child category relationships dynamically. |
| **Expense Analytics** | Category-wise total expense tracking with Chart.js reports. |
| **CSV Importer** | Bulk upload data for operational efficiency. |
| **Report Exporting** | Generate expense summaries in PDF & Excel formats. |
| **Authentication Layer** | Django-based login, logout, access control. |
| **REST API** | Light-weight API endpoints using Django REST Framework. |

---

## 🧩 Tech Stack & Integrations

| Layer | Technology |
|:------|:------------|
| Backend | Django 5.2.7, Python 3.11 |
| Frontend | HTML5, Bootstrap 5.3.2, Chart.js |
| Database | SQLite (plug-and-play) |
| Additional Libraries | xhtml2pdf, django-filter, openpyxl |
| Versioning | Git + GitHub |
| Deployment | Render / Vercel / PythonAnywhere ready |

---

## 🧱 Architecture


graph TD
A[User Interface / Browser] -->|HTTP Request| B(Views - Django CBVs)
B --> C[Models (Book, BookCategory)]
C --> D[(SQLite Database)]
B --> E[Template Engine (Jinja2)]
E --> F[Chart.js Data Visualization]
G[REST Framework] --> B
text

---

## 🌀 System Workflow


sequenceDiagram
participant U as User
participant D as Django
participant DB as SQLite
participant API as DRF Endpoint
text
U->>D: Request Dashboard (/books/)
D->>DB: Query Book & Category Tables
DB-->>D: Result Set (JSON/QuerySet)
D-->>U: Render HTML + Chart Data
U->>API: GET /api/books/
API->>D: Serve RESTful JSON Response

text

---

## ⚙️ Installation

### Prerequisites
- Python 3.8+
- Git installed
- Virtual environment configured

### Commands (Copy-Paste)


git clone https://github.com/NovusAevum/expense-tracker-app.git
cd expense-tracker-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8001
text

Access the application:
- 📚 http://127.0.0.1:8001/books/
- 🏛 http://127.0.0.1:8001/admin/
- 📈 http://127.0.0.1:8001/report/

---

## 📘 Usage

### Manage Data
- **Add books:** `/books/add/`
- **Track expenses:** `/report/`
- **Manage users:** `/admin/`
- **View JSON:** `/api/books/`

### Export Reports

/report/pdf/ → PDF Export
/report/excel/ → Excel Export
text

---

## 🧭 Directory Structure


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
│ └── report_pdf.html
├── expense_tracker/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── manage.py

---

## 📊 API Overview

| Method | Endpoint | Description |
|:--------|:----------|:-------------|
| GET | `/api/books/` | Retrieve all books |
| POST | `/api/books/` | Create a book |
| PUT | `/api/books/<id>/` | Update a book |
| DELETE | `/api/books/<id>/` | Delete a book |

---

## 🎨 Theming & UX

📌 Integrated with **Bootstrap 5** (light/dark switch ready via CSS Variables).  
📈 Charts rendered dynamically using **Chart.js responsive canvas**.  

Want Dark Mode? Toggle provided in navbar on all templates extending `base.html`.

---

## 🔮 Future Enhancements

| Feature | Description |
|----------|--------------|
| 🔍 Search Filter | Advanced search powered by `django-filter`. |
| 🔐 Multi-user Access | Multi-login roles with permissions. |
| 📤 Export CSV | Export records in bulk. |
| 🧾 DRF JWT Auth | Authenticated REST endpoints. |
| 🖼 File Management | Add book cover image uploads. |
| 📧 Notifications | Auto email alerts for low stock. |

---

## 🧠 Learning Outcomes

- Working knowledge of Django ORM and CBVs  
- Template Inheritance + Bootstrap composition  
- API design fundamentals (CRUD architecture)  
- Handling static & media content efficiently  
- Integrating data visualization for insights  

---

## 🤝 Contributing

Contributions are open for pull requests.  

🔥 Enhancement ideas? Open an **Issue** on [GitHub](https://github.com/NovusAevum/expense-tracker-app/issues).

---

## 🧾 License

Licensed under Educational Use © 2025 — *Wan Mohamad Hanis Bin Wan Hassan*.  
Created as part of coursework and personal portfolio development.

---

## 👨‍💻 Author & Maintainer

**Wan Mohamad Hanis Bin Wan Hassan (WMH)**  
👔 [LinkedIn](https://www.linkedin.com/in/wanmohamadhanis)  
🧠 [GitHub](https://github.com/NovusAevum)  
🎓 [Coursera Profile](https://www.coursera.org/learner/triumphanthanis)  
💬 [TryHackMe](https://tryhackme.com/p/wmhZeroSignal)

---

## 🪶 Acknowledgments

- Django Official Documentation  
- Bootstrap Framework  
- Coursera Showcase Lab  
- Chart.js for financial visualizations  

---

<div align="center">

> _“Built with precision. Crafted with intention. Documented for clarity.”_  
> — **WMH (NovusAevum)**

</div>

---












# 📚 Expense Tracker App (Django)

A full-featured Django web application for tracking book inventory, expenses, and categories. Originally designed to automate book distribution tracking for Rumi Press, this project demonstrates proficiency in Django MVC architecture, database design, CRUD operations, and modern web development practices.

## 🌟 Features

### Core Functionality
- **Book Management**: Complete CRUD operations for book entries with title, author, price, quantity, and publication date
- **Category System**: Organize books into hierarchical categories with parent-child relationships
- **Expense Tracking**: Monitor spending across different book categories
- **Reporting Dashboard**: Generate category-wise expense reports with totals and summaries
- **CSV Import**: Bulk import book data from CSV files using custom management commands
- **Admin Interface**: Full Django admin integration for backend management

### Technical Highlights
- Clean Django MVT (Model-View-Template) architecture
- SQLite database with proper migrations
- Bootstrap 5 responsive UI design
- Form validation and error handling
- RESTful URL patterns
- Template inheritance for DRY principles

## 🛠️ Technology Stack

- **Backend**: Python 3.8+, Django 5.2.7
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Version Control**: Git/GitHub

## 📋 Project Structure

```
expense-tracker-app/
├── books/                      # Main Django app
│   ├── migrations/            # Database migrations
│   ├── templates/books/       # HTML templates
│   │   ├── book_list.html     # Book listing page
│   │   ├── book_detail.html   # Book detail view
│   │   ├── book_form.html     # Book create/edit form
│   │   ├── category_list.html # Category listing
│   │   ├── category_form.html # Category form
│   │   └── report.html        # Expense reporting
│   ├── models.py              # Data models (Book, BookCategory)
│   ├── views.py               # View controllers
│   ├── urls.py                # URL routing
│   └── admin.py               # Admin configuration
├── expense_tracker/           # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configuration
│   └── wsgi.py                # WSGI configuration
├── import_books.py            # CSV import utility
├── manage.py                  # Django management script
├── db.sqlite3                 # SQLite database
└── README.md                  # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NovusAevum/expense-tracker-app.git
   cd expense-tracker-app
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   # Or if requirements.txt exists:
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser account** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set username, email, and password.

6. **Start development server**
   ```bash
   python manage.py runserver 8001
   ```

7. **Access the application**
   - Main app: http://127.0.0.1:8001/books/
   - Admin panel: http://127.0.0.1:8001/admin/
   - Categories: http://127.0.0.1:8001/categories/
   - Reports: http://127.0.0.1:8001/reports/

## 📖 Usage Guide

### Managing Books
1. Navigate to `/books/` to view all books
2. Click "Add New Book" to create entries
3. Click on any book title to view details
4. Use "Edit" to modify book information
5. Use "Delete" to remove books (with confirmation)

### Managing Categories
1. Navigate to `/categories/` to view all categories
2. Click "Add New Category" to create categories
3. Assign parent categories to create hierarchies
4. Edit or delete categories as needed

### Generating Reports
1. Navigate to `/reports/` to view expense summaries
2. See category-wise book counts and total values
3. Analyze spending patterns across categories

### Importing Data
Use the custom import script to bulk-load book data:
```bash
python import_books.py
```

### Admin Interface
1. Access `/admin/` and log in with superuser credentials
2. Full access to all models and database entries
3. Advanced filtering, searching, and bulk operations

## 🗃️ Database Models

### BookCategory Model
```python
class BookCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, 
                              on_delete=models.CASCADE, 
                              related_name='subcategories')
```

### Book Model
```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(BookCategory, on_delete=models.SET_NULL, 
                                 null=True, related_name='books')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    publication_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## 🎯 Key Learning Outcomes

This project demonstrates proficiency in:

1. **Django Framework**
   - Models, Views, Templates (MVT) architecture
   - ORM for database operations
   - Django forms and validation
   - URL routing and reverse lookups
   - Template inheritance and filters

2. **Database Design**
   - Relational database modeling
   - Foreign key relationships
   - Self-referential relationships (parent categories)
   - Database migrations

3. **Web Development**
   - RESTful design patterns
   - CRUD operations
   - Form handling and validation
   - Responsive UI with Bootstrap
   - User-friendly navigation

4. **Software Engineering**
   - Version control with Git
   - Code organization and modularity
   - DRY (Don't Repeat Yourself) principles
   - Documentation and README best practices

## 🔮 Future Enhancements

### Planned Features
- [ ] **Data Visualization**: Integrate Chart.js for interactive expense charts and graphs
- [ ] **Search & Filtering**: Advanced search with filters by category, author, date range
- [ ] **User Authentication**: Multi-user support with permissions and user-specific data
- [ ] **Export Functionality**: Export reports to PDF and Excel formats
- [ ] **API Development**: Build RESTful API using Django REST Framework
- [ ] **Pagination**: Implement pagination for large book lists
- [ ] **File Uploads**: Support for book cover images
- [ ] **Email Notifications**: Alert users for low inventory or new additions

### Deployment Strategy
- [ ] Deploy to **PythonAnywhere** for free hosting
- [ ] Alternative: **Heroku** with PostgreSQL database
- [ ] Alternative: **Railway** or **Render** for modern cloud deployment
- [ ] Configure PostgreSQL for production database
- [ ] Set up static file serving with WhiteNoise or AWS S3
- [ ] Implement environment variables for secrets management
- [ ] Add custom domain and SSL certificate

## 🧪 Testing

To run the development server and test functionality:
```bash
python manage.py runserver 8001
```

Manual testing checklist:
- ✅ Create, read, update, delete books
- ✅ Create, read, update, delete categories
- ✅ View reports with accurate calculations
- ✅ Import books from CSV
- ✅ Admin panel accessibility
- ✅ Form validation and error messages
- ✅ Responsive design on mobile/tablet

## 📝 Development Notes

### Recent Updates (Latest Commit)
- Finalized CRUD templates with consistent navigation
- Improved Bootstrap styling across all pages
- Added category hierarchy support
- Enhanced report generation functionality
- Implemented proper form validation

### Known Issues
- Root URL (/) returns 404 - intentional, direct users to /books/ or /categories/
- CSV import requires specific format - see import_books.py for structure

## 👨‍💻 Author

**Wan Mohamad Hanis Bin Wan Hassan**
- GitHub: [@NovusAevum](https://github.com/NovusAevum)
- Project: [expense-tracker-app](https://github.com/NovusAevum/expense-tracker-app)

## 📄 License

This project is created for educational purposes as part of coursework and portfolio development.

## 🙏 Acknowledgments

- Built as part of web development coursework
- Inspired by real-world inventory management needs
- Uses Django's excellent documentation and community resources
- Bootstrap framework for responsive UI components

---

**Note**: This is a development project intended for portfolio demonstration and educational assessment. For production deployment, additional security configurations and environment-specific settings should be implemented.
