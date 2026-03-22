
let currentOrderToTakeId = null;


function openOrderModal(order) {
    const modal = document.getElementById('modalOverlay');


    currentOrderToTakeId = order.id;


    document.getElementById('modalBadge').textContent = order.work;
    document.getElementById('modalTitle').textContent = order.title;

    if (order.price && !isNaN(order.price)) {
        document.getElementById('modalPrice').textContent = Number(order.price).toLocaleString('ru-RU') + ' ₽';
    } else {
        document.getElementById('modalPrice').textContent = "Договорная";
    }

    document.getElementById('modalPhone').textContent = order.phone;
    document.getElementById('modalAddress').textContent = `г. ${order.city}, ${order.address}`;
    document.getElementById('modalRequired').textContent = order.required || 'Не указано';
    document.getElementById('modalText').textContent = order.text;


    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
}


function closeOrderModal() {
    const modal = document.getElementById('modalOverlay');
    if (modal) modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}


async function takeOrder() {
    if (!currentOrderToTakeId) {
        console.error("Ошибка: ID заказа не определен");
        return;
    }

    const btn = document.getElementById('takeOrderBtn');
    const originalText = btn.innerText;

    btn.innerText = "Оформление...";
    btn.disabled = true;

    try {
        const response = await fetch(`/api/v1/tasks/${currentOrderToTakeId}/take/`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                status: "Принято",
                progress: 0
            })
        });

        if (response.ok) {
            alert("Заказ успешно взят в работу!");
            window.location.reload();
        } else {
            const error = await response.json();
            alert("Ошибка: " + (error.detail || "Не удалось взять заказ"));
        }
    } catch (err) {
        console.error("Ошибка сети:", err);
        alert("Ошибка сети. Проверьте соединение с сервером.");
    } finally {
        btn.innerText = originalText;
        btn.disabled = false;
    }
}

document.addEventListener('DOMContentLoaded', () => {

    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    const serviceWindow = document.getElementById('serviceAppWindow');
    const openTrigger = document.querySelector('.btn-primary');
    const closeX = document.getElementById('serviceAppCloseX');
    const cancelBtn = document.getElementById('serviceAppBtnCancel');

    if (openTrigger && serviceWindow) {
        openTrigger.addEventListener('click', () => {
            serviceWindow.style.display = 'flex';
            document.body.style.overflow = 'hidden';
        });
    }

    const closeServiceApp = () => {
        if (serviceWindow) serviceWindow.style.display = 'none';
        document.body.style.overflow = 'auto';
    };

    if (closeX) closeX.addEventListener('click', closeServiceApp);
    if (cancelBtn) cancelBtn.addEventListener('click', closeServiceApp);


    window.addEventListener('click', (e) => {
        const orderModal = document.getElementById('modalOverlay');
        if (e.target === orderModal) closeOrderModal();
        if (e.target === serviceWindow) closeServiceApp();
    });
});