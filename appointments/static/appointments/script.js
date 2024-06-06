// appointments/static/js/script.js

// Ensure the DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', (event) => {
    console.log('JavaScript is working!');

    // Add event listeners to all elements with the class 'btn-primary'
    document.querySelectorAll('.btn-primary').forEach(button => {
        button.addEventListener('click', () => {
            alert('Appointment button clicked!');
        });
    });

    // Example of adding more interactivity
    document.querySelectorAll('.list-group-item').forEach(item => {
        item.addEventListener('mouseover', () => {
            item.style.backgroundColor = '#f0f0f0';
        });
        item.addEventListener('mouseout', () => {
            item.style.backgroundColor = '';
        });
    });
});