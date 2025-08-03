class  Animal{
    constructor(age,size,IQ,){
     this.age=age
     this.size=size
     this.IQ=IQ
    }
}
class shark extends Animal{
 constructor(age ,size,IQ,color,name,teath,){
    this.age=age
    this.size=size
    this.color=color
    this.IQ=IQ
    this.name=name
    this.teath=teath
 }

}
var a1= new Animal(20,'big','small')
var a2= new Animal(15,'verysmall','medium')
var a3= new Animal(50,'medium','high')
var a4= new Animal(30,'small','small')

var ob2= new Animal(15,'verybig','high','gray','shark',28)

console.log(a1.size)
console.log(a2.IQ)
console.log(a3.age)
console.log(a4.size)
console.log(ob2.teath)
console.log(ob2.name)