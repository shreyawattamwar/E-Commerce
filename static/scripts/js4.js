document.addEventListener('DOMContentLoaded' ,() => {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    
    
    

    socket.on('message', data => {
        const p = document.createElement('p');
        const p_user = document.createElement('span');
        const br = document.createElement('br');
        p_user.innerHTML = data.username;
        p.innerHTML = p_user.outerHTML  + data.msg;
        document.querySelector('#display-msg-area').append(p);

    });

    
    //send


    document.querySelector('#send-msg').onclick =  ()=>{
        socket.send({'msg' : document.querySelector('#user-msg').value,
        'username': user_name+" : "});
        
}

})