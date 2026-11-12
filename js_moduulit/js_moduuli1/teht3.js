const a = parseInt(prompt("Enter the first integer:"), 10);
const b = parseInt(prompt("Enter the second integer:"), 10);
const c = parseInt(prompt("Enter the third integer:"), 10);
if (isNaN(a) || isNaN(b) || isNaN(c)) {
    document.getElementById("sum").textContent = "Please enter valid integers.";
} else {
    const sum = a + b + c;
    const product = a * b * c;
    const average = sum / 3;
    document.getElementById("sum").textContent = "Sum: " + sum;
    document.getElementById("product").textContent = "Product: " + product;
    document.getElementById("average").textContent = "Average: " + average;
}