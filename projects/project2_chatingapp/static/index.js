document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('button').onclick = ()=>{
    display_name = document.querySelector('input').value;
    localStorage.setItem(display_name);
  }
  if(!localStorage.getItem('user')){
    localStorage.setItem('user','');
  }else{
    location.href=Flask.url_for('channels')
  }

});
