$(document).ready(function () {
    $('main').css('padding-top', $('nav').height() + 'px');
    let toggled = false;
    $('.navbar-toggle').click(function () {
        toggled = !toggled;
        console.log(toggled);
        let panel = $('#navbar');
        panel.toggleClass('collapse');
        /*if (!toggled) {
            $('nav').css('box-shadow', '0px 8px 5px 0px rgba(0, 0, 0, 0.3)');
        } else {
            $('nav').css('box-shadow', '0 0 0 0 rgba(0,0,0,0)');
        }*/
    });
    var lastScrollTop = 0;
    var navShowing = true;
    $(document).scroll(function () {
        var newScrollTop = $(document).scrollTop();
        console.log(newScrollTop);
        if (lastScrollTop > newScrollTop && !navShowing) {
            navShowing = true;
            $('nav').addClass('show-nav');
            $('nav').removeClass('hide-nav');
            $('main').css('padding-top', $('nav').height() + 'px');
            $('nav').slideDown("slow");
        } else if (lastScrollTop < newScrollTop) {
            if (navShowing) {
                $('.hide-nav').css('top', newScrollTop + 'px');
            }
            navShowing = false;
            $('nav').removeClass('show-nav');
            $('nav').addClass('hide-nav');
            $('main').css('padding-top', '0');
        }
        lastScrollTop = newScrollTop;
    });
    var toCheck = $('.navbar-collapse');
    toCheck.toggle();
    toCheck.slideToggle();
    $('button.navbar-toggle').click(function () {
        if (toCheck.hasClass('collapse')) {
            toCheck.slideToggle();
        } else {
            toCheck.slideToggle();
        }
    })
});