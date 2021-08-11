$(function (){
    $('tbody > tr').on('mouseenter', function (event){
        $(this).addClass('myfocus')
    })
    $('tbody > tr').on('mouseleave', function (event){
        $(this).removeClass('myfocus')
    })
})