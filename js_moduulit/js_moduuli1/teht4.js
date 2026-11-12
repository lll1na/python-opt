const name = prompt("What is your name?");
const number = Math.floor(Math.random() * 4) + 1;
let house;
switch (number) {
    case 1:
        house = "Gryffindor";
        break;
    case 2:
        house = "Slytherin";
        break;
    case 3:
        house = "Hufflepuff";
        break;
    default:
        house = "Ravenclaw";
}
document.getElementById("result").textContent = name + ", you are " + house + ".";