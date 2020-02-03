const btn = document.getElementById('btn');
const container = document.getElementById('section');


addEventListener('click', function(){

    console.log("Cambiando el color");
    container.classList.remove('green');
container.className += "purple";
})