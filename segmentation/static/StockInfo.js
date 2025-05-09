// Object to hold stock information
let stockData = {};

// Function to update or add stock
function updateStock() {
    const productId = document.getElementById("product-id").value.trim();
    const quantity = parseInt(document.getElementById("quantity").value.trim());

    if (!productId || isNaN(quantity) || quantity < 0) {
        alert("Please enter a valid Product ID and Quantity.");
        return;
    }

    // Update or add the product to stockData
    if (stockData[productId]) {
        stockData[productId] += quantity; // Add quantity to existing stock
    } else {
        stockData[productId] = quantity; // Add new product to stock
    }

    // Clear input fields
    document.getElementById("product-id").value = "";
    document.getElementById("quantity").value = "";

    // Refresh the stock table
    refreshStockTable();
}

// Function to refresh the stock table
function refreshStockTable() {
    const tableBody = document.getElementById("stock-table");
    tableBody.innerHTML = ""; // Clear existing rows

    // Populate table with stock data
    for (const productId in stockData) {
        const row = document.createElement("tr");

        const idCell = document.createElement("td");
        idCell.textContent = productId;

        const quantityCell = document.createElement("td");
        quantityCell.textContent = stockData[productId];

        row.appendChild(idCell);
        row.appendChild(quantityCell);
        tableBody.appendChild(row);
    }
}

// Event listener for update button
document.getElementById("update-stock").addEventListener("click", updateStock);
