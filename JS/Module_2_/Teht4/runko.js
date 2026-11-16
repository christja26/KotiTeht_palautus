'use strict';
let arra = [];
while (arra[arra.length - 1] != 0) {arra.push(prompt("give number."))}
arra.sort((a,b) => b-a);
for (let i = 0; i < arra.length; i++) {console.log(arra[i]);}