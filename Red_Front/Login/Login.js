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
});
