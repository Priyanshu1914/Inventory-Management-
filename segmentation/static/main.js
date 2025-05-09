let stockData = [];
function addStock() {
  const productId = document.getElementById('product_id').value;
  const stockQuantity = parseInt(document.getElementById('stock_quantity').value, 10);

  if (!productId || isNaN(stockQuantity)) {
    alert('Please provide valid inputs.');
    return;
  }

  const existingProduct = stockData.find(item => item.productId === productId);
  if (existingProduct) {
    existingProduct.stockQuantity = stockQuantity;
  } else {
    stockData.push({ productId, stockQuantity });
  }
  updateStockTable();
}

function updateStockTable() {
  const tableBody = document.getElementById('stock-table-body');
  tableBody.innerHTML = '';
  stockData.forEach(item => {
    tableBody.innerHTML += `<tr><td>${item.productId}</td><td>${item.stockQuantity}</td></tr>`;
  });
}

function processSales() {
  const fileInput = document.getElementById('csv-upload');
  if (!fileInput.files.length) {
    alert('Please upload a CSV file.');
    return;
  }

  const file = fileInput.files[0];
  const reader = new FileReader();

  reader.onload = function (event) {
    const csvData = event.target.result;
    const rows = csvData.split('\n');
    rows.forEach(row => {
      const [productId, quantity] = row.split(',');
      const stockItem = stockData.find(item => item.productId === productId);
      if (stockItem) {
        stockItem.stockQuantity -= parseInt(quantity, 10);
      }
    });
    updateStockTable();
    showResults();
  };

  reader.readAsText(file);
}

function showResults() {
  document.getElementById('results').classList.remove('hidden');
}

function showSection(sectionId) {
  document.querySelectorAll('.hidden-section').forEach(section => {
    section.classList.add('hidden');
  });
  document.getElementById(sectionId).classList.remove('hidden');
}

function goToHome() {
  // Hide all sections
  document.querySelectorAll('.hidden-section').forEach(section => {
    section.classList.add('hidden');
  });

  // Show the Upload Section
  const uploadSection = document.querySelector('.upload-section');
  uploadSection.scrollIntoView({ behavior: 'smooth' }); // Scroll to the section
}