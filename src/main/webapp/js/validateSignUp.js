
const sup_email = document.getElementById('email_id');
const sup_password = document.getElementById('password');
const sup_fname= document.getElementById('lname');
const sup_lname= document.getElementById('fname');
const sup_number= document.getElementById('number');
const sup_submit = document.querySelector("#signup-submit");


// console.log(sup_submit);
// console.log(sup_email);
// console.log(sup_password);
// console.log(sup_fname);
// console.log(sup_lname);
// console.log(sup_number);

import validate from "./validation.js";


sup_submit.addEventListener('click',(e)=>{
    if(validate(sup_email,sup_password,sup_fname,sup_lname,sup_number)){
        e.preventDefault();
    }
});


