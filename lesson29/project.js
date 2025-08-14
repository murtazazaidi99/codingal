//json:javascript object notation
//var a={name:'zaiid',age:23,height:6,gun:true,look:'good'}

//console.log(a)

//var b=JSON.stringify(a)

//console.log(b)

//var c=JSON.parse(b)

//console.log(c)

console.log("starting")
setTimeout(()=>{
    console.log("work done,yehhoo")
},6000)

console.log("end")

var p=new Promise((resolve,reject)=>{
    setTimeout(()=>{resolve(" finnaly i won the match ")},8000)
})

p.then((data)=>console.log(data)).catch(err=>console.log("opps you were not win", err))