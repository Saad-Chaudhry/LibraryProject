# LibraryProject

A Django application for managing a database of books and authors. Users can perform CRUD operations on book records, manage author details, and retrieve useful statistics through aggregation methods.

## Screenshots

![Screenshot 1](url_to_screenshot_1)
*Login Page*

![Screenshot 2](url_to_screenshot_2)
*Sign Up Page*

![Screenshot 3](url_to_screenshot_3)
*Library Home*

![Screenshot 4](url_to_screenshot_4)
*Books List*

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Saad-Chaudhry/LibraryProject.git
cd LibraryProject
```

### 2. Create Virtual Environment

```bash
python -m venv env
```

### 3. Activate Virtual Environment
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run the Application
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your web browser to access the application.
