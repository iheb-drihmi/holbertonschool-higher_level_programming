document.querySelector('#toggle_header').onclick = function (){
    element  = document.querySelector('header')
    if (element.classList.contains('red')){
        element.classList.remove('red')
    }
    else{
        element.classList.add('red')
    }
    element.classList.toggle('green');
}