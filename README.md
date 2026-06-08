# 🎓 Face Attendance System using Computer Vision

## 📌 Overview

The Face Attendance System is an AI-powered attendance management application that automatically detects, recognizes, and records attendance using facial recognition technology. The system eliminates manual attendance tracking and provides a faster, more accurate, and secure method for attendance management.

The application uses Computer Vision and Machine Learning techniques to identify registered users in real time through a webcam and automatically generate attendance records.

---

## ✨ Features

* 👤 Face Registration and Dataset Creation
* 🎥 Real-Time Face Detection using OpenCV
* 🤖 Face Recognition using K-Nearest Neighbors (KNN)
* 📝 Automatic Attendance Recording
* 📊 Attendance Dashboard with Streamlit
* 🔊 Voice Confirmation for Attendance Marking
* 📅 Daily Attendance Report Generation
* 💾 Local Data Storage using Pickle Files

---

## 🛠 Technologies Used

* Python
* OpenCV
* NumPy
* Pandas
* Scikit-learn
* Streamlit
* Pickle
* Haar Cascade Classifier

---

## 📂 Project Structure

```text
face-attendance-system/
│
├── app.py
├── add_face.py
├── test.py
├── bgNew.png
├── README.md
├── requirements.txt
│
├── data/
│   ├── haarcascade_frontalface_default.xml
│
├── Attendance/
│   └── Attendance_DD-MM-YY.csv
│
└── screenshots/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/face-attendance-system.git
cd face-attendance-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Step 1: Register a New Face

Run:

```bash
python add_face.py
```

Enter the user's name and capture face images using the webcam.

---

### Step 2: Start Attendance System

Run:

```bash
python test.py
```

The system will:

* Detect faces
* Recognize registered users
* Mark attendance automatically
* Save attendance records in the Attendance folder

---

### Step 3: View Attendance Dashboard

Run:

```bash
streamlit run app.py
```

The dashboard displays attendance records in an organized format.

---

## 📊 Attendance Output

Attendance is stored in CSV format:

```text
Attendance/
└── Attendance_DD-MM-YY.csv
```

Example:

| Name       | Time     |
| ---------- | -------- |
| Chan  | 08:30:15 |
| Ben   | 08:35:42 |

---

## 🔒 Privacy Notice

This project stores facial data locally using Pickle files.

Before publishing or sharing the project:

* Exclude personal attendance records
* Exclude generated face datasets
* Exclude sensitive user information

Recommended `.gitignore` entries:

```text
Attendance/*.csv
data/face_data.pkl
data/names.pkl
```

---

## 🔮 Future Improvements

* Database Integration (MySQL/PostgreSQL)
* Face Recognition using Deep Learning (FaceNet)
* Cloud-Based Attendance Storage
* Admin Login System
* Attendance Analytics Dashboard
* Email Attendance Reports
* Mobile Application Integration

---

## 🎯 Learning Outcomes

This project demonstrates practical experience in:

* Computer Vision
* Machine Learning
* Facial Recognition
* Data Processing
* Streamlit Application Development
* Real-Time Video Processing
* Attendance Automation

---

## 👨‍💻 Author

**Chanuuj Navaretnam**

Information and Communication Technology Undergraduate
Uva Wellassa University of Sri Lanka

* GitHub: https://github.com/N-Chanuuj-NC
* LinkedIn: https://www.linkedin.com/in/chanuuj-navaretnam-b117683a9

---

⭐ If you found this project useful, consider giving it a star on GitHub.
