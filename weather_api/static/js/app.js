const mainContainer = document.getElementById('main-container');
const modalWindow = document.getElementById('modal');
const removeButtons = document.getElementsByClassName("remove");


for(i=0; i<removeButtons.length; i++){
    removeButtons[i].addEventListener('click', showModal);
}


function showModal(e){
    mainContainer.classList.add('blur');
    modalWindow.style.display = "flex";
    document.getElementById('modal-button').addEventListener('click', hideModal);
    e.preventDefault();
};


function hideModal(e){
    mainContainer.classList.remove('blur');
    modalWindow.style.display = "none";
    e.preventDefault();
};





const Http = new XMLHttpRequest();
const url='http://api.openweathermap.org/data/2.5/forecast?q=krakow&APPID=f8d2eb98e626defe7bcc37762d3af2b7';
Http.open("GET", url);
Http.send();

Http.onreadystatechange=(e)=>{
console.log(JSON.parse(Http.responseText));
response = JSON.parse(Http.responseText);

// city
console.log(response.city.name);
// temp
console.log(response.list[0].main.temp);
// icon
console.log(response.list[0].weather[0].icon);
// weather
console.log(response.list[0].weather[0].description);
}