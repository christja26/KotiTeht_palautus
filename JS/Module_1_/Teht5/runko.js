'use strict';
     const year = parseInt(prompt('Give a year.'));
    if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {document.querySelector('#head').innerHTML = year + ', is LeapyEar.';}
    else                                                            {document.querySelector('#head').innerHTML = year + ', is  not LeapyEar.';}
