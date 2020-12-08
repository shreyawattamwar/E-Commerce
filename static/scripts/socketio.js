document.addEventListener('DOMContentLoaded' ,() => {
    var socket = newFunction();
    socket.on('connect', ()=> {
        socket.send('i am connected! How are you?');

    });

    socket.on('message', data => {
        const p = document.createElement('p');
        const br = document.createElement('br');
        p.innerHTML = data;
        document.querySelector('#display-msg-area').append(p);

    });

    


    document.querySelector('#send-msg').onclick =  ()=>{
        socket.emit(document.querySelector('#user-msg').value);
    }
        
})

function newFunction() {
    return io.connect('http://' + document.domain + ':' + location.port);
}
