

$(document).on('confirmation', '.remodal', function () {
    var mid = $('#mid').text()
    window.location.href='/group/movie/' + mid
});