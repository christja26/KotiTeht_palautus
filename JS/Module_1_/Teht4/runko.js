'use strict';
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}
     const name = prompt('Give your name.');
     const number = getRandomInt(4);
     switch (number) {
    case 0:
        document.querySelector('#head').innerHTML = name + ', you are Gryffindor.';break;
    case 1:
        document.querySelector('#head').innerHTML = name + ', you are Slytherin.';break;
    case 2:
        document.querySelector('#head').innerHTML = name + ', you are Hufflepuff.';break;
    case 3:
        document.querySelector('#head').innerHTML = name + ', you are Ravenclaw.';break;
     }