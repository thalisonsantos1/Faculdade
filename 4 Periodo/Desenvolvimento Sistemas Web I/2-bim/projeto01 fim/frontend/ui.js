// UI utilities: showAlert(message, type) and confirmAction(message) -> Promise<boolean>
(function(){
    // Create alert container - CENTERED
    function ensureAlertContainer(){
        let c = document.getElementById('alert-container');
        if (!c){
            c = document.createElement('div');
            c.id = 'alert-container';
            c.style.position = 'fixed';
            c.style.top = '50%';
            c.style.left = '50%';
            c.style.transform = 'translate(-50%, -50%)';
            c.style.zIndex = 10800;
            c.style.maxWidth = '500px';
            c.style.width = '90%';
            document.body.appendChild(c);
        }
        return c;
    }

    function showAlert(message, type='success', timeout=15000){
        const c = ensureAlertContainer();
        const wrapper = document.createElement('div');
        const alertClass = type === 'danger' ? 'danger' : type;
        wrapper.innerHTML = `
            <div class="alert alert-${alertClass} alert-dismissible fade show shadow-lg" role="alert" style="margin-bottom: 0; border-radius: 0.5rem;">
                <strong>${type === 'success' ? '✓ Sucesso' : type === 'error' || type === 'danger' ? '✕ Erro' : type === 'warning' ? '⚠ Aviso' : 'ℹ Info'}:</strong> ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `;
        c.innerHTML = '';
        c.appendChild(wrapper);
        if (timeout > 0){
            setTimeout(()=>{
                try{ const bs = bootstrap.Alert.getOrCreateInstance(wrapper.querySelector('.alert')); bs.close(); }catch(e) { wrapper.remove(); }
            }, timeout);
        }
    }

    // Confirm modal generator
    function ensureConfirmModal(){
        let m = document.getElementById('confirm-modal');
        if (m) return m;
        m = document.createElement('div');
        m.id = 'confirm-modal';
        m.className = 'modal fade';
        m.tabIndex = -1;
        m.innerHTML = `
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Confirmação</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body"><p id="confirm-body">Mensagem</p></div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="button" class="btn btn-danger" id="confirm-yes">Confirmar</button>
                    </div>
                </div>
            </div>
        `;
        document.body.appendChild(m);
        return m;
    }

    function confirmAction(message){
        return new Promise((resolve)=>{
            const m = ensureConfirmModal();
            m.querySelector('#confirm-body').textContent = message;
            const modal = new bootstrap.Modal(m, { backdrop: 'static' });
            function cleanup(){
                m.querySelector('#confirm-yes').removeEventListener('click', onYes);
                m.removeEventListener('hidden.bs.modal', onHidden);
            }
            function onYes(){ cleanup(); modal.hide(); resolve(true); }
            function onHidden(){ cleanup(); resolve(false); }
            m.querySelector('#confirm-yes').addEventListener('click', onYes);
            m.addEventListener('hidden.bs.modal', onHidden);
            modal.show();
        });
    }

    window.showAlert = showAlert;
    window.confirmAction = confirmAction;
})();
