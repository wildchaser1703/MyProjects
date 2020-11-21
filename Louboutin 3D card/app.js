//Movement animation to happen
const card = document.querySelector(".card");
const container = document.querySelector(".container");
//Items
const title = document.querySelector('.title');
const shoes = document.querySelector('.shoes img');
const purchase = document.querySelector('.purchase button');
const description = document.querySelector('.info h3');
const sizes = document.querySelector('.sizes');


//Moving Animation Event
container.addEventListener("mousemove", e => {
    let xAxis = (window.innerWidth / 2 - e.pageX) / 25;
    let yAxis = (window.innerHeight / 2 - e.pageY) / 25;
    card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
});

//When mouse starts to hover
container.addEventListener("mouseenter", e => {
    card.style.transition = "none";
    shoes.style.transform = "translateZ(200px) rotate(-15deg)";
    title.style.transform = "translateZ(100px)";
    description.style.transform = "translateZ(75px)";
    sizes.style.transition = "translateZ(75px)";
    purchase.style.transform = "translateZ(75px)";
});

//put the container back in place after hovering
container.addEventListener("mouseleave", e => {
    card.style.transform = `rotateY(0deg) rotateX(0deg)`;
    card.style.transition = "all 0.5s ease";
    shoes.style.transform = "translateZ(0px) rotate(0deg)";
    title.style.transform = "translateZ(0px)";
    description.style.transform = "translateZ(0px)";
    sizes.style.transition = "translateZ(0px)";
    purchase.style.transform = "translateZ(0px)";
});

