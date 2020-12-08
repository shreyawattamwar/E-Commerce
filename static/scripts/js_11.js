document.addEventListener('DOMContentLoaded' ,() => {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    
    let room = 'Clothing';
    joinRoom(room);
    
    const username = document.querySelector('#get-username').innerHTML;


    socket.on('message', data => {
        const p = document.createElement('p');
        const p_user = document.createElement('b');
        const br = document.createElement('br');
        const p_msg = document.createElement('span');
        if(data.username==username){
            
            p.className = 'msgbox';
            p_user.innerHTML = data.username;
            p_msg.innerHTML = data.msg;
            p.innerHTML = p_user.outerHTML  + " : "+ p_msg.outerHTML + br.outerHTML + data.time_msg;
            document.querySelector('#display-msg-area').append(p);
        
        
    }
    else if(typeof data.username!=='undefined'){
        p.className = 'msgbox2'
        p_user.innerHTML = data.username;
        p_msg.innerHTML = data.msg;
        p.innerHTML = p_user.outerHTML  + " : "+ p_msg.outerHTML + br.outerHTML + data.time_msg;
        document.querySelector('#display-msg-area').append(p);

    }
        
        else{
            printSysMsg(data.msg);
        }

    });

    
    //send


    document.querySelector('#send-msg').onclick =  ()=>{
        socket.send({'msg' : document.querySelector('#user-msg').value,
        'username': user_name ,'room' : room});


        //clear input box
        document.querySelector('#user-msg').value = '';
        
}

    document.querySelectorAll('.select_room').forEach(p => {
        p.onclick = () =>{
            let newroom = p.innerHTML;
            if (newroom == room){
                msg = `You are already in ${room} room.`
                printSysMsg(msg);
            }
            else{
                leaveRoom(room);
                joinRoom(newroom);
                room = newroom;
            }
        }
    });


    //Leave Room
    function leaveRoom(room) {
        socket.emit('leave',{'username': user_name ,'room': room});
    }

    //join room
    function joinRoom(room) {
        socket.emit('join',{'username': user_name ,'room': room});

        //clear display area
        document.querySelector('#display-msg-area').innerHTML = '';

        //auto focus
        document.querySelector('#user-msg').focus();


    }

    // print sys msg
    function printSysMsg(msg) {
        const p = document.createElement('p');
        p.innerHTML = msg;
        p.className = 'top-msg';
        document.querySelector('#display-msg-area').append(p);
    }


    document.querySelector('#logout').onclick =  ()=>{
        location.assign('http://127.0.0.1:5000/logout');

    }


})