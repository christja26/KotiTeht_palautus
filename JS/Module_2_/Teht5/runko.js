'use strict';
let arra = [];
while (true) { let number = prompt("give number.");
if (arra.includes(number)) {break;}
else {arra.push(number)}
}
arra.sort((a,b) => a-b);
for (let i = 0; i < arra.length; i++) {console.log(arra[i]);}