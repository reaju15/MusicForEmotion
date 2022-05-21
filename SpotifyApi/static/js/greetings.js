var english = 'Hello!';
var spanish = 'Hola!';
var french = 'Bonjour!';

//var myArray = [
//  "Hello!",
//  "Hola!",
//  "Bonjour"
//];
//
//var ranNumber = Math.floor(Math.random()*myArray.length)
//
//var randomItem = myArray[ranNumber];
//
//
//document.getElementById("greeting").textContent = ranNumber;

var x_greeting = document.getElementById("greeting");
var rand = Math.floor(Math.random() * 3);

if (rand == 0){
    greeting_out(english);
    } else if (rand == 1) {
    greeting_out(spanish);
    } else if (rand == 2) {
    greeting_out(french);
}

function greeting_out (language) {
    x_greeting.textContent = language;
}

//numberList = ["hello","hola","bonjour"]

//
//x_greeting.textContent = numberList;

//
//
//if (rand == 0){
//    x_greeting.textContent = english;
//    }else if (rand == 1) {
//    x_greeting.textContent = spanish;
//    }else if (rand == 2) {
//    x_greeting.textContent = french;
//    }