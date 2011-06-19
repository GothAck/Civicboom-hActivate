var flash = null;

$(document).ready(function() {
   flash = $(".flash_message").hide();
   setTimeout('flash_in()', 500);
});

function flash_in() {
    $(".flash_message").fadeIn();
    setTimeout('flash_out()', 2000);
}

function flash_out() {
    $(".flash_message").fadeOut();
}