<template>
	<div class="register-container">
		<h2>Crear una cuenta</h2>
		<form @submit.prevent="registerUser">
			<div class="form-group">
				<label for="text">Nombre de usuario:</label>
				<input type="text" id="text" v-model="username" required />
			</div>
			<div class="form-group">
				<label for="email">Email:</label>
				<input type="email" id="email" v-model="email" required />
			</div>
			<div class="form-group">
				<label for="password">Contraseña:</label>
				<input type="password" id="password" v-model="password" required />
			</div>
			<button class="register-button" type="submit">Registrarse</button>
		</form>
	</div>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toast-notification';

export default {
	name: 'RegisterFormView',
	data() {
		return {
			email: '',
			password: '',
			username: '',
			submitted: false,
			error: null,
		};
	},
	methods: {
		async registerUser() {
			this.loading = true;
			this.errorMessage = '';
			const toast = useToast(); 
			
			try {
				const response = await axios.post('http://127.0.0.1:8000/api/register/', {
					username: this.username,
					email: this.email,
					password: this.password,
				});

				const { message } = response.data;

			    toast.success(message, {duration: 1500});

				// login page
				this.$router.push('/');

			} catch (error) {
				console.error('Error al crear el registro:', error);
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

.register-button:hover {
  background-color: rgba(2, 82, 129, 0.692);
  transform:scale(1.05)
}

.register-container {
	max-width: 400px;
	margin: 50px auto;
	padding: 20px;
	border: 1px solid #ccc;
	border-radius: 8px;
	box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.register-container h2 {
	margin-bottom: 30px;
	font-size: 30px;
	font-weight: bold;
}

.register-container label {
	text-align: center;
	color: white;
}

.register-button {
	margin-top: 30px;
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
input[type="password"],
input[type="text"] {
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