var but = document.querySelector('#mybutton')

but.addEventListener('click', function(e){
    alert('Button clicked');
})


var but1 = document.querySelector('#mybutton1')

but1.addEventListener('click', function(toggleColor){
    const myBgr = document.body;
    myBgr.classList.toggle('red-background');
    
})
