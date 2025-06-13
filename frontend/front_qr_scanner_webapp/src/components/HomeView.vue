<script setup>
import qrCodeImg from '../assets/airfi-qr-code.png';

</script>


<template>
    <div class="headline">
        <h1 class="title">Prueba Técnica Air-Fi
            <span class="sub-title">by Marc Alfonso</span>
        </h1>
    </div>
    <img v-bind:src="qrCodeImg" width="300px" />

    <button class="login-button" @click="goToLogin">
        Iniciar Sesión
    </button>

</template>

<script>
export default {
    name: 'LoginFormView',
    methods: {
        registerUser() {
            this.$router.push('/register');
        },
        async goToLogin() {
            // Save the token
            this.$router.push('/login');
        },
    },
};
</script>

<style scoped>
.login-container {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.login-button {
    max-width: 40%;
    margin: 50px;
}

.login-button:hover {
    background-color: rgba(2, 82, 129, 0.692);
    transform: scale(1.05)
}

.title {
    font-size: 50px;
    color: white;
    position: top;
}

.headline {
    margin-bottom: 30px;
}

.sub-title {
    display: block;
    text-align: right;
    font-size: 13px;
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