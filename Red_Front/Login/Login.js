document.addEventListener('DOMContentLoaded', function() {
    const registerBtn = document.getElementById('register-btn');
    const cancelBtn = document.getElementById('cancel-btn');
    const registrationFormContainer = document.getElementById('registration-form-container');
    const loginForm = document.getElementById('login-form');

    registerBtn.addEventListener('click', function() {
        loginForm.style.display = 'none'; 
        registrationFormContainer.style.display = 'block'; 
    });

    cancelBtn.addEventListener('click', function() {
        registrationFormContainer.style.display = 'none';
        loginForm.style.display = 'block'; 
    });

    // --------------------------------- Esto es la logica para el login ----------------------------------------

    // Al formulario (loginForm) le añadimos la funcion addEventListener que realiza un evento de escucha, osea que cada vez que se intente enviar el formulario se ejecutara 
    loginForm.addEventListener('submit', function(event) {
        // Por defecto el formulario se envia, vamos a cancelar esto para que nosotros realicemos el envio de forma manual
        event.preventDefault();

        // Acceder a los valores de los inputs del formulario
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // fetch es una funcion tipo http donde definimos la peticion mediante la url. De tipo get y json 
        fetch(`http://127.0.0.1:8000/api/usuarioGet/${username}/${password}/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        //fetch da una respuesta y nosotros usaremos la funcion flecha (then(response => {) para observar que paso 
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Usuario no encontrado');
            }
        })
        //Por ultimo se imprime o se captura el error 
        .then(data => {
            console.log('Login exitoso:', data);
        })
        .catch(error => {
            console.error('Error en el login:', error);
        });
    });

    // --------------------------------- Esto es la logica para el sign up ----------------------------------------

    registrationFormContainer.addEventListener('submit',function(event) {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const lasName = document.getElementById('lasName').value;
        const userName = document.getElementById('userName').value;
        const description = document.getElementById('description').value;
        const age = document.getElementById('age').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const sex = document.getElementById('sex').value;
        const telephone = document.getElementById('telephone').value;
        const ilustracion = document.getElementById('ilustracion').value;

        fetch('http://127.0.0.1:8000/api/usuarioPost/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name,
                lasName: lasName,
                userName: userName,
                description: description,
                age: age,
                email: email,
                password: password,
                sex: sex,
                telephone: telephone,
                ilustracion: ilustracion
            })
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Error en el registro');
            }
        })
        .then(data => {
            console.log('Registro exitoso:', data);
        })
        .catch(error => {
            console.error('Error en el registro:', error);
        });
    });
});
