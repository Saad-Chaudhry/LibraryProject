# LibraryProject

A Django application for managing a database of books and authors. Users can perform CRUD operations on book records, manage author details, and retrieve useful statistics through aggregation methods.

## Screenshot

#### Book List
![Screenshot](https://i.ibb.co/5rMR7YQ/Screenshot-2023-12-22-023030.png)


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

### 6. Create Super User
##### Username: saad
##### Password: saad
```bash
python manage.py createsuperuser
```

### 7. Run the Application
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your web browser to access the application.

## Author

- [@Saad-Chaudhry](https://github.com/Saad-Chaudhry)
