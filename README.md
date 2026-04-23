# 🎓 Student Registration System (Python + Tkinter + MySQL)

A **fully functional desktop-based Student Registration System** built using **Python (Tkinter GUI)** and **MySQL database**.  
This application allows users to **add, update, delete, search, and manage student records efficiently** with an interactive graphical interface.

---

## 📌 Project Overview

This system is designed to simplify student data management in educational institutions.  
It provides a **user-friendly interface** and ensures smooth database operations.

---

## ✨ Features

✅ Add new student records  
✅ Update existing student details  
✅ Delete student records  
✅ Search students by:
- Enrollment
- Name
- Phone  

✅ View all student records in a table  
✅ Scrollable modern GUI  
✅ Responsive full-screen layout  
✅ MySQL database integration  

---

## 🖼️ Project Preview

### 🔹 Main UI
![UI](assets/UI.png)

### 🔹 Student Registration Form
![Register](assets/register.png)

### 🔹 Database View
![Database](assets/database.png)

---

## 🏗️ Tech Stack

- **Frontend:** Tkinter (Python GUI)
- **Backend:** Python
- **Database:** MySQL
- **Libraries Used:**
  - tkinter
  - ttk
  - PIL (Pillow)
  - mysql-connector-python

---

## 📂 Project Structure

```bash
student-registration-system/
│── assets/
│   ├── UI.png
│   ├── register.png
│   ├── database.png
│
│── college_images/
│   ├── mits.png
│   ├── university.png
│   ├── 5th.jpeg
│
│── main.py
│── requirements.txt
│── README.md
```

## ⚙️ Installation & Setup

### 🔹 1. Clone Repository
```bash
git clone https://github.com/hamzamehmoodkhan1245/Student-Registration-System.git
cd Student-Registration-System

2. Install Dependencies
pip install -r requirements.txt

3. Setup MySQL Database

Open MySQL and run:
CREATE DATABASE student_management_system;

USE student_management_system;

CREATE TABLE student (
    Enrollment VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(100),
    Course VARCHAR(50),
    Department VARCHAR(100),
    Year VARCHAR(50),
    Semester VARCHAR(50),
    Section VARCHAR(50),
    Gender VARCHAR(20),
    DOB VARCHAR(50),
    Phone VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(255)
);

🔹 4. Update Database Credentials
host="localhost"
username="root"
password="YOUR_PASSWORD"
database="student_management_system"

🔹 5. Run the Application
python main.py

## 🧠 How It Works

- Built using **Tkinter GUI** with a scrollable layout  
- Uses **MySQL database** for data storage  

### 🔄 CRUD Operations

- **Insert** → Add new student  
- **Select** → Fetch and display data  
- **Update** → Modify existing records  
- **Delete** → Remove student records  

### 📊 Data Display

- Records are displayed using the **TreeView table widget**

## 🔍 Key Functional Modules

### ➤ Student Registration
- Input student details  
- Save data into database  

### ➤ Data Management
- Update existing records  
- Delete records with confirmation  

### ➤ Search System
- Dynamic filtering using SQL `LIKE`  

### ➤ Data Display
- Table view with horizontal & vertical scrolling  

## 🚀 Future Improvements

- 🔐 Add login authentication system  
- 📊 Export data to CSV/Excel  
- 🖼️ Add image upload for students  
- 🌐 Convert into a web-based app (Django/React)  
- 🤖 Add AI-based analytics  

## 👨‍💻 Author

**Hamza  Haroon**  

📧 Email: hamzamehmoodkhan1245@gmail.com  
🔗 GitHub: https://github.com/hamzamehmoodkhan1245  

---

## ⭐ Support

If you like this project:

- ⭐ Star this repository  
- 🍴 Fork it  
- 🧠 Contribute improvements  

---

## 💡 Final Note

This project demonstrates a complete **Student Registration System** using Python (Tkinter) and MySQL, showcasing real-world CRUD operations, GUI design, and database integration.  
It is ideal for **academic submissions, portfolio projects, and practical learning**.

---

## 📦 requirements.txt

```txt
pillow
mysql-connector-python
