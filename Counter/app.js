// set initial count
let count = 0;
//select value spans and all the buttons
//selct all the buttons using the querySelectrorAll
//where all the buttons have the generic btn class
const value = document.querySelector("#value");         //id name is value
const btns = document.querySelectorAll(".btn");


//use for each method to call for the items in each and every list
//e is the event object
btns.forEach(function (btn) {
    btn.addEventListener("click", function (e) {
        const styles = e.currentTarget.classList;
        if (styles.contains("decrease")) {
            count--;
        }
        else if (styles.contains("increase")) {
            count++;
        }
        else {
            count = 0;
        }
        if(count > 0){
            value.style.color = "green";
        }
        if(count < 0){
            value.style.color = "red";
        }
        value.textContent = count;
    });
});






