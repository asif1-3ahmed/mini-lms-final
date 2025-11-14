// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDApl_-5yjRuNP0C_iUHNzXXR4PmHkzrRg",
  authDomain: "mini-lms-a5e66.firebaseapp.com",
  projectId: "mini-lms-a5e66",
  storageBucket: "mini-lms-a5e66.firebasestorage.app",
  messagingSenderId: "511701248669",
  appId: "1:511701248669:web:d78801b1616e731cee0274",
  measurementId: "G-92R5JLSDHD"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);