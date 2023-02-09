

let errorFound=(valid_age ,phone_number)=>{
    document.getElementById('form').addEventListener("submit",function(event){
        if(valid_age && phone_number){
            document.myform.submit()   
        }
    
        else{
            event.preventDefault() 
            }
       });
    }






function validator(){

    document.getElementById('phone_number').addEventListener('input',()=>{
    let valid_phone_number = false
    let valid_age = false
        let  displayPhoneNumberError = document.getElementById("phone_number_error");
               let phone_number = document.getElementById('phone_number').value
               let  phone_number_length =  phone_number.toString().length
              
               if(phone_number_length  < 9){
                   displayPhoneNumberError.style.display = "block";
                   displayPhoneNumberError.innerHTML = `Invalid Phone Number: its only ${phone_number_length} check and correct` ;
                //    valid_phone_number = false
                }
           
           
               else if( phone_number_length   == 10 && phone_number.toString().charAt(0) != 0 ){
                   displayPhoneNumberError.style.display = "block";
                    displayPhoneNumberError.innerHTML = `Invalid Phone Number : Please Use This Format : 0912345678 or 912345678`;
                    // valid_phone_number = false       
                  }
           
           
               else if( phone_number_length  == 10 && phone_number.toString().charAt(0) == 0 ){
                   valid_phone_number = true
                   phone_number = parseInt(phone_number);
                   displayPhoneNumberError.style.display = "none";
                }
                   
           
               else if( phone_number_length  > 10){
                   displayPhoneNumberError.style.display = "block";
                    displayPhoneNumberError.innerHTML = "Invalid Phone Number: Please Insert In This Format : 0912345678 or 912345678 ";
                    // valid_phone_number = false
                 }
           
           
             else {
                   displayPhoneNumberError.style.display = "none";
       
             }
             errorFound(valid_age,valid_phone_number)  
          
            });
       
           const firstname = document.getElementById("id-first-name");
      firstname.addEventListener('input',(e)=>{
            // firstname.addEventListener("keydown", keyHandler);
            firstname.setAttribute('pattern',"[A-Za-z]+");


           // function keyHandler(e) {
           //   if (e.which === 32) {
           //     this.value = this.value.replace(/\s/g, "");
           //     return false;
           //   }
           // }
 });
          
 const middlename = document.getElementById("id-middlename");
 middlename.addEventListener('input',(e)=>{
         // firstname.addEventListener("keydown", keyHandler);
         middlename.setAttribute('pattern',"[A-Za-z]+");


        // function keyHandler(e) {
        //   if (e.which === 32) {
        //     this.value = this.value.replace(/\s/g, "");
        //     return false;
        //   }
        // }
 });
           const lastname = document.getElementById("id-lastname");
         lastname.addEventListener('input',(e)=>{
                 // firstname.addEventListener("keydown", keyHandler);
                 lastname.setAttribute('pattern',"[A-Za-z]+");
     
     
                // function keyHandler(e) {
                //   if (e.which === 32) {
                //     this.value = this.value.replace(/\s/g, "");
                //     return false;
                //   }
                // }
     
     
     
                });
       
                const mothername = document.getElementById("id-mothername");
                mothername.addEventListener('input',(e)=>{
                        // firstname.addEventListener("keydown", keyHandler);
                        mothername.setAttribute('pattern',"[A-Za-z]+");
                         if (e.which === 32) {
                        //    this.value = this.value.replace(/\s/g, "");
                        //    return false;
                        this.value += " ";
                         }
     
                       });           
                       


                const age = document.getElementById("id-age");
                age.addEventListener('input',(e)=>{

                        age.setAttribute('pattern',"[0-9]+");
                         if (age.value < 18 || age.value > 150 ) {
                            valid_age = false;
                         }
                         else{
                            valid_age = true;
                         }
                         
     
errorFound(valid_age,valid_phone_number);       
                       });      

}

validator();