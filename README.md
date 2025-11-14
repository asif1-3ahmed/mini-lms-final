# Mini LMS - Learning Management System

A full-stack Learning Management System built with Django REST Framework and React with Vite.

## Features

- **User Authentication**: JWT-based authentication with admin and student roles
- **Course Management**: Create, view, and manage courses (admin only)
- **Video Upload**: Upload and stream videos using Firebase Storage
- **Quiz System**: Create and take quizzes with instant scoring
- **Analytics**: Track course views and engagement with charts
- **Role-Based Access**: Different dashboards for admins and students

## Tech Stack

### Backend
- Django 4.2+
- Django REST Framework
- PostgreSQL
- JWT Authentication (djangorestframework-simplejwt)
- Firebase Storage Integration
- Gunicorn + Docker

### Frontend
- React 18.2
- Vite 5.2
- React Router v6
- Tailwind CSS 3.3+
- Axios
- Firebase SDK
- recharts (Analytics)
- react-player (Video playback)

## Project Structure

```
mini-lms/
├── backend/
│   ├── core/                  # Django project settings
│   ├── accounts/              # User authentication
│   ├── courses/               # Course & video management
│   ├── quizzes/               # Quiz system
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── Procfile
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── pages/             # Page components
│   │   ├── components/        # Reusable components
│   │   ├── context/           # Auth context
│   │   ├── api/               # Axios config
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── firebase.js
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── .env.example
│   └── index.html
└── README.md
```

## Setup Instructions

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

The backend will run on `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Setup environment variables**
   ```bash
   cp .env.example .env.local
   # Add your Firebase credentials to .env.local
   ```

4. **Start development server**
   ```bash
   npm run dev
   ```

The frontend will run on `http://localhost:5173`

## Database Setup

The project uses PostgreSQL. Make sure you have PostgreSQL installed and running:

```bash
# Windows (using psql)
psql -U postgres
CREATE DATABASE mini_lms;

# macOS/Linux
createdb mini_lms
```

Update `.env` in backend folder with your PostgreSQL credentials.

## Firebase Setup

1. Create a new Firebase project at https://console.firebase.google.com
2. Enable Firebase Storage
3. Get your Firebase credentials
4. Add credentials to `frontend/.env.local`:
   ```
   VITE_FIREBASE_API_KEY=YOUR_KEY
   VITE_FIREBASE_AUTH_DOMAIN=YOUR_DOMAIN
   VITE_FIREBASE_PROJECT_ID=YOUR_PROJECT_ID
   VITE_FIREBASE_STORAGE_BUCKET=YOUR_BUCKET
   VITE_FIREBASE_MESSAGING_SENDER_ID=YOUR_ID
   VITE_FIREBASE_APP_ID=YOUR_APP_ID
   VITE_FIREBASE_MEASUREMENT_ID=YOUR_ID
   ```

5. Update Firebase Storage Rules in Firebase Console:
   ```javascript
   rules_version = '2';
   service firebase.storage {
     match /b/{bucket}/o {
       match /{allPaths=**} {
         allow read, write: if true;
       }
     }
   }
   ```
   
   For production, use:
   ```javascript
   rules_version = '2';
   service firebase.storage {
     match /b/{bucket}/o {
       match /videos/{allPaths=**} {
         allow read: if true;
         allow write: if request.auth != null && request.resource.size < 200 * 1024 * 1024;
       }
     }
   }
   ```

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/token/` - Login (get tokens)
- `POST /api/auth/token/refresh/` - Refresh access token
- `GET /api/auth/me/` - Get current user

### Courses
- `GET /api/courses/` - List all courses
- `POST /api/courses/` - Create course (admin only)
- `GET /api/courses/{id}/` - Get course detail
- `PUT /api/courses/{id}/` - Update course (admin only)
- `DELETE /api/courses/{id}/` - Delete course (admin only)

### Videos
- `GET /api/videos/` - List all videos
- `POST /api/videos/` - Upload video (admin only)
- `GET /api/videos/{id}/` - Get video detail
- `DELETE /api/videos/{id}/` - Delete video (admin only)

### Quizzes
- `GET /api/quizzes/` - List all quizzes
- `POST /api/quizzes/` - Create quiz (admin only)
- `GET /api/quizzes/{id}/` - Get quiz detail
- `GET /api/questions/` - List all questions
- `POST /api/questions/` - Create question (admin only)

## User Roles

### Admin
- Create, edit, delete courses
- Upload and manage videos
- Create quizzes and questions
- View analytics

### Student
- Browse courses
- Watch videos
- Take quizzes
- View personal dashboard

## Running the Application

1. **Terminal 1 - Backend**
   ```bash
   cd backend
   python manage.py runserver
   ```

2. **Terminal 2 - Frontend**
   ```bash
   cd frontend
   npm run dev
   ```

3. **Access the application**
   - Open browser to `http://localhost:5173`
   - Login with admin or student credentials

## Building for Production

### Backend
```bash
# Using Docker
docker build -t mini-lms-backend .
docker run -p 8000:8000 mini-lms-backend

# Using Heroku
git push heroku main
```

### Frontend
```bash
npm run build
# Deploy dist/ folder to hosting service
```

## Development Commands

### Backend
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Access Django admin
# Navigate to http://localhost:8000/admin/
```

### Frontend
```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

## Troubleshooting

### Database Connection Issues
- Ensure PostgreSQL is running
- Check `.env` database credentials
- Run `python manage.py migrate`

### CORS Errors
- Update `CORS_ALLOWED_ORIGINS` in backend settings.py
- Frontend must be running on correct port (5173)

### Firebase Upload Errors
- Verify Firebase credentials in `.env.local`
- Check Firebase Storage Rules
- Ensure storage bucket permissions are correct

### JWT Token Issues
- Clear browser localStorage
- Check token expiration (60 minutes for access token)
- Ensure refresh token is stored

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please create an issue in the project repository.
