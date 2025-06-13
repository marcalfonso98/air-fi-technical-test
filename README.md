# Prueba Técnica Air-Fi: Lector de Códigos QR

Este proyecto forma parte de la prueba técnica para una vacante de programador en la empresa **Air-Fi**.

## Descripción del Proyecto

El objetivo de este proyecto es desarrollar una aplicación web completa, que incluye tanto el frontend como el backend, para permitir la lectura y gestión de códigos QR. La aplicación permite a los usuarios autenticados escanear códigos QR y registrar la información asociada, incluyendo el envío de dicha información a una dirección de correo electrónico específica.

## Estructura del Proyecto

El repositorio está organizado en dos directorios principales:

* `backend/`: Contiene la lógica del servidor desarrollada con Django y Django REST Framework.
* `frontend/`: Contiene la interfaz de usuario desarrollada con Vue.js.

## Cómo Ejecutar el Proyecto

Para poner en marcha la aplicación, deberás levantar tanto el backend como el frontend por separado.

### **1. Backend (Django REST Framework)**

El backend se encarga de gestionar la API, la base de datos (registro de escaneos, usuarios) y la lógica de negocio.

**Requisitos previos:**
* Python 3.8+
* pip (gestor de paquetes de Python)

**Pasos para la ejecución:**

1.  **Navega al directorio del backend:**
    ```bash
    cd backend/qr_scanner_webapp/
    ```
2.  **Crea y activa un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate # macOS/Linux
    # o
    venv\Scripts\activate # Windows
    ```
3.  **Instala las dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Aplica las migraciones de la base de datos:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  **Crea un superusuario (opcional, para acceder al panel de administración de Django):**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    El backend estará disponible en `http://127.0.0.1:8000/`.

### **2. Frontend (Vue.js)**

El frontend proporciona la interfaz de usuario para interactuar con la aplicación, incluyendo el lector de códigos QR y el flujo de autenticación.

**Requisitos previos:**
* Node.js (versión LTS recomendada)
* npm (gestor de paquetes de Node.js, viene con Node.js)

**Pasos para la ejecución:**

1.  **Navega al directorio del frontend:**
    ```bash
    cd frontend/front_qr_scanner_webapp
    ```
2.  **Instala las dependencias de Node.js:**
    ```bash
    npm install
    ```
3.  **Inicia el servidor de desarrollo de Vue.js:**
    ```bash
    npm run dev
    ```
    Se proporcionará un dominio `localhost` (ej. `http://localhost:5173/`) en la consola. Abre esta URL en tu navegador web.

### **3. Prueba de la Aplicación**

Una vez que tanto el backend (Django) como el frontend (Vue.js) estén levantados y ejecutándose, ya podrás acceder a la aplicación web a través de la URL del frontend y probar su funcionalidad completa.

## Observaciones Importantes

1.  **Funcionalidades Adicionales:** Se han implementado todos los pasos opcionales de la prueba técnica. Además, se ha añadido una pantalla de inicio (`HomeView`) que precede a la pantalla de inicio de sesión (`LoginFormView`), ofreciendo un punto de entrada más amigable.
2.  **Historial de Escaneos:**
    * Puedes visualizar el historial de todos los escaneos realizados accediendo al panel de administración de Django (`http://127.0.0.1:8000/admin/`) con una cuenta de superusuario.
    * Alternativamente, existe una API específica para consultar el historial de escaneos de un usuario autenticado: `http://127.0.0.1:8000/api/scan-history/`. Esta API requiere un **token de autenticación de tipo Bearer** en las cabeceras de la solicitud. El historial retornado corresponderá únicamente a los escaneos realizados por el usuario asociado a dicho token.
3.  **Lector de Códigos QR:**
    * El lector de códigos QR está implementado para utilizar la **cámara del dispositivo** (webcam). Por lo tanto, se requiere una cámara o webcam funcional para utilizar esta característica.
    * **Nota sobre la detección:** El lector puede ocasionalmente presentar desafíos en la detección del código QR. Para asegurar una lectura exitosa, se recomienda enfocar el código QR desde una distancia cercana y lo más nítido posible.
4.  **Configuración de Correo Electrónico:**
    * La configuración de envío de correos electrónicos en el backend se ha realizado utilizando `console.EmailBackend` de Django. Esto significa que **no se enviarán correos electrónicos reales** sino que se verán en la misma consola de ejecución.

## Tecnologías Utilizadas

### Backend
* **Python:** Lenguaje de programación principal.
* **Django:** Framework web de alto nivel.
* **Django REST Framework (DRF):** Para la construcción de APIs RESTful.
* **Simple JWT:** Para la autenticación con tokens.


### Frontend
* **Vue.js 3:** Framework progresivo de JavaScript para la interfaz de usuario.
* **Vue Router:** Para la gestión de la navegación y las rutas.
* **Axios:** Cliente HTTP para realizar las solicitudes API.
* **Vue QRcode Reader:** Componente para la funcionalidad de lectura de códigos QR.
* **Vue Toast Notification:** Para notificaciones de usuario (toasts).
* **Vite:** Herramienta de compilación rápida para el desarrollo frontend.