import { initializeApp } from "firebase/app";
import { getStorage, ref, uploadBytesResumable, getDownloadURL } from "firebase/storage";

const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY || "AIzaSyDApl_-5yjRuNP0C_iUHNzXXR4PmHkzrRg",
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN || "mini-lms-a5e66.firebaseapp.com",
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID || "mini-lms-a5e66",
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET || "mini-lms-a5e66.firebasestorage.app",
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID || "511701248669",
  appId: import.meta.env.VITE_FIREBASE_APP_ID || "1:511701248669:web:d78801b1616e731cee0274",
  measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENT_ID || "G-92R5JLSDHD",
};

const app = initializeApp(firebaseConfig);
const storage = getStorage(app);

export { storage, ref, uploadBytesResumable, getDownloadURL };
