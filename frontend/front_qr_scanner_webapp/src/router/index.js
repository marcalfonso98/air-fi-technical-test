import { createRouter, createWebHistory } from 'vue-router';

import LoginFormView from '../components/LoginFormView.vue'
import ScannerView from '@/components/ScannerView.vue';
import RegisterFormView from '@/components/RegisterFormView.vue';
import HomeView from '@/components/HomeView.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView, 
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginFormView, 
  },
    {
    path: '/scan',
    name: 'Scan',
    component: ScannerView, 
    meta: { requiresAuth: true}
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterFormView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Protect the scan view
router.beforeEach((to, from) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const isAuthenticated = localStorage.getItem('accessToken'); 

  if (requiresAuth && !isAuthenticated) {
    return '/login';
  } 
});


export default router;