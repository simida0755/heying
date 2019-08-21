(function () {
    url = window.location.pathname
    if (url == '/'){
        $('#index').addClass('linking')
    }
    if (url== '/coming_soon'){
        $('#gifts').addClass('linking')
    }
    if (url == '/my/matches'){
        $('#matches').addClass('linking')
    }
    if (url == '/my/group'){
        $('#group').addClass('linking')
    }
})()