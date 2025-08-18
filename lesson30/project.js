function validateform(){
    var x= document.form['myform']

    if(x['fullname'].value=='abc'){
        alert("please give  proper name")     return false
    }else if (x['addressnumber'].value=='abc'|x['addressnumber'].value=='xyz'){
        alert("please give proper address number") return false
    }
}