const mainContainer = document.getElementById('main-container');
const removeButtons = document.getElementsByClassName("remove-button");

for(i=0; i<removeButtons.length; i++){
    removeButtons[i].addEventListener('click', blur);
}

function blur(){
    mainContainer.classList.add('blur');
    setTimeout(function(){ 
        mainContainer.classList.remove('blur');}, 
    1000);
}