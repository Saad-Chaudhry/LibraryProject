# LibraryProject

A Django application for managing a database of books and authors. Users can perform CRUD operations on book records, manage author details, and retrieve useful statistics through aggregation methods.

## Screenshots

![Screenshot 1](https://drive.google.com/file/d/1EEE1tw4d5FBKNoXX9IZ2Mw535Ztuv88O/view?usp=sharing)
*Login Page*

![Screenshot 2](https://drive.google.com/file/d/1IgVvElR6iNUII1UIzTi-mIueDoPxBjLW/view?usp=sharing)
*Sign Up Page*

![Screenshot 3](https://drive.google.com/file/d/1pkW6vrhuvBVeJ4hmz4qmG--vToBW3N3j/view?usp=sharing)
*Library Home*

![Screenshot 4](https://drive.google.com/file/d/1POxn479AgBHiQ4CVIPUTEye1YnpCHOMy/view?usp=sharing)
*Books List*

![Screenshot 5](https://drive.google.com/file/d/1XI-FCGRJhPQG8IB72G1kdrn5rShjobbx/view?usp=sharing)
*Aggregation Methods*

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

## Author

- [@Saad-Chaudhry](https://github.com/Saad-Chaudhry)
