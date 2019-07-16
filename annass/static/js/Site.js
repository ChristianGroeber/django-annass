$(document).ready(function() {
    $('main').css('padding-top', $('nav').height() + 'px');
    $('.navbar-toggle').click(function() {
        var panel = $('#navbar');
        panel.toggleClass('collapse');
    })
    var lastScrollTop = 0;
    var navShowing = true;
    $(document).scroll(function() {
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
    })
    var toCheck = $('.navbar-collapse');
    toCheck.toggle();
    toCheck.slideToggle();
    $('button.navbar-toggle').click(function() {
        if (toCheck.hasClass('collapse')) {
            toCheck.slideToggle();
        } else {
            toCheck.slideToggle();
        }
    })
})