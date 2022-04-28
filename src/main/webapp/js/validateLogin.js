
const log_email = document.getElementById('email');
const log_password = document.getElementById('pword');
const log_submit = document.querySelector("#login-submit");



// console.log(log_email);
// console.log(log_password);

import validate from "./validation.js";

log_submit.addEventListener('click',(e)=>{
    if(validate(log_email,log_password)){
        e.preventDefault();
    }
});


