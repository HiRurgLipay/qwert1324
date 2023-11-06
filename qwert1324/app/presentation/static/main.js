$(document).ready(function() {
    var count = 0;
    $('#add-btn').click(function() {
        count++;
        $('#form-container').append(`<input type="text" name="name${count}"><br>`);
    });
});
