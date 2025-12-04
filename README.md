# 📌 **Project Title: Django CRM System**

A simple Customer Relationship Management (CRM) web application built using Django.
The system allows users to register, log in, add customer records, update them, and delete them.

## 🚀 **Features**

* User Registration
* User Login / Logout
* Add New Record
* View All Records
* View Record Details
* Update Record
* Delete Record
* MySQL Database Integration
* Bootstrap UI


## 🛠 **Tech Stack**

| Technology       | Purpose         |
| ---------------- | --------------- |
| **Python 3**     | Backend logic   |
| **Django**       | Web framework   |
| **MySQL**        | Database        |
| **Bootstrap 5**  | UI styling      |
| **HTML / CSS**   | Templates       |
| **Git & GitHub** | Version control |


## ⚙️ **Installation & Setup**

### **1. Clone the project**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### **2. Create a virtual environment**

```bash
python -m venv venv
```

### **3. Activate the virtual environment**

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### **4. Install dependencies**

```bash
pip install -r requirements.txt
```

### **5. Create MySQL Database**

```sql
CREATE DATABASE dbname;
```

Update settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbname',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### **6. Run migrations**

```bash
python manage.py migrate
```

### **7. Start server**

```bash
python manage.py runserver
```


## 👤 **User Authentication**

* Only authenticated users can add, update, or delete records
* Unauthenticated users can only see the login page
* Login logic uses Django's built-in authentication system

## 🎯 **How It Works (Short Explanation)**

* Users log in using Django authentication
* MySQL stores user and record data
* Bootstrap makes the UI clean and responsive
* CRUD operations allow managing customer records easily
* Messages framework shows success/error notifications

## 🤝 **Contributing**

Pull requests are welcome.


## 📄 **License**

This project is open source.
(Use MIT License if you want.)
Do you want me to prepare the final polished README for you?
