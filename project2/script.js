const numberbuttons=document.querySelectorAll('.number')
const operatorbuttons=document.querySelectorAll('.operator')
const display=document.querySelector('.display')

let currentInput=''
let previousInput=''
let operator=null

function updateDisplay(v){
    display.innerText= v
}

numberbuttons.forEach(b =>{
    b.addEventListener('click',()=>{
        currentInput =currentInput+b.id
        updateDisplay(currentInput)
    })
})