// document.addEventListener('DOMContentLoaded', function() {
//     const form = document.getElementById('summarizeForm');  // Change the id to 'summarizeForm'
//     const button = document.getElementById('my-button');

//     button.addEventListener('click', function() {
//         form.submit();
//     });
// });
// function showError(errorElement, errorMessage){
//     document.querySelector("."+errorElement).classList.add("display-error");
//     document.querySelector("."+errorElement).innerHTML = errorMessage;
// }
// function clearError(){
//     let errors = document.querySelectorAll(".error");
//     for(let error of errors){
//         error.classList.remove("display-error");
//     }
// }
// let form = document.forms['main-input'];
// form.onsubmit = function(event){
//     clearError();
//     if(form.input_text.value === "" || form.selectModel.value === "" || form.selectLength == ""){
//         showError('email-error', "Please enter information ");
//         return false;
//     }

//     event.preventDefault();
    
// }


document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('summarizeForm');  // Change the id to 'summarizeForm'
    const button = document.getElementById('my-button');
    var inputText = document.getElementById('input_text').value;
    var selectModel = document.getElementById('selectModel').value;
    var selectLength = document.getElementById('selectLength').value;
    var errorInput = document.getElementById('error email-error');

    button.addEventListener('click', function() {
        if (inputText.trim() === '' || selectModel === '' || selectLength === '') {
                    errorInput.innerHTML("Please Check Information Again")
                } else {
                    errorInput.innerHTML("");
            
                    // Gọi hàm để submit form
                    form.submit();
                }
    });
});

// function validateAndSubmit() {
//     var rawtext = document.getElementById("input_text").value;
//     var errorMessage = document.getElementById("error-message");

//     if (rawtext.trim() === "") {
//         errorMessage.innerHTML = "Please enter information into the textarea.";
//     } else {
//         errorMessage.innerHTML = "";
//         document.getElementById("summarizeForm").submit();
//     }
// }


// function back() {
//     // Redirect to the home page (replace '/' with your actual route)
//     window.location.href = '/';
// }

// // Attach the function to the click event of the button
// document.getElementById('backButton').addEventListener('click', back);

// function validateAndSubmit(){
//     var inputtext = document.getElementById('input-text');
//     var selectM = document.getElementById('selectModel');
//     var selectL = document.getElementById('selectLength');
//     var errorInput = document.getElementById('error-input-text');
//     var errorSelect = document.getElementById('error-select');

//     if (inputtext.value === ''|| selectM.value === "Select Model" || selectM === "Select Summary Length"){
//         errorInput.style.display = 'block';
//     }
//     else {
//         document.addEventListener('DOMContentLoaded', function() {
//             const form = document.getElementById('summarizeForm');  // Change the id to 'summarizeForm'
//             const button = document.getElementById('my-button');
        
//             button.addEventListener('click', function() {
//                 form.submit();
//             });
//         });
//     }
// }

// function validateAndSubmit() {
//     var inputText = document.getElementById('input_text').value;
//     var selectModel = document.getElementById('selectModel').value;
//     var selectLength = document.getElementById('selectLength').value;
//     var errorInput = document.getElementById('error-input-text');

//     if (inputText.trim() === '' || selectModel === 'Select Model' || selectLength === 'Select Summary Length') {
//         errorInput.innerHTML("Please Check Information Again")
//     } else {
//         errorInput.innerHTML("");

//         // Gọi hàm để submit form
//         submitForm();
//     }
// }

// function submitForm() {
//     document.getElementById('summarizeForm').submit();
// }
