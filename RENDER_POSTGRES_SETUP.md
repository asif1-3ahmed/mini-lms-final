# Render PostgreSQL Setup Guide

## You've added PostgreSQL on Render ✓

Now connect your Django backend to it:

### Step 1: Get the Database URL from Render

1. Go to your Render dashboard → PostgreSQL service
2. Copy the **Internal Database URL** (looks like: `postgresql://user:pass@host:5432/dbname`)
   - Use "Internal" URL if your backend is also on Render (faster, no internet)
   - Use "External" URL if backend is elsewhere

### Step 2: Set Environment Variables on Render (Backend Service)

1. Go to your **backend service** on Render (where Django is deployed)
2. Click **Environment** (or Settings → Environment Variables)
3. Add:
   ```
   DATABASE_URL=postgresql://user:pass@host:5432/dbname
   SECRET_KEY=your-random-long-string
   DEBUG=False
   ALLOWED_HOSTS=your-backend-domain.onrender.com
   CORS_ALLOWED_ORIGINS=https://mini-lms-a5e66.web.app,https://mini-lms-a5e66.firebaseapp.com
   ```

### Step 3: Redeploy

- Click **Redeploy** on your backend service
- Watch the logs for:
  - `Running release script...`
  - `python manage.py migrate` (should run successfully)
  - `Starting gunicorn...` (server starts)

### Step 4: Check Logs

If you see errors:
- **"relation does not exist"** → migrations didn't run
  - Make sure Procfile has: `release: python manage.py migrate`
  - Check that `DATABASE_URL` is set and correct
- **Connection refused** → DATABASE_URL format is wrong or server is down
- **"IntegrityError"** → data conflict (safe to delete db and remigrate)

### Step 5: Test the API

```powershell
# Replace YOUR_BACKEND_URL with your Render backend domain
$BASE_URL = "https://your-backend.onrender.com/api"

# Test register
Invoke-WebRequest -Uri "$BASE_URL/auth/register/" `
  -Method Post `
  -Headers @{"Content-Type"="application/json"} `
  -Body '{"username":"testuser","email":"test@example.com","password":"pass123","first_name":"Test"}'

# Test courses list
Invoke-WebRequest -Uri "$BASE_URL/courses/" -Method Get
```

## Local Testing (Optional)

Test locally first to catch errors early:

```powershell
# Set env var temporarily
$env:DATABASE_URL = "postgresql://user:pass@localhost:5432/mini_lms"

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

Then visit `http://localhost:8000/api/` to verify.

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| 500 on `/api/auth/register/` | Migrations not run / DB not accessible | Check Procfile, logs, DATABASE_URL |
| CORS "Network Error" | Origin not in CORS_ALLOWED_ORIGINS | Add frontend origin to env var |
| 502 Bad Gateway | Backend crashed | Check Render logs for Python errors |
| "relation auth_user does not exist" | Migrations didn't run | Check if `release` phase executed in Procfile |

## Your Current Setup

- **Backend**: Render (Django + Gunicorn)
- **Database**: PostgreSQL on Render
- **Frontend**: Firebase Hosting (React + Vite)
- **Storage**: Firebase Cloud Storage (videos)
- **Auth**: JWT tokens (60 min access, 7 day refresh)

Everything is connected — once DATABASE_URL is set and migrations run, the app will work! 🚀
