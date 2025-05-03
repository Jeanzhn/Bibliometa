document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registerForm');
    const inputs = form.querySelectorAll('input[required]');
    const cadastrarBtn = document.getElementById('cadastrarBtn');

    function validarCampos() {
        const todosPreenchidos = Array.from(inputs).every(input => input.value.trim() !== '');
        const senha = document.getElementById('senha').value;
        const confirmarSenha = document.getElementById('confirmar_senha').value;
        const senhasCoincidem = senha === confirmarSenha;
        cadastrarBtn.disabled = !(todosPreenchidos && senhasCoincidem);
    }
    inputs.forEach(input => {
        input.addEventListener('input', validarCampos);
    });
});