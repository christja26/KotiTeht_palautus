'use strict';
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

     const die = parseInt(prompt('Give a number of die.'));
     let sum = 0;
     for (let i = 0;i != die;i++) {sum += getRandomInt(5) + 1;}
     document.querySelector('#head').innerHTML = sum + ' is sum.';