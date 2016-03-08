$(document).ready(function () {
    if ($('.menu-nav>ul>li').hasClass('selected')) {
        $('.selected').addClass('active');
        var currentleft = $('.selected').position().left + "px";
        var currentwidth = $('.selected').css('width');
        $('.lamp').css({"left": currentleft, "width": currentwidth});
    }
    else {
        $('.menu-nav>ul>li').first().addClass('active');
        var currentleft = $('.active').position().left + "px";
        var currentwidth = $('.active').css('width');
        $('.lamp').css({"left": currentleft, "width": currentwidth});
    }
    $('.menu-nav>ul>li').hover(function () {
        $('.menu-nav ul li').removeClass('active');
        $(this).addClass('active');
        var currentleft = $('.active').position().left + "px";
        var currentwidth = $('.active').css('width');
        $('.lamp').css({"left": currentleft, "width": currentwidth});
    }, function () {
        if ($('.menu-nav>ul>li').hasClass('selected')) {
            $('.selected').addClass('active');
            var currentleft = $('.selected').position().left + "px";
            var currentwidth = $('.selected').css('width');
            $('.lamp').css({"left": currentleft, "width": currentwidth});
        }
        else {
            $('.menu-nav>ul>li').first().addClass('active');
            var currentleft = $('.active').position().left + "px";
            var currentwidth = $('.active').css('width');
            $('.lamp').css({"left": currentleft, "width": currentwidth});
        }
    });
});