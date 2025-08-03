var a=[10,22,-54,72,-110,78,98,65]

a.sort(function(a,b){return a-b})

a.sort((a,b)=>a-b)
console.log(a)

a.sort((a,b)=>b-a)
console.log(a)

console.log(a.map(e=>e*22))

console.log(a.map(function(e){return e*22}))

function meo(){
    var x=100
    var y=120
    var z=720

    var a=eval("x+y")
    var b=eval("10*3+z")
    var c=eval("2-4+x+y+z")

    console.log(a)
    console.log(b)        
    console.log(c)
}