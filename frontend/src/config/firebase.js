import { initializeApp } from 'firebase/app';
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, onAuthStateChanged } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
  apiKey: "AIzaSyCA2xqzunUA_86dK3il8G6PR8s2SlAq_7k",
  authDomain: "smartbid-5df90.firebaseapp.com",
  projectId: "smartbid-5df90",
  storageBucket: "smartbid-5df90.firebasestorage.app",
  messagingSenderId: "1026308403094",
  appId: "1:1026308403094:web:c752c8b5558a198606f7b7"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

export { 
  auth, 
  db, 
  createUserWithEmailAndPassword, 
  signInWithEmailAndPassword, 
  signOut, 
  onAuthStateChanged 
};

export default app; 