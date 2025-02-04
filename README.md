[README.md](https://github.com/user-attachments/files/18657355/README.md)
# ArtCode's Creations - Health & Fitness Tracker

## 📌 Project Overview

The **Health & Fitness Tracker** is a Python-based application that helps users track their health and fitness progress. It integrates **MySQL, CSV files, text files, YouTube API, and email services** to provide a seamless experience. Users can:

- Register and authenticate securely
- Set fitness goals
- Track workout progress
- Receive daily workout recommendations via email
- Get motivational quotes
- Analyze progress with **data visualization**

---

## ✨ Features

✔ **User Authentication** – Secure login & password management  
✔ **Profile Management** – Stores user info securely in a CSV file  
✔ **Activity Tracking** – Logs workouts & daily habits in MySQL  
✔ **Nutrition Ideas** – Fetches personalized YouTube nutrition videos  
✔ **Goal Setting** – Helps users set & achieve fitness goals  
✔ **Workout Plans** – Stores pre-defined workout plans in MySQL  
✔ **Data Privacy & Security** – Ensures secure storage of user data  
✔ **Analytics & Graphs** – Visualizes progress using Matplotlib  

---

## 🛠 Technologies Used

- **Programming Language**: Python
- **Backend**: MySQL, CSV Files, Text Files
- **Libraries & Modules**: `tkinter`, `pandas`, `matplotlib`, `pytube`, `urllib`, `smtplib`

---

## 📂 Modules Overview

This project is built using **19 core modules**, each handling a specific task:

| Module                  | Purpose |
|-------------------------|---------|
| `secrets`               | Generates cryptographically secure random numbers & passwords |
| `os`                    | Provides functions for file operations and directory handling |
| `string`                | Generates passwords using ASCII characters, digits, and punctuation |
| `csv`                   | Reads and writes CSV files for user data storage |
| `verify_email`          | Verifies email addresses for authentication purposes |
| `mysql.connector`       | Connects and interacts with the MySQL database |
| `email.message`         | Structures and sends email messages |
| `ssl`                   | Ensures secure SSL connections for emails |
| `smtplib`               | Sends emails using SMTP protocol |
| `random`                | Selects random motivational quotes from a text file |
| `datetime`              | Manages date and time operations for database entries |
| `re`                    | Uses regular expressions to extract YouTube video IDs |
| `urllib.request`        | Opens and fetches YouTube search results HTML content |
| `pytube`                | Interacts with YouTube videos for fetching metadata |
| `webbrowser`            | Opens selected YouTube videos in the default browser |
| `tkinter`               | Builds the graphical user interface (GUI) for the application |
| `pandas`                | Structures MySQL data into DataFrames for analysis |
| `matplotlib.pyplot`     | Visualizes user consistency graphs (sleep & water intake) |

---

## 🔧 Installation & Setup

### 1️⃣ Prerequisites

- Install **Python 3.11**
- Install **MySQL Workbench**
- Install required dependencies:
  ```sh
  pip install mysql-connector-python pandas matplotlib pytube urllib3
  ```

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/YourUsername/ArtCode-Creations.git
cd ArtCode-Creations
```

### 3️⃣ Configure Database

- Open **MySQL Workbench** and create databases for different fitness goals.
- Import `users.csv` for authentication management.

### 4️⃣ Run the Application

```sh
python main.py
```

---

## 📊 How to Use

1️⃣ **Sign Up/Login** using a unique username & auto-generated password.  
2️⃣ **Set Your Fitness Goal** (Weight Loss, Strength Training, etc.).  
3️⃣ **Track Your Workouts** – Data is stored in MySQL.  
4️⃣ **Get Motivational Quotes & Nutrition Ideas**.  
5️⃣ **Visualize Your Progress** using graphs.  
6️⃣ **Logout** – Securely removes your session.  

---

## 🔮 Future Improvements

🚀 **Web/App Integration** – Convert into a mobile/web app  
🚀 **Dynamic Workout Plans** – Allow users to customize routines  
🚀 **Mobile Compatibility** – Track steps & distances  
🚀 **API Integration** – Expand functionality with external fitness APIs  

---

## 📜 License

This project is **open-source**. Feel free to use, modify, and contribute!

---

## 📩 Contact

🔹 **Developer**: ArtCode  
🔹 **Email**: mj.priyadarshini0207@gmail.com
🔹 **GitHub**: GOLDEN-TOPEZ-RUBY

---

🔥 *Stay fit, stay motivated!* 🔥
