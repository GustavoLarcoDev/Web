// Animación suave para la navegación
document.addEventListener('DOMContentLoaded', function() {
    // Remover clase is-preload
    document.body.classList.remove('is-preload');

    // Marcar el enlace activo en la navegación
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.navbar-links a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
        }
        
        // Efecto hover
        link.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
        });
        
        link.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });

        // Animación al hacer clic
        link.addEventListener('click', function(e) {
            if (this.getAttribute('href') !== currentPage) {
                e.preventDefault();
                document.body.style.opacity = '0';
                document.body.style.transition = 'opacity 0.3s ease';
                
                setTimeout(() => {
                    window.location.href = this.getAttribute('href');
                }, 300);
            }
        });
    });

    // Animación de entrada
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.opacity = '1';
        document.body.style.transition = 'opacity 0.5s ease';
    }, 100);

    // Prevenir comportamiento por defecto en dispositivos móviles
    window.ontouchmove = function() { return false; }
    window.onorientationchange = function() { document.body.scrollTop = 0; }
});
