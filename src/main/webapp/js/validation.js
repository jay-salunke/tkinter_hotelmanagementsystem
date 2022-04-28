const isEmpty = (string) => {
    if(string.trim() === ''){
        return true;
    }
    return false;
}

export default function validate(...inputFields){
    let notValid = false;
    for(let i = 0; i < inputFields.length; i++){
        if(isEmpty(inputFields[i].value)){
            notValid = true;
            inputFields[i].classList.toggle("box-shadow-red");
            setTimeout(() => {
                inputFields[i].classList.toggle("box-shadow-red");
            },1000);
        }
    }
    return notValid;
}