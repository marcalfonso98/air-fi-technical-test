<template>
  <h1 class="title">Lector de códigos QR</h1>
  <div class="login-container">
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="loginUser">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div class="form-group">
        <label for="password">Contraseña:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button class="login-button" type="submit">Acceder</button>
    </form>
    <p class="register-text" @click="registerUser">Nuevo usuario? Registrarse</p>

  </div>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toast-notification';


export default {
  name: 'LoginFormView', 
  data() {
    return {
      email: '',
      password: '',
      submitted: false,
      error: null,
    };
  },
methods: {
    registerUser() {
      this.$router.push('/register'); 
    },
    async loginUser() {
      this.loading = true;
      this.errorMessage = '';
			const toast = useToast(); 

      try {
        const response = await axios.post('http://127.0.0.1:8000/api/token/', {
          email: this.email,
          password: this.password,
        });
        const { access } = response.data;
        
        // Save the token
        localStorage.setItem('accessToken', access);

        this.$router.push('/scan'); 
      } catch (error) {
        console.error('Error al iniciar sesión:', error);
        toast.error("No existe ningún usuario con las credenciales introducidas.")
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>

:global(h2) {
  color: white;
}
.login-container {
  width: 400px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.login-container h2 {
  margin-bottom: 30px;
  font-size: 30px;
  font-weight: bold;
  text-align: center;
}

.login-container label {
  text-align: center;
  color: white;
}

.title {
  font-size: 50px;
  color: white;
  position: top;
}

.register-text {
  color: white;
  margin-top: 30px;
  text-align: center;
}
.register-text:hover {
  cursor: pointer;
  transform: scale(1.1);
}

.login-button {
  margin-top: 30px;
}

.login-button:hover {
  background-color: rgba(2, 82, 129, 0.692);
  transform:scale(1.05)
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}
</style>