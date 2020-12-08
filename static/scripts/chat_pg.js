document.addEventListener('DOMContentLoaded', ()=> {
    msg = document.querySelector('#user-msg');

    msg.addEventListener('keyup' , event => {
        event.preventDefault();
        if(event.keyCode === 13) {
            document.querySelector('#send-msg').click();
        }
    })



    
})