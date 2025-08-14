var a=56
console.log(typeof(a))

a=Number(a)

console.log(typeof(a))

console.log(typeof(NaN))

var b=[3,6,9,12]

console.log(typeof(b))

try{
    //error
    console.log("zaidi")
}catch(err){
    console.log("handling the err")
    console.log("err")
}

console.log("very important thing")
console.log("can you sned me")


function play(x,y,z,a){
    console.log("putting to play with football"+a)
    console.log("putting to play with football"+z)
    console.log("putting to play with football"+y)
    console.log("putting to play with football"+x)
}
play('zaidi','ali','murtaza','syed')

var play1 = a=>console.log("putting to play with football through play "+a)

play1('killer')