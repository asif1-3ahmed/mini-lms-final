# Mini LMS Deployment Guide

## Railway Backend Setup

Your backend is deployed on Railway at:
https://mini-lms-final-production.up.railway.app/

### Required Environment Variables on Railway

Set these in your Railway project dashboard (Settings → Variables):

```
SECRET_KEY=your-random-secret-key-here
DEBUG=False
ALLOWED_HOSTS=mini-lms-final-production.up.railway.app
DATABASE_URL=<Railway provides this if you add PostgreSQL plugin>
CORS_ALLOWED_ORIGINS=https://mini-lms-a5e66.web.app,https://mini-lms-a5e66.firebaseapp.com
```

### Steps to Fix the 500 Error

1. **Add PostgreSQL to Railway** (recommended for production):
   - Go to your Railway project
   - Click "New" → Add Service → PostgreSQL
   - Railway will auto-set `DATABASE_URL`
   - Run migrations (Procfile has `release: python manage.py migrate`)

   OR use SQLite (simpler, not recommended for prod):
   - Don't add PostgreSQL; let it use SQLite

2. **Set Environment Variables**:
   - Dashboard → Variables
   - Add each variable above
   - Set `DEBUG=False` for production

3. **Check Logs**:
   - Dashboard → Logs
   - Look for migration errors or other issues
   - If you see "relation does not exist", migrations didn't run

4. **Redeploy**:
   - Make a small change and push (e.g., update a comment in settings.py)
   - Or click "Redeploy" in the dashboard
   - Watch logs for "Running release script" and "python manage.py migrate"

### Testing the API

Once deployed and logs are clean:

```powershell
# Test register endpoint
Invoke-WebRequest -Uri 'https://mini-lms-final-production.up.railway.app/api/auth/register/' `
  -Method Post `
  -Headers @{"Content-Type"="application/json"} `
  -Body '{"username":"test","email":"test@example.com","password":"testpass123","first_name":"Test"}'

# Test courses endpoint (no auth needed for GET)
Invoke-RestMethod -Uri 'https://mini-lms-final-production.up.railway.app/api/courses/' -Method Get
```

### Firebase Frontend

Your frontend is deployed at:
https://mini-lms-a5e66.firebaseapp.com

Environment variables in `frontend/.env.local`:
- `VITE_API_URL=https://mini-lms-final-production.up.railway.app/api` (auto-uses when `npm run build`)
- Firebase config is embedded in `src/firebase.js`

## Troubleshooting

**Problem**: 500 on `/api/auth/register/`
- **Cause**: Likely migrations not run or database not accessible
- **Fix**: Ensure PostgreSQL is added, migrations run in Procfile, logs show success

**Problem**: CORS "Network Error" in browser
- **Cause**: `CORS_ALLOWED_ORIGINS` doesn't match frontend origin
- **Fix**: Add exact frontend domain (e.g., `https://mini-lms-a5e66.web.app`)

**Problem**: Static files 404
- **Not needed**: Django serves API only; Firebase serves frontend

## Local Development

Run locally first to test:

```powershell
# Backend
cd backend
python manage.py migrate
python manage.py runserver

# Frontend (in another terminal)
cd frontend
npm run dev
```

Then visit `http://localhost:5173` and test the full flow.
