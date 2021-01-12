 
    window.addEventListener('scroll',function(){
      var x = document.getElementById('navtoggle');
    const navHeight = x.getBoundingClientRect().height;
    const winHeight = window.pageYOffset;
      if(winHeight>navHeight){
    
      x.classList.add('dark');
        x.classList.remove('border-bottom');   
      }
      else{
    
        x.classList.remove('dark');
        x.classList.add('border-bottom');

      }
    });
    
    var btn = document.getElementById('btn');
    var links = document.getElementById('navtoggle');
    btn.addEventListener('click',function(){
        links.classList.toggle('show-links');
    })
    

    var dropDownToggleBtn = document.querySelector('.dropdown-toggle');
    function my(){
      var dropMenu = document.querySelector('.dropdown-menu');
      dropMenu.classList.toggle('drop');
    }
    dropDownToggleBtn.addEventListener('click', my);
   
   