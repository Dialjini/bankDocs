function getUsers() {
    $.ajax({
        url: '/getUsers',
        type: 'GET',
        dataType: 'html',
        success: function(data) {
            let users = JSON.parse(data).reverse()
            for(let i = 0; i < users.length; i++) {
                document.getElementById("selector").append(new Option(users[i], users.length - i - 1))
            }
            document.getElementById("selector").options[0].selected = true
        }});
}

$(document).ready(function() {
    getUsers()
});