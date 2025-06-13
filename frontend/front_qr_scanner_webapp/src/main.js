
import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router' 
import * as VueQrcodeReader from 'vue-qrcode-reader'
import ToastPlugin from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-bootstrap.css';

const app = createApp(App)
app.use(router) 
app.use(VueQrcodeReader)
app.mount('#app')

// Set the toast preferences
app.use(ToastPlugin, {
  position: 'bottom',
  duration: 3000,        
  type: 'success',
  dismissible: true,     
  pauseOnHover: true,    
});