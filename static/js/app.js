const mainContainer = document.getElementById('main-container');
const modalWindow = document.getElementById('modal');
const removeButtons = document.getElementsByClassName("remove");


for(i=0; i<removeButtons.length; i++){
    removeButtons[i].addEventListener('click', showModal);
}


function showModal(e){
    mainContainer.classList.add('blur');
    modalWindow.style.display = "flex";
    document.getElementById('modal').addEventListener('click', hideModal);
    e.preventDefault();
};


function hideModal(e){
    mainContainer.classList.remove('blur');
    modalWindow.style.display = "none";
    e.preventDefault();
};