// window.onload() = function(){
//     let adds = document.getElementById("page-counter");
// }
let adds = document.getElementById("page-counter");
console.log(adds)
let count = 0;
function increasement(){
    count = count + 1;
    adds.innerText = count;
}
function toggleActive(element) {
    element.classList.toggle("active");
}

