'use strict';
let arra = [];
for (let i = 0; i != 6;i++) {arra.push(prompt('give dog.'));}
arra.sort().reverse();
const listobject = document.getElementById ('list');
for (let i = 0; i != 6; i++) {
     let newobject = document.createElement ('li');
     newobject.textContent = arra[i];
     listobject.appendChild(newobject);
}
