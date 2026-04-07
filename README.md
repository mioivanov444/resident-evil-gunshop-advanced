# Resident Evil Gunshop ADVANCED

A full-stack Django web application that catalogs firearms featured in Resident Evil games and their real-life counterparts.
The project demonstrates advanced Django concepts, REST API integration, authentication, and deployment.
---

## 🌐 Live Demo
https://resident-evil-gunshop-advanced.onrender.com

## 📂 Project Structure

- **core/** — home page, base templates, general views
- **guns/** — Gun & Category models, CRUD operations, API endpoints
- **reviews/** — review system linked to guns
- **users/** — authentication, registration, permissions
- **media/** — uploaded images
- **static/** — static files (CSS, images, icons)
- **templates/** — Django templates with inheritance
- **residentevil_gunshop/** — project settings and configuration

---

## 🛠️ Technologies

- Python 3.12  
- Django 6.x  
- PostgreSQL  
- Bootstrap 5.3 for styling  
- Pillow (for image uploads)
- Django REST Framework
- Render (deployment)

---

## 💾 Setup Instructions

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd residentevil_gunshop
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## 🗄️ Database Setup (PostgreSQL Required)

This project uses PostgreSQL as required by the assignment.

1. Make sure PostgreSQL is installed and running.
2. Create a database:
   ```bash
   createdb residentevil_gunshop
   ```
3. If required, update the DATABASE settings in settings.py to match your PostgreSQL username and password (username/password is postgres/postgres by default).


4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create a superuser** (Optional)

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

7. **Open http://127.0.0.1:8000/ in your browser.**


8. **Add Guns/Categories to your database through their respective pages**

***Note: I recommend adding your categories first, so that they may appear when adding/editing a gun. After this you can also freely edit and delete your guns/categories.***

## 🔐 Authentication & Permissions
- Users can register, log in, and log out
- Authenticated users can:
  - Add, edit, and delete guns and categories
  - Create reviews
- Anonymous users can browse the site and view content

## 🔌 REST API

The project includes RESTful API endpoints using Django REST Framework:

**Guns**
- GET /api/guns/ — list all guns
- GET /api/guns/<slug>/ — gun details

**Categories**
- GET /api/categories/
- GET /api/categories/<slug>/

**Email**
- POST /api/send-email/

## 🔹 Features

- Full CRUD functionality for **Guns**, **Reviews** and **Categories**
- Categorized guns with **many-to-many relationships**
- Search guns by **name** or **game**
- Responsive layout using **Bootstrap 5**
- **Images** for guns (a ready-to-go sample of images will be located in the **media/guns** directory, ready for use.)
- Custom **404 page**
- Navigation with consistent **header/footer**
- **Edit/Delete** functionality for guns and reviews

## ⚡ Asynchronous Processing

Originally implemented with Celery + Redis, but simplified for deployment:

- Email sending is currently handled synchronously
- This ensures compatibility with Render’s free tier (no background workers required)

## 🧪Tests
Includes 15 automated tests
Covers:
- Models
- Authentication
- Views
- API endpoints

Run tests with:

python manage.py test


## 🚀 Deployment (Render)
- Hosted on Render (free tier)
- Uses PostgreSQL database
- Static files handled with collectstatic

---

## 📋 Notes

- All environment variables and credentials required for local testing are included in the project defaults; no additional configuration is needed for local testing.
- Gun images can be uploaded via the **admin panel** or the **Gun edit/add page**.
- The site is fully functional without authentication, as per project requirements.

---

## ⚡ License / Disclaimer

This project is for **educational purposes**.  
No copyrighted material has been copied, and all code is original.