# QuickNote

A simple Django notebook/reminder app. Sign up, log in, write a note, save it, view all your notes, delete them when done.

## Features

- 🔐 Login required — sign up with just an email + password (no separate username). Each user only sees their own notes.
- 🌗 Light / dark mode toggle (top-right button, remembered between visits)
- 🅝 Simple single-letter "N" logo
- 📌 Notes shown as pinned sticky-note cards
- ✅ Saving a note takes you to a dedicated "Note saved!" confirmation page

## Setup

```bash
# 1. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations
python manage.py migrate

# 4. (Optional) create an admin account
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** in your browser. You'll be redirected to `/login/` — click **Sign up** to create your first account.

Admin panel: **http://127.0.0.1:8000/admin/**
