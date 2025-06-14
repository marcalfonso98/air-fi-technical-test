<template>
  <h1 class="title">Lector de códigos QR</h1>
  <div class="simple-container">
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
      <button class="simple-button" type="submit">Acceder</button>
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


.simple-container {
  width: 400px;
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

input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

</style>