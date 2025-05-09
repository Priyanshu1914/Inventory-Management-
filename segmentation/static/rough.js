// Access form elements
const csvUploadInput = document.getElementById("csv-upload");
const addCsvButton = document.querySelector(".add-csv-btn");
const uploadForm = document.getElementById("upload-form");

// Show file dialog on button click
addCsvButton.addEventListener("click", () => {
  csvUploadInput.click();
});

// Handle form submission
uploadForm.addEventListener("submit", event => {
  event.preventDefault(); // Prevent page reload
  const file = csvUploadInput.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = () => {
      const csvData = reader.result;
      console.log("CSV Data:", csvData); // Log CSV data for debugging
      alert("CSV processed successfully!");
    };
    reader.readAsText(file);
  } else {
    alert("Please upload a valid CSV file.");
  }
});