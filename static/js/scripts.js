document.addEventListener('DOMContentLoaded', function() {
    // Function to validate login form
    function validateLoginForm() {
        const ngoId = document.getElementById('ngoId').value;
        const restaurantId = document.getElementById('restaurantId').value;
        const donorId = document.getElementById('donorId').value;
        const adminId = document.getElementById('adminId').value;

        if (!ngoId && !restaurantId && !donorId && !adminId) {
            alert('Please enter at least one ID to log in.');
            return false;
        }
        return true;
    }

    // Attach event listener to the login form
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            if (!validateLoginForm()) {
                event.preventDefault();
            }
        });
    }

    // Function to handle dropdown menu toggle
    function setupMainMenu() {
        const menuButton = document.getElementById('mainMenuButton');
        const menuDropdown = document.getElementById('mainMenuDropdown');

        if (!menuButton || !menuDropdown) {
            return;
        }

        function closeMenu() {
            menuDropdown.classList.remove('show');
            menuButton.setAttribute('aria-expanded', 'false');
            menuDropdown.setAttribute('aria-hidden', 'true');
        }

        menuButton.addEventListener('click', function(event) {
            event.stopPropagation();
            const isOpen = menuDropdown.classList.contains('show');
            if (isOpen) {
                closeMenu();
            } else {
                menuDropdown.classList.add('show');
                menuButton.setAttribute('aria-expanded', 'true');
                menuDropdown.setAttribute('aria-hidden', 'false');
            }
        });

        document.addEventListener('click', function(event) {
            if (!menuDropdown.contains(event.target) && !menuButton.contains(event.target)) {
                closeMenu();
            }
        });
    }

    // Function to handle food category display
    function displayFoodCategories() {
        const categories = document.querySelectorAll('.food-category');
        categories.forEach(category => {
            category.addEventListener('click', function() {
                const foodDetails = this.querySelector('.food-details');
                foodDetails.classList.toggle('hidden');
            });
        });
    }

    // Function to handle sidebar panel switching
    function setupPanelMenu() {
        const buttons = document.querySelectorAll('.panel-icon');
        const panels = document.querySelectorAll('.panel-card');

        if (!buttons.length || !panels.length) {
            return;
        }

        buttons.forEach(button => {
            button.addEventListener('click', function() {
                const targetId = this.getAttribute('data-panel');
                buttons.forEach(btn => btn.classList.remove('active'));
                panels.forEach(panel => panel.classList.add('hidden'));

                this.classList.add('active');
                const targetPanel = document.getElementById(targetId);
                if (targetPanel) {
                    targetPanel.classList.remove('hidden');
                }
            });
        });
    }

    // Initialize menu, panel menu, and food category display
    setupMainMenu();
    setupPanelMenu();
    displayFoodCategories();
});