
document.getElementById("id_emergency_contact").type = "number";
const emergency = document.getElementById("id_emergency");
emergency.addEventListener('keypress',(event)=>{
      let inputedValue = event.charCode;
      if(!(inputedValue>=65&&inputedValue<=122) && (inputedValue =32 && inputedValue !=0)){
          event.preventDefault() 
      }
});          
let errorFound=(phone_number)=>{
    console.log(phone_number);
    document.getElementById('form').addEventListener("submit",function(event){
        if(phone_number){
            document.myform.submit()   
        }
    
        else{
            event.preventDefault() 
     
            }
       });
    }


function validator(){
    let valid_phone_number = false
    document.getElementById('id_emergency_contact').addEventListener('input',()=>{
        let  displayPhoneNumberError = document.getElementById("phone_number_error");
               let phone_number = document.getElementById('id_emergency_contact').value
               let  phone_number_length =  phone_number.toString().length
              
               if(phone_number_length  < 9){
                
                   displayPhoneNumberError.style.display = "block";
                   displayPhoneNumberError.innerHTML = `Invalid Phone Number: its only ${phone_number_length} check and correct` ;
                   valid_phone_number = false
                }
           
           
               else if( phone_number_length   == 10 && phone_number.toString().charAt(0) != 0 ){
                   displayPhoneNumberError.style.display = "block";
                    displayPhoneNumberError.innerHTML = `Invalid Phone Number : Please Use This Format : 0912345678 or 912345678`;
                    valid_phone_number = false       
                  }
           
           
               else if( phone_number_length  == 10 && phone_number.toString().charAt(0) == 0 ){
                   valid_phone_number = true
                   phone_number = parseInt(phone_number);
                   displayPhoneNumberError.style.display = "none";
                }
                   
           
               else if( phone_number_length  > 10){
                   displayPhoneNumberError.style.display = "block";
                    displayPhoneNumberError.innerHTML = "Invalid Phone Number: Please Insert In This Format : 0912345678 or 912345678 ";
                    valid_phone_number = false
                 }
           
           
             else {
                   displayPhoneNumberError.style.display = "none";
       
             }
             errorFound(valid_age,valid_phone_number)  
          
            });    
errorFound(valid_phone_number);       
                       
}

validator();