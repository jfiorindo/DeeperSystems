# DeeperSystems - Full Stack CRUD (Vue 3 + Flask + MongoDB)

Hi! This is a full stack CRUD project I developed using Vue.js 3 (Composition API) for the frontend, Flask for the backend, and MongoDB for the database. The interface is built with PrimeVue components to make everything look clean and user-friendly.

I used resources like YouTube, ChatGPT, and Google to help me with parts of the implementation and learning process during the development.

---

## Technologies Used

- Frontend: Vue.js 3, Vite, PrimeVue
- Backend: Flask, PyMongo
- Database: MongoDB
- UI Components: PrimeVue
- Tools used to learn and build: YouTube, ChatGPT, Google

---

## How to Run the Project (Recommended - Windows)

To make it easier to run, I included a `.bat` file that starts both the backend and the frontend automatically.

### Quick Start:

1. Double-click `start_project.bat` in the root folder.
2. This will open:
   - One terminal running the backend (Flask) on `http://localhost:5000`
   - Another terminal running the frontend (Vue.js) on `http://localhost:5173`
3. Open your browser and go to `http://localhost:5173` to use the app.

---

## Manual Setup (Alternative)

If needed, here’s how to run everything manually.

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python parser.py   # Imports users from users.json to MongoDB
python app.py      # Starts Flask API on port 5000
```

### Frontend

```bash
cd frontend
npm install
npm run dev        # Starts Vue app on port 5173
```

---

## About the Database

This project uses a local MongoDB connection:

- Database name: `deeper_db`
- Collection: `users`

The `parser.py` script loads the initial user data from `users.json` and inserts it into the database.

Make sure MongoDB is running locally on the default port: `mongodb://localhost:27017`

---

## Features

- Data import from JSON
- Full CRUD functionality (Create, Read, Update, Delete)
- Role-based users (admin, manager, tester)
- Status handling (active/inactive)
- User interface with modals, confirmation dialogs and tags
- Clean and responsive layout using PrimeVue

---

## Project Structure

```
Test_DeeperSystems/
├── backend/
│   ├── app.py
│   ├── parser.py
│   ├── users.json
│   ├── venv/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
├── start_project.bat
└── README.md
```

---

## Notes

- Tested on Windows 10+ with Python 3.10+ and Node.js 18+
- If anything goes wrong, check the terminal output for error messages.
- I built this as part of a practical test challenge using online resources and tools to support my learning.

---

Made by João Pedro Fiorindo Pinto
