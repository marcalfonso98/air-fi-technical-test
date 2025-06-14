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

    <button class="simple-button" @click="goToLogin">
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

/* Set the max width */
.simple-button {
    max-width: 50%;
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

</style>