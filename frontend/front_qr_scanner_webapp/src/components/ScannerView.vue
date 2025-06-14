<template>
  <div class="scanner-container">
    <h2 style="color: white">Escáner de códigos QR</h2>
    <h4>Enfoca tanto como sea posible y acerca el código a la cámara, a veces le cuesta identificar el QR</h4>

    <p class="error-message">{{ cameraError }}</p>

    <div class="qr-scanner-area">
      <p v-if="!qrContent && !cameraError">Apunte su cámara a un código QR...</p>
      <qrcode-stream :constraints="selectedConstraints" :track="trackFunctionSelected.value"
        :formats="selectedBarcodeFormats" @error="onError" @detect="onDetect" @camera-on="onCameraReady" />
    </div>

    <div class="form-group">
      <label for="qrContentDisplay">Contenido QR</label>
      <input type="text" id="qrContentDisplay" v-model="qrContent" readonly>
    </div>

    <div class="form-group">
      <label for="toEmail">Email</label>
      <input type="email" id="toEmail" v-model="toEmail" required placeholder="Correo del destinatario...">
    </div>

    <button class="send-button" @click="sendQrData">
      {{ loading ? 'Enviando...' : 'Enviar QR' }}
    </button>

  </div>
</template>

<script setup>
import { ref } from 'vue';
import { QrcodeStream } from 'vue-qrcode-reader';
import axios from 'axios';
import { useToast } from 'vue-toast-notification';
import { useRouter } from 'vue-router';
const router = useRouter();

const qrContent = ref('');
const result = ref('');
const cameraError = ref('');
const successMessage = ref(null);
const errorMessage = ref(null);

const toEmail = ref('');
const loading = ref(false);

function onDetect(detectedCodes) {
  if (detectedCodes.length > 0) {
    const rawValue = detectedCodes[0].rawValue;
    qrContent.value = rawValue;
    result.value = JSON.stringify(detectedCodes.map((code) => code.rawValue));
    successMessage.value = 'QR Decodificado con éxito.';
    cameraError.value = '';
  } else {
    qrContent.value = '';
    successMessage.value = null;
  }
}

const selectedConstraints = ref({ facingMode: 'environment' });
const defaultConstraintOptions = [
  { label: 'Cámara trasera', constraints: { facingMode: 'environment' } },
  { label: 'Cámara frontal', constraints: { facingMode: 'user' } }
];
const constraintOptions = ref(defaultConstraintOptions);

async function onCameraReady() {
  try {
    const devices = await navigator.mediaDevices.enumerateDevices();
    const videoDevices = devices.filter(({ kind }) => kind === 'videoinput');

    constraintOptions.value = [
      ...defaultConstraintOptions,
      ...videoDevices.map(({ deviceId, label }) => ({
        label: `${label} (ID: ${deviceId})`,
        constraints: { deviceId }
      }))
    ];
    cameraError.value = '';
  } catch (err) {
    console.error('Debug: onCameraReady - Error al enumerar dispositivos:', err);
  }
}

function paintOutline(detectedCodes, ctx) {
  for (const detectedCode of detectedCodes) {
    const [firstPoint, ...otherPoints] = detectedCode.cornerPoints;
    ctx.strokeStyle = 'red';
    ctx.beginPath();
    ctx.moveTo(firstPoint.x, firstPoint.y);
    for (const { x, y } of otherPoints) {
      ctx.lineTo(x, y);
    }
    ctx.lineTo(firstPoint.x, firstPoint.y);
    ctx.closePath();
    ctx.stroke();
  }
}

const trackFunctionOptions = [
  { text: 'Ninguno', value: undefined },
  { text: 'Contorno (Rojo)', value: paintOutline },
];
const trackFunctionSelected = ref(trackFunctionOptions[1]);

// Check for common camera errors
function onError(err) {
  cameraError.value = `[${err.name}]: `;

  if (err.name === 'NotAllowedError') {
    cameraError.value += 'Faltan permisos para acceder a la cámara.';
  } else if (err.name === 'NotFoundError') {
    cameraError.value += 'No se encontró ninguna cámara en este dispositivo.';
  } else if (err.name === 'NotReadableError') {
    cameraError.value += 'Cámara en uso por otra aplicación.';
  } else if (err.name === 'StreamApiNotSupportedError') {
    cameraError.value += 'Incompatibilidad de la API con el navegador actual.';
  } else {
    cameraError.value += err.message;
  }
}

async function sendQrData() {
  loading.value = true;
  successMessage.value = null; 
  errorMessage.value = null;   
  const toast = useToast(); 


  // Check if the QR content is filled
  if (!qrContent.value) { 
    toast.warning('Escanea el código QR antes de enviar, por favor.');
    loading.value = false;
    return;
  }

  // Check if the email field is filled
  if (!toEmail.value) { 
    toast.warning('El campo email no puede estar vacío.');
    loading.value = false;
    return;
  }

  // Check email format
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(toEmail.value)) {
    toast.warning('El correo introducido no tiene el formato adecuado.');
    loading.value = false;
    return;
  }

  try {
    // Retrieve accessToken from localStorage
    let accessToken = localStorage.getItem('accessToken'); 

    // Set the bearer token
    if (accessToken) {
      axios.defaults.headers.common['Authorization'] = 'Bearer ' + accessToken;
    } else {
      // If acces token is not found -> user ain't logged
      toast.error('No tienes autenticación para usar el escáner, por favor inicia sessión');
      
      // Send the user to the login page
      router.push('/');
      loading.value = false;
      return;
    }

    // Get the API response
    const response = await axios.post('http://127.0.0.1:8000/api/scan/', {
      qr_content: qrContent.value,
      to_email: toEmail.value,
    });

    const { message } = response.data;
    toast.success(message);

    qrContent.value = '';
    toEmail.value = '';

  } catch (error) {
    let statusCode = null;
    let errorMessageForUser = 'Ocurrió un error desconocido.';

    if (error.response) {
      
      statusCode = error.response.status;
      console.error('Error de respuesta del servidor:', statusCode, error.response.data);

      if (statusCode) {
        switch (statusCode) {
          case 401: // Unauthorized
            errorMessageForUser = 'Acceso no autoritzado, por favor, inicia sesión de nuevo.';
            localStorage.removeItem('accessToken');
            
            // Go to login
            router.push('/');
            break;
          default:
            errorMessageForUser = `Error del servidor: ${statusCode}.`;
        }
      }
    } 

    toast.error(`Error: ${errorMessageForUser}`);

  } finally {
    loading.value = false; 
  }
}

</script>

<style scoped>

.send-button:hover {
  transform: scale(1.05);
}

.error-message {
  color: red;
}

.scanner-container {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.camera-options {
  margin-bottom: 20px;
  padding: 10px;
  border: 1px dashed #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.qr-scanner-area {
  min-height: 250px;
  border: 2px dashed #007bff;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
  padding: 10px;
  background-color: #f0f8ff;
  border-radius: 8px;
}

input[type="text"],
input[type="email"] {
  width: calc(100% - 22px);
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  padding: 10px 20px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
  margin-right: 5px;
}

</style>