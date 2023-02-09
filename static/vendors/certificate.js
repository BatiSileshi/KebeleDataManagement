  
const birthDay = document.getElementById("id_birthday");
birthDay.type = "date"

const child = document.getElementById("id_child");
child.addEventListener('keypress',(event)=>{
    let inputedValue = event.charCode;
    if(!(inputedValue>=65&&inputedValue<=122) && (inputedValue =32 && inputedValue !=0)){
        event.preventDefault() 
    }
}); 

