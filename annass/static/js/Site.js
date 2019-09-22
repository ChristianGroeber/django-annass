$(document).ready(function () {
    $('main').css('padding-top', $('nav').height() + 'px');
    let toggled = false;
    $('.navbar-toggle').click(function () {
        toggled = !toggled;
        let panel = $('#navbar');
        panel.toggleClass('collapse');
    });
    let lastScrollTop = 0;
    let navShowing = true;
    $(document).scroll(function () {
        let newScrollTop = $(document).scrollTop();
        let nav = $('nav');
        if (lastScrollTop > newScrollTop && !navShowing) {
            navShowing = true;
            nav.addClass('show-nav');
            nav.removeClass('hide-nav');
            // nav.css('padding-top', $('nav').height() + 'px');
            nav.slideDown("slow");
        } else if (lastScrollTop < newScrollTop) {
            if (navShowing) {
                $('.hide-nav').css('top', newScrollTop + 'px');
            }
            navShowing = false;
            nav.removeClass('show-nav');
            nav.addClass('hide-nav');
            $('main').css('padding-top', '0');
        }
        lastScrollTop = newScrollTop;
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