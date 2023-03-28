function editProduct(e) {
  const productId = e.getAttribute("productId");
  fetch(`http://localhost:5500/products/${productId}`).then((resp) => {
    const response = resp.json();
    response.then((data) => {
      document.getElementById("edit_product_id").value = data.product_id;
      document.getElementById("edit_nama_produk").value = data.name;
      document.getElementById("edit_keterangan").value = data.description;
      document.getElementById("edit_harga").value = data.price;
      document.getElementById("edit_jumlah").value = data.stock;
    });
  });
}

function updateProduct() {
  const productId = document.getElementById("edit_product_id").value;
  const data = new FormData();
  data.append("nama_produk", document.getElementById("edit_nama_produk").value);
  data.append("keterangan", document.getElementById("edit_keterangan").value);
  data.append("harga", document.getElementById("edit_harga").value);
  data.append("jumlah", document.getElementById("edit_jumlah").value);
  fetch(`http://localhost:5500/products/${productId}`, {
    method: "PUT",
    body: data,
  }).then(() => {
    window.location = "http://localhost:5500";
  });
}

function deleteProduct(e) {
  const productId = e.getAttribute("productId");
  fetch(`http://localhost:5500/products/${productId}`, {
    method: "DELETE",
  }).then(() => {
    window.location = "http://localhost:5500";
  });
}
