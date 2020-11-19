const colors = ["green", "red", "rgba(133,122,200)", "#f15025"];
const btn = document.getElementById("btn");
const color = document.querySelector(".color");

btn.addEventListener('click', function () {
    // get random number between between 0-3 of the array
    const randomNumber = getRandomNumber();
    console.log(randomNumber);
    document.body.style.backgroundColor = colors[randomNumber];
    color.textContent = colors[randomNumber];

    /*
    const randomNumber = 2;
    document.body.style.backgroundColor = colors[randomNumber];

    // display the background color code
    color.textContent = colors[randomNumber];

    The above line displays rgba(133,122,200) and a lilac background.
    */

});

// randomNumber generatesa number between 0 and 1 only
// Multiply this random number generated with the length of the array
// Now we can get the numbers between 0-3


function getRandomNumber() {
    return Math.floor(Math.random() * colors.length);
}

//Use floor to round the value to a closest integer
// Math.floor(Math.random() * colors.length); gives all colors in the colours array


