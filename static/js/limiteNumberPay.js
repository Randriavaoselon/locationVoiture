const input = document.getElementsByName('total')[0];
const min = input.getAttribute('min');
input.onkeypress = e => {
// 13: enter, +: 43 , -: 45
if (13 == e.keyCode ) input.blur();
if ([43, 45].includes(e.keyCode)) return false;
};

input.onkeyup = e => {
// Valeur inférieure au minimum
if (parseFloat(input.value) < min) {
input.value = min;
}
else if (0 != input.value % 1) {
input.value = Math.floor(input.value);
}
else {
   input.value = parseFloat(input.value);
}
};