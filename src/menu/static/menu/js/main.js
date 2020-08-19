
$(document).ready(function() {
    'use strict';

    //------ start menu box ------//

    // $('.menu_ti').click(function () {

    //     $('.menu_ty').slideToggle()
    // });

    // $('.menu_ty').click(function () {

    //     $('.menu_co').slideToggle()
    // });

    // $('.scroll').click(function () {
    //     $('html, body').animate({
    //         scrollTop: 50
    //     }, 300);
    // });

    // $('#menu_box').animate({
    //     scrollTop: $('#menu_box').get(0).scrollHeight
    // }, 1500);

    //------ end menu box ------//




    // navbar active link

    $('.navbar div div a').click(function() {
        $(this).addClass('active');
    });

    // menu active link

    $('.main_box .menu_title, .main_box .menu_type').click(function() {
        $(this).addClass('active')
    });


});