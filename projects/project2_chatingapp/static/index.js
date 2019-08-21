document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('button').onclick = ()=>{
    display_name = document.querySelector('input').value;
    localStorage.setItem('user',display_name);
    location.replace('channels');

  }
  if(!localStorage.getItem('user')){
    localStorage.setItem('user','');
  }else{
    console.log('hello');
    location.replace('channels');
    if(!localStorage.getItem('currentChannel')){
      localStorage.setItem('currentChannel','');
    }
    else{
      location.replace(`channel/${localStorage.currentChannel}`);
    }
  }


});
