function logout() {
    window.location.href = "/logout";
}

function login() {
    window.location.href = "/login";
}

  function searchBook() {
    const input = document.getElementById("searchInput").value.toLowerCase();
    const cards = document.querySelectorAll("book-card");
    cards.forEach(card => {
      const title = card.querySelector("h3").textContent.toLowerCase();
      card.style.display = title.includes(input) ? "block" : "none";
    });
  }

  function mostrarFormulario() {
    const form = document.getElementById("formularioLivro");
    form.style.display = form.style.display === "none" ? "block" : "none";
  }

  function toggleRemoveMode() {
    const checkboxes = document.querySelectorAll(".select-book");
    const confirmDelete = document.getElementById("confirmDelete");
    const isVisible = confirmDelete.style.display === "block";
    checkboxes.forEach(checkbox => checkbox.style.display = isVisible ? "none" : "inline-block");
    confirmDelete.style.display = isVisible ? "none" : "block";
  }

  function deleteSelectedBooks() {
    const selectedBooks = document.querySelectorAll(".select-book:checked");
    selectedBooks.forEach(book => {
      const card = book.parentElement;
      card.remove();
    });
    toggleRemoveMode(); 
  }

  function cancelDelete() {
    toggleRemoveMode();  
  }

  function addBook(event) {
    event.preventDefault();
    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;
    const card = document.createElement("div");
    card.className = "book-card";
    card.innerHTML = `
      <input type="checkbox" class="select-book" style="display:none"/>
      <h3>${titulo}</h3>
      <p>${autor}</p>
    `;
    document.getElementById("bookList").appendChild(card);
    document.getElementById("titulo").value = "";
    document.getElementById("autor").value = "";
    document.getElementById("formularioLivro").style.display = "none";
  }
