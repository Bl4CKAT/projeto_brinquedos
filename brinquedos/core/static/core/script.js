function confirmarExclusao (event) {
    if (!confirm("Você tem certeza que deseja excluir esse brinquedo?")){
        event.preventDefault();
    }
}

window.addEventListener("DOMContentLoaded", () => {
    const params = new URLSearchParams(window.location.search);
    if (params.get("added") === "true") {
        alert("Brinquedo adicionado com sucesso!");
    }
});

