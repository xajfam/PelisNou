function sortTable(columnIndex) {
    const tableBody = document.getElementById("movieTableBody");
    const rows = Array.from(tableBody.rows);

    // Determina si cal ordenar ascendent o descendent
    const currentOrder = tableBody.dataset.sortOrder === "asc" ? "desc" : "asc";
    tableBody.dataset.sortOrder = currentOrder;

    // Ordena les files
    rows.sort((a, b) => {
        const aText = a.cells[columnIndex].innerText;
        const bText = b.cells[columnIndex].innerText;

        if (!isNaN(aText) && !isNaN(bText)) {
            // Ordenació numèrica
            return currentOrder === "asc" ? aText - bText : bText - aText;
        } else {
            // Ordenació alfabètica
            return currentOrder === "asc"
                ? aText.localeCompare(bText)
                : bText.localeCompare(aText);
        }
    });

    // Reorganitza les files a la taula
    rows.forEach(row => tableBody.appendChild(row));
}
