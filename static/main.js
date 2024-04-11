document.addEventListener('DOMContentLoaded', function () {
    const statusButtons = document.querySelectorAll('.status');
    const taskList = document.getElementById('task-list');
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchButton');

    // Function to filter tasks based on status
    function filterTasks(status) {
        const tasks = taskList.querySelectorAll('li');
        tasks.forEach(task => {
            const taskStatus = task.getAttribute('data-status');
            if (status === 'all' || taskStatus === status) {
                task.style.display = 'block';
            } else {
                task.style.display = 'none';
            }
        });
    }

    // Function to filter tasks by title
    function searchTasks(title) {
        const tasks = taskList.querySelectorAll('li');
        tasks.forEach(task => {
            const taskTitle = task.textContent.toLowerCase();
            if (taskTitle.includes(title.toLowerCase())) {
                task.style.display = 'block';
            } else {
                task.style.display = 'none';
            }
        });
    }

    // Event listener for status buttons
    statusButtons.forEach(button => {
        button.addEventListener('click', function () {
            const status = this.getAttribute('data-status');
            filterTasks(status);
        });
    });

    // Event listener for search button
    searchButton.addEventListener('click', function () {
        const searchTerm = searchInput.value.trim();
        searchTasks(searchTerm);
    });

    // Event listener for delete buttons
    taskList.addEventListener('click', function (event) {
        if (event.target.classList.contains('delete')) {
            const taskId = event.target.parentElement.getAttribute('data-id');
            const confirmed = confirm('Are you sure you want to delete this task?');
            if (confirmed) {
                // You can implement AJAX request here to delete the task from the server
                // For simplicity, just remove the task from the DOM
                event.target.parentElement.remove();
            }
        }
    });
});
