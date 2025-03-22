/**
 * Update this file with your Firebase configuration settings.
 * API key and auth domain are required.
 */

/**
 * ++++ ADD YOUR FIREBASE CONFIGURATION BELOW ++++
 * === Firebase Apikey and Domain ===
 */


/**
 * Firebase configuration
 * @type {{apiKey: string, authDomain: string}}
 */

import { initializeApp } from "firebase/app";
const config = {
  apiKey: "AIzaSyD9LaQkHUBpyxYjRxF1fE_8soGVsNeuJh8",
  authDomain: "cloud-run-project-454317.firebaseapp.com",
  projectId: "cloud-run-project-454317",
  storageBucket: "cloud-run-project-454317.firebasestorage.app",
  messagingSenderId: "164008081777",
  appId: "1:164008081777:web:3a19cb0486b17d71179ed0"
};

const app = initializeApp(config);

export default config;