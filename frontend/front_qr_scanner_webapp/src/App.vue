<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App', 
};
</script>

<style>

/* Set global styles shared with some files*/
body {
  margin: 0;
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

h2 {
  color: white;
  text-align: center;
}

/* Styles for the login button (Home + Login Views) */
/* Globalise containers + buttons */
.simple-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 30px;
}

.simple-button:hover {
  background-color: rgba(2, 82, 129, 0.692);
  transform:scale(1.05)
}

.simple-container {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.simple-container h2 {
  margin-bottom: 30px;
  font-size: 30px;
  font-weight: bold;
  text-align: center;
}

.simple-container label {
	text-align: center;
	color: white;
}

label {
  display: block;
  margin-bottom: 5px;
  color: white;
}

.form-group {
  margin-bottom: 15px;
}

</style>