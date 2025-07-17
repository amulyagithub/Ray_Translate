// document.getElementById("uploadForm").addEventListener("submit", function(event) {
//     event.preventDefault();  // Prevent the default form submission

//     const formData = new FormData(this);  // Create FormData object from the form

//     // Send the form data to the server using fetch
//     fetch("/upload", {
//         method: "POST",
//         body: formData
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Handle success or error response from the server
//         const resultDiv = document.getElementById("result");
//         if (data.message) {
//             resultDiv.innerHTML = `<p>Success: ${data.message}</p>`;
//         } else if (data.error) {
//             resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
//         }
//     })
//     .catch(error => {
//         // Handle any unexpected errors
//         const resultDiv = document.getElementById("result");
//         resultDiv.innerHTML = `<p>Error: ${error}</p>`;
//     });
// });

document.getElementById("uploadForm").addEventListener("submit", function(event) {
    event.preventDefault(); 

    const form = this;
    const formData = new FormData(form);
    const resultDiv = document.getElementById("result");
    const submitButton = form.querySelector("button");

    
    resultDiv.innerHTML = "";
    resultDiv.style.opacity = 0;

    
    submitButton.disabled = true;
    submitButton.innerText = "Uploading...";

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            resultDiv.innerHTML = `<p class="success">✅ ${data.message}</p>`;
        } else if (data.error) {
            resultDiv.innerHTML = `<p class="error">❌ ${data.error}</p>`;
        }
        fadeIn(resultDiv);
    })
    .catch(error => {
        resultDiv.innerHTML = `<p class="error">❌ Unexpected Error: ${error}</p>`;
        fadeIn(resultDiv);
    })
    .finally(() => {
        submitButton.disabled = false;
        submitButton.innerText = "Upload and Translate";
    });
});


function fadeIn(element) {
    element.style.transition = "opacity 0.5s ease";
    element.style.opacity = 1;
}
