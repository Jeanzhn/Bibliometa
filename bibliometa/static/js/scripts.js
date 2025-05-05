function logout() {
  window.location.href = "/logout";
}

function login() {
  window.location.href = "/login";
}

function register() {
  window.location.href = "/login";
}

function lists(){
  window.location.href="/lists";
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

function emprestarConfirm(button) {
  const confirmDiv = button.nextElementSibling;
  button.style.display = 'none';
  confirmDiv.style.display = 'block';
}

function confirmEmpresta(button) {
  const bookCard = button.closest('.book-card');
  const titulo = bookCard.querySelector('.book-card__title').textContent;
  const isbn = bookCard.querySelector('[data-isbn]').getAttribute('data-isbn');
  
  fetch('/emprestar', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ titulo: titulo, isbn: isbn })
  })
  .then(response => response.json())
  .then(data => {
    if(data.success) {
      alert(`Livro "${titulo}" emprestado com sucesso!`);
      location.reload();
    } else {
      alert('Erro ao emprestar livro');
    }
  });
}

function cancelEmpresta(button) {
  const confirmDiv = button.closest('.confirm-emprestar');
  const borrowBtn = confirmDiv.previousElementSibling;
  confirmDiv.style.display = 'none';
  borrowBtn.style.display = 'block';
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
