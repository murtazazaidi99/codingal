var a=49
console.log(typeof(a))

a=Number(a)

console.log(typeof(a))

console.log(typeof(NaN))

var b=[16,17,18,19]

console.log(typeof(b))

try{
    //error
    console.log("killer")
}catch(err){
    console.log("handling the err")
    console.log("err")
}

console.log("i request to you")
console.log("give me  a permission")


function drive(x,y,z,a){
    console.log("putting to drive a car" +a)
    console.log("putting to drive a car" +z)
    console.log("putting to drive a car" +y)
    console.log("putting to drive a car" +x)
}
drive('mickymouse','doramon','mrbeem','spiderman')

var drive1 = a=>console.log("putting to drive a car through drive "+a)

drive1('nakola')