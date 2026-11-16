'use strict';
     const int_1 = prompt('Give int 1.');
     const int_2 = prompt('Give int 2.');
     const int_3 = prompt('Give int 3.');
     const sum = parseInt(int_1) + parseInt(int_2) + parseInt(int_3);
     document.querySelector('#head').innerHTML = 'sum is, ' + sum + '.';