
document.addEventListener('DOMContentLoaded', function() {
    // Example: Add event listener to a button inside the inline form
    document.querySelectorAll('.inline-related').forEach(function(inline) {
        var deleteButton = inline.querySelector('.delete');
        if (deleteButton) {
            deleteButton.addEventListener('click', function() {
                alert('You are about to delete a book!');
            });
        }
    });
});
