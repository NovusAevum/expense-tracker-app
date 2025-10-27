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
