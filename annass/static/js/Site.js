$(document).ready(function () {
    $('main').css('padding-top', $('nav').height() + 'px');
    let toggled = false;

    $('.navbar-toggle').click(function () {
        toggled = !toggled;
        let panel = $('#navbar');
        panel.toggleClass('collapse');
    });

    let toCheck = $('.navbar-collapse');
    toCheck.toggle();
    toCheck.slideToggle();
    $('button.navbar-toggle').click(function () {
        if (toCheck.hasClass('collapse')) {
            toCheck.slideToggle();
        } else {
            toCheck.slideToggle();
        }
    });

    let width = document.body.clientWidth;
    if (width <= 770) {
        let ueberMichContent = $('.ueber-mich-text');
        let ueberMichBild = $('.profile-image');
    }
});