window.addEventListener('scroll',function(){
  const winHeight = window.pageYOffset;
  const link = document.querySelector('.top-link');
  if(winHeight>500){
    link.classList.add('show-link');
  }
  else{
    link.classList.remove('show-link');
  }
})