var a=[100,2,-60,43,54,56,71,0,-2]

a.sort(function(a,b){return a-b})

a.sort((a,b)=>a-b)
console.log(a)

a.sort((a,b)=>b-a)
console.log(a)

console.log(a.map(e=>e*20))

console.log(a.map(function(e){return e*20}))

function meo(){
    var x=12
    var y=14
    var z=72

    var a=eval("x+y")
    var b=eval("10*3+z")
    var c=eval("2-4+x+y+z")

    console.log(a)
    console.log(b)        
    console.log(c)
}
meo()