'use strict';
const number = parseInt(prompt('give number of partisipants.'));
let arra = [];
while (arra.length != number ) {arra.push(prompt('give partisipant.'));}
const listobject = document.getElementById ('list');
for (let i = 1; i != number; i++) {
     let newobject = document.createElement ('li');
     newobject.textContent = arra[i];
     listobject.appendChild(newobject);
}
