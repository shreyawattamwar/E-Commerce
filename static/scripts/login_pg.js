document.addEventListener('DOMContentLoaded', ()=> {

    msg = document.querySelector('#login');

    msg.addEventListener('keyup' , event => {
        event.preventDefault();
        if(event.keyCode === 13) {
            document.querySelector('#login').click();
        }
    })

})