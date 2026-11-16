'use strict';
     const burning_question = confirm('Should I calculate the square root?');
     if (burning_question) {document.querySelector('#head').innerHTML = Math.sqrt(parseInt(prompt('give number'))) + ' is your square.';}
     else                  {document.querySelector('#head').innerHTML = 'The square root is not calculated.';}
