
const houseNumber= document.getElementById("id_hnum");
houseNumber.addEventListener('keypress',(event)=>{
      let inputedValue = event.charCode;
      if(inputedValue === 32 ){
          event.preventDefault() 
      }
});  
const area = document.getElementById("id_area");
area.addEventListener('keypress',(event)=>{
      let inputedValue = event.charCode;
      if(!(inputedValue>=48&&inputedValue<=57)&& (inputedValue!=46)){
          event.preventDefault() 
      }
}); 

