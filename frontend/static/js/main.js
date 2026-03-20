// Глобальная переменная для хранения ID текущего заказа
let currentOrderToTakeId = null;

// 1. Единая функция открытия модального окна
function openOrderModal(order) {
    const modal = document.getElementById('modalOverlay');

    // Сохраняем ID заказа, чтобы функция takeOrder знала, что обновлять
    currentOrderToTakeId = order.id;

    // Заполняем поля данными
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

    // Показываем окно
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

// 2. Функция закрытия модального окна
function closeOrderModal() {
    const modal = document.getElementById('modalOverlay');
    if (modal) modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

// 3. Функция "Взять в работу" (Отправка на бэкенд)
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

// 4. Логика для окон и инициализация иконок
document.addEventListener('DOMContentLoaded', () => {
    // Инициализация иконок Lucide
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

    // Закрытие по клику на фон для ОБОИХ окон
    window.addEventListener('click', (e) => {
        const orderModal = document.getElementById('modalOverlay');
        if (e.target === orderModal) closeOrderModal();
        if (e.target === serviceWindow) closeServiceApp();
    });
});