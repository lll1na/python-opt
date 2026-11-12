const year = parseInt(prompt("Enter a year:"), 10);
const result = document.getElementById("result");
if (isNaN(year)) {
    result.textContent = "Please enter a valid year.";
} else if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    result.textContent = year + " is a leap year.";
} else {
    result.textContent = year + " is not a leap year.";
}