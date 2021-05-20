$.ajaxSetup({
    headers: {
        'X-CSRFToken': getCookie('csrftoken')
    }
}); 
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    console.log(cookieValue)
    return cookieValue;
}

function like(event){
    let article = event.currentTarget
    console.log(article)
    $.post({
        url: article.id,
        method: 'POST',
        success: function() {
            console.log('success')
        },
        error: function(response, status) {
            console.log(status);
        }
        });
}

function unlike(event){
    let article = event.currentTarget
    $.ajax({
        url: article.id,
        method: 'DELETE',
        success: function(data, status) {
            console.log('success')
        },
        error: function(response, status) {
            console.log(status);
        }
        });
}
