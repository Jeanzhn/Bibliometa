function logout() {
<<<<<<< HEAD
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
=======
    alert("Você saiu da conta!");
    window.location.href = "/logout";
}

function searchBook() {
    const input = document.getElementById("searchInput").value.toLowerCase();
    const cards = document.querySelectorAll(".book-card");
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
>>>>>>> 1e2e812574405ef881ee2d99d2c854746fd86e9c
    const checkboxes = document.querySelectorAll(".select-book");
    const confirmDelete = document.getElementById("confirmDelete");
    const isVisible = confirmDelete.style.display === "block";
    checkboxes.forEach(checkbox => checkbox.style.display = isVisible ? "none" : "inline-block");
    confirmDelete.style.display = isVisible ? "none" : "block";
<<<<<<< HEAD
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
=======
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
>>>>>>> 1e2e812574405ef881ee2d99d2c854746fd86e9c
    event.preventDefault();
    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;
    const card = document.createElement("div");
    card.className = "book-card";
    card.innerHTML = `
<<<<<<< HEAD
      <input type="checkbox" class="select-book" style="display:none"/>
=======
      <input type="checkbox" class="select-book" />
>>>>>>> 1e2e812574405ef881ee2d99d2c854746fd86e9c
      <h3>${titulo}</h3>
      <p>${autor}</p>
    `;
    document.getElementById("bookList").appendChild(card);
    document.getElementById("titulo").value = "";
    document.getElementById("autor").value = "";
    document.getElementById("formularioLivro").style.display = "none";
<<<<<<< HEAD
  }
=======
}
>>>>>>> 1e2e812574405ef881ee2d99d2c854746fd86e9c
