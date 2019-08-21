function createDeletebutton(div){
  btn = document.createElement('button');
  btn.innerHTML = "Delete";
  div.appendChild(btn);
}

document.addEventListener('DOMContentLoaded',()=>{
  console.log(localStorage.currentChannel);
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port+'/channel');
  document.querySelector('button').onclick=()=>{
   const msg = document.querySelector('input').value;
   console.log(msg);
   socket.emit('send msg',{'user':localStorage.user,'msg':msg,'currentChannel':localStorage.currentChannel});
  }
  document.querySelectorAll('div').forEach(div=>{
    // alert(div.firstChild)
    console.log(div.firstElementChild.textContent);
    if(div.firstElementChild.textContent==localStorage.user){
      createDeletebutton(div);
    }
    div.appendChild(document.createElement('hr'));

  });
  socket.on('recieve msg',data=>{
    console.log(data)
    if(data.currentChannel==localStorage.currentChannel){
    div = document.createElement('div')
    user = document.createElement('h3');
    msg = document.createElement('p');
    text = document.createTextNode(data.user);
    user.appendChild(text);
    text = document.createTextNode(data.msg);
    msg.appendChild(text);
    div.appendChild(user);
    div.appendChild(msg);
    if(localStorage.user== data.user)
      {
        createDeletebutton(div);
      }
    div.appendChild(document.createElement('hr'));

    document.body.appendChild(div)
  }
  });

});
function setStorage(){
  console.log('ana fe storage');
    var request = new XMLHttpRequest;
    request.open('GET','/GetCurrentChannel');
    request.onload=()=>{
      console.log('ana fe onload')
      const data = JSON.parse(request.responseText);
      console.log(data);
      if(data.success){
        console.log(data.currentChannel);
        localStorage['currentChannel'] =data.currentChannel;
      }
    }

    request.send();

}
function checkuser(user){
  alert(user);
}
