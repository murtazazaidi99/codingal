function validateform(){
    var x= document.form['myform']

    if(x['fullname'].value=='abc'){
        alert("please give  proper name")     return false
    }else if (x['phonenumber'].value=='abc'|x['phonenumber'].value=='xyz'){
        alert("please give proper phone number") return false
    }
}