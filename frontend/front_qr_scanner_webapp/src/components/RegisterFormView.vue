<template>
	<div class="simple-container">
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
			<button class="simple-button" type="submit">Registrarse</button>
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

input[type="email"],
input[type="password"],
input[type="text"] {
	width: 100%;
	padding: 10px;
	border: 1px solid #ddd;
	border-radius: 4px;
	box-sizing: border-box;
}

</style>