const apiUrl = "/users";
let users = [];

function setStatus(message, isError = false) {
    const status = document.getElementById("statusMessage");
    status.textContent = message;
    status.className = isError ? "mt-3 text-center text-danger" : "mt-3 text-center text-muted";
}

function formatValue(value) {
    return value ?? "-";
}

function renderUsers(list) {
    const tbody = document.getElementById("userTableBody");

    if (!list.length) {
        tbody.innerHTML = `
            <tr>
                <td colspan="5" class="text-center py-4">Nenhum usuário encontrado.</td>
            </tr>
        `;
        return;
    }

    tbody.innerHTML = list
        .map(user => `
            <tr>
                <td>${formatValue(user.idusuario)}</td>
                <td>${formatValue(user.nome)}</td>
                <td>${formatValue(user.email)}</td>
                <td>${formatValue(user.telefone)}</td>
                <td>
                    <button type="button" class="btn btn-sm btn-outline-primary me-2" onclick="editUser(${user.idusuario})">Editar</button>
                    <button type="button" class="btn btn-sm btn-outline-danger" onclick="deleteUser(${user.idusuario})">Excluir</button>
                </td>
            </tr>
        `)
        .join("\n");
}

function applyFilter(term) {
    const normalized = term.trim().toLowerCase();
    if (!normalized) {
        renderUsers(users);
        return;
    }
    const filtered = users.filter(user => {
        return [user.nome, user.email, user.telefone]
            .filter(Boolean)
            .some(value => value.toLowerCase().includes(normalized));
    });
    renderUsers(filtered);
}

function getFormData() {
    return {
        nome: document.getElementById("nameInput").value.trim(),
        email: document.getElementById("emailInput").value.trim(),
        telefone: document.getElementById("phoneInput").value.trim(),
    };
}

function showForm() {
    const wrapper = document.getElementById("userFormWrapper");
    if (wrapper) {
        wrapper.classList.add("show");
        wrapper.classList.remove("d-none");
        wrapper.style.display = "block";
    }
}

function hideForm() {
    const wrapper = document.getElementById("userFormWrapper");
    if (wrapper) {
        wrapper.classList.remove("show");
        wrapper.classList.add("d-none");
        wrapper.style.display = "none";
    }
}

function resetForm() {
    document.getElementById("userId").value = "";
    document.getElementById("nameInput").value = "";
    document.getElementById("emailInput").value = "";
    document.getElementById("phoneInput").value = "";
    document.getElementById("saveButton").textContent = "Salvar";
    setStatus("Pronto para criar um novo usuário.");
}

function populateForm(user) {
    document.getElementById("userId").value = user.idusuario ?? "";
    document.getElementById("nameInput").value = user.nome ?? "";
    document.getElementById("emailInput").value = user.email ?? "";
    document.getElementById("phoneInput").value = user.telefone ?? "";
    document.getElementById("saveButton").textContent = "Atualizar";
    setStatus(`Editando usuário ${formatValue(user.idusuario)}.`);
    showForm();
}

async function loadUsers() {
    setStatus("Carregando usuários...");
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`Erro ao carregar usu�rios: ${response.status} ${response.statusText}`);
        }
        users = await response.json();
        renderUsers(users);
        setStatus(`Exibindo ${users.length} usu�rio(s).`);
    } catch (error) {
        renderUsers([]);
        setStatus(error.message, true);
        console.error(error);
    }
}

async function saveUser(event) {
    event.preventDefault();
    const id = document.getElementById("userId").value;
    const payload = getFormData();

    if (!payload.nome || !payload.email) {
        setStatus("Nome e email são obrigatórios.", true);
        return;
    }

    const method = id ? "PUT" : "POST";
    const url = id ? `${apiUrl}/${id}` : apiUrl;

    try {
        const response = await fetch(url, {
            method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            const text = await response.text();
            throw new Error(text || `Falha ao salvar usu�rio (${response.status})`);
        }

        await loadUsers();
        resetForm();
        hideForm();
        setStatus(id ? "Usuário atualizado com sucesso." : "Usuário criado com sucesso.");
    } catch (error) {
        setStatus(error.message, true);
        console.error(error);
    }
}

function editUser(id) {
    const user = users.find(userEntry => Number(userEntry.idusuario) === Number(id));
    if (!user) {
        setStatus("Usuário não encontrado para edição.", true);
        return;
    }
    populateForm(user);
    window.scrollTo({ top: 0, behavior: "smooth" });
}

async function deleteUser(id) {
    if (!confirm("Deseja realmente excluir este usu�rio?")) {
        return;
    }

    try {
        const response = await fetch(`${apiUrl}/${id}`, { method: "DELETE" });
        if (!response.ok && response.status !== 204) {
            const text = await response.text();
            throw new Error(text || `Falha ao excluir usu�rio (${response.status})`);
        }
        await loadUsers();
        resetForm();
        setStatus("Usuário excluído com sucesso.");
    } catch (error) {
        setStatus(error.message, true);
        console.error(error);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    hideForm();

    const searchInput = document.getElementById("searchInput");
    const form = document.getElementById("userForm");
    const cancelButton = document.getElementById("cancelButton");

    if (searchInput) {
        searchInput.addEventListener("input", event => applyFilter(event.target.value));
    }
    if (form) {
        form.addEventListener("submit", saveUser);
    }
    if (cancelButton) {
        cancelButton.addEventListener("click", () => {
            resetForm();
            hideForm();
        });
    }

    const newUserButton = document.getElementById("newUserButton");
    if (newUserButton) {
        newUserButton.addEventListener("click", () => {
            resetForm();
            showForm();
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }

    loadUsers();
});
