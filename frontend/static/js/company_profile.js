let originalData = {};
let currentTaskId = null;


document.addEventListener('DOMContentLoaded', () => {

    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }


    const editForm = document.getElementById('orderEditForm');
    if (editForm) {
        editForm.addEventListener('input', function() {
            const currentData = {
                status: document.getElementById('modalStatus').value,
                progress: document.getElementById('modalProgress').value,
                technical: document.getElementById('modalTechnical').value,
                driver: document.getElementById('modalDriver').value
            };

            const hasChanges = Object.keys(originalData).some(key => originalData[key] !== currentData[key]);
            const saveBtn = document.getElementById('saveBtn');
            if (saveBtn) saveBtn.style.display = hasChanges ? 'block' : 'none';
        });

        editForm.onsubmit = async function(e) {
            e.preventDefault();

            const saveBtn = document.getElementById('saveBtn');
            saveBtn.innerText = "Сохранение...";
            saveBtn.disabled = true;

            const updatePayload = {
                status: document.getElementById('modalStatus').value,
                progress: parseInt(document.getElementById('modalProgress').value),
                technical: document.getElementById('modalTechnical').value || null,
                driver: document.getElementById('modalDriver').value || null
            };

            try {
                const response = await fetch(`/api/v1/tasks/${currentTaskId}`, {
                    method: 'PATCH',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(updatePayload)
                });

                if (response.ok) {
                    window.location.reload();
                } else {
                    const error = await response.json();
                    alert("Ошибка сохранения: " + (error.detail || "Сервер отклонил запрос"));
                }
            } catch (err) {
                console.error(err);
                alert("Ошибка сети. Проверьте соединение с сервером.");
            } finally {
                saveBtn.innerText = "Сохранить изменения";
                saveBtn.disabled = false;
            }
        };
    }
});

document.addEventListener('click', function(e) {
    const btn = e.target.closest('.open-modal-btn');
    if (btn) {
        const order = JSON.parse(btn.getAttribute('data-order'));
        currentTaskId = order.id;

        originalData = {
            status: order.status || "Заявка создана",
            progress: String(order.progress || 0),
            technical: order.technical || "",
            driver: order.driver || ""
        };

        document.getElementById('modalTitle').innerText = order.title || 'Заказ без названия';
        document.getElementById('modalWork').innerText = order.work || '-';
        document.getElementById('modalPrice').innerText = (order.price || 0) + ' ₽';
        document.getElementById('modalCity').innerText = order.city || '-';
        document.getElementById('modalPhone').innerText = order.phone || '-';
        document.getElementById('modalAddress').innerText = order.address || 'Адрес не указан';
        document.getElementById('modalText').innerText = order.text || 'Нет описания';

        document.getElementById('modalStatus').value = originalData.status;
        document.getElementById('modalProgress').value = originalData.progress;
        document.getElementById('modalTechnical').value = originalData.technical;
        document.getElementById('modalDriver').value = originalData.driver;

        document.getElementById('saveBtn').style.display = 'none';
        document.getElementById('orderModal').style.display = 'flex';
    }
});


function closeModal() {
    const modal = document.getElementById('orderModal');
    if (modal) modal.style.display = 'none';
}

window.onclick = function(event) {
    const modal = document.getElementById('orderModal');
    if (event.target === modal) closeModal();
};