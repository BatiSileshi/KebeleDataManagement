
const businesName = document.getElementById("id_name");
businesName.addEventListener('keypress',(event)=>{
      let inputedValue = event.charCode;
      if(!(inputedValue>=65&&inputedValue<=122) && (inputedValue =32 && inputedValue !=0)){
          event.preventDefault() 
      }
});
    
const businesType = document.getElementById("id_type");
businesType.addEventListener('keypress',(event)=>{
    let inputedValue = event.charCode;
    if(!(inputedValue>=65&&inputedValue<=122) && (inputedValue = 32 && inputedValue !=0)){
        event.preventDefault() 
    }
   
});
            
                 