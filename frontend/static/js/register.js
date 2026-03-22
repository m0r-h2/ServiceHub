document.addEventListener('DOMContentLoaded', () => {
    const registrationForm = document.querySelector('.form-container');

    if (registrationForm) {
        registrationForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const formData = new FormData(e.target);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch('/api/v1/companies/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                if (response.ok) {
                    const result = await response.json();


                    if (result.access_token) {
                        localStorage.setItem('access_token', result.access_token);
                    }

                    alert('Регистрация успешна!');

                    window.location.href = '/company_profile';
                } else {
                    const error = await response.json();
                    alert('Ошибка: ' + (error.detail || 'Не удалось создать аккаунт'));
                }
            } catch (err) {
                console.error('Ошибка сети:', err);
                alert('Проблема с соединением. Попробуйте позже.');
            }
        });
    }
});