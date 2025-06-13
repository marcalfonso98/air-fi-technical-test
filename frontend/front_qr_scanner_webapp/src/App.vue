<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App', // Es buena práctica darle un nombre al componente
};
</script>

<style>
/* Aquí puedes poner estilos CSS globales para toda tu aplicación */
/* Por ejemplo, para resetear márgenes del cuerpo */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
#app {
  /* Puedes añadir estilos aquí si necesitas que el contenedor principal ocupe toda la pantalla */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>