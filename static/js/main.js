// Seleccionar elementos del DOM
const sidebar = document.querySelector('.sidebar');
const toggleSidebarBtn = document.createElement('button');

// Configuración del botón de alternar la barra lateral
toggleSidebarBtn.textContent = '☰';
toggleSidebarBtn.style.position = 'fixed';
toggleSidebarBtn.style.top = '10px';
toggleSidebarBtn.style.left = '10px';
toggleSidebarBtn.style.backgroundColor = '#4CAF50';
toggleSidebarBtn.style.color = 'white';
toggleSidebarBtn.style.border = 'none';
toggleSidebarBtn.style.padding = '10px 15px';
toggleSidebarBtn.style.borderRadius = '5px';
toggleSidebarBtn.style.fontSize = '16px';
toggleSidebarBtn.style.cursor = 'pointer';
toggleSidebarBtn.style.display = 'none';

// Agregar el botón al cuerpo de la página
document.body.appendChild(toggleSidebarBtn);

// Mostrar el botón de alternar en pantallas pequeñas
function handleWindowResize() {
    if (window.innerWidth <= 768) {
        toggleSidebarBtn.style.display = 'block';
        sidebar.style.display = 'none'; // Ocultar la barra lateral por defecto
    } else {
        toggleSidebarBtn.style.display = 'none';
        sidebar.style.display = 'block'; // Mostrar la barra lateral en pantallas grandes
    }
}

// Alternar visibilidad de la barra lateral
toggleSidebarBtn.addEventListener('click', () => {
    if (sidebar.style.display === 'none' || sidebar.style.display === '') {
        sidebar.style.display = 'block';
    } else {
        sidebar.style.display = 'none';
    }
});

// Manejar eventos de redimensionamiento
window.addEventListener('resize', handleWindowResize);

// Ejecutar la función al cargar la página
handleWindowResize();

// Ejemplo de notificaciones (puedes personalizar esto)
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.textContent = message;
    notification.style.position = 'fixed';
    notification.style.bottom = '10px';
    notification.style.right = '10px';
    notification.style.padding = '10px 20px';
    notification.style.backgroundColor = type === 'success' ? '#4CAF50' : '#f44336';
    notification.style.color = 'white';
    notification.style.borderRadius = '5px';
    notification.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
    notification.style.zIndex = '1000';
    document.body.appendChild(notification);

    // Ocultar la notificación después de 3 segundos
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Ejemplo de uso de la función de notificación
document.addEventListener('DOMContentLoaded', () => {
    showNotification('¡Bienvenido al dashboard del gimnasio!', 'success');
});

// Manejo de clic para mostrar/ocultar el submenú
document.addEventListener('DOMContentLoaded', () => {
    const toggleSubmenu = document.querySelector('.toggle-submenu');
    const submenuItems = document.querySelector('.submenu-items');

    toggleSubmenu.addEventListener('click', () => {
        if (submenuItems.style.display === 'block') {
            submenuItems.style.display = 'none';
        } else {
            submenuItems.style.display = 'block';
        }
    });
});

