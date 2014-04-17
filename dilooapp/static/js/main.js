$(function() {
    $('#btn_sidebar').hover(function() {
        $('#sidebar-wrapper').slideDown('slow');
    });

    $('#sidebar-wrapper').mouseleave(function() {
        $('#sidebar-wrapper').slideUp('slow');
    });

    $('.container').mouseenter(function() {
        $('#sidebar-wrapper').slideUp('slow');
    });

    $('#switch').click(function(){
    	$('#feed-publico').removeClass('col-md-8 col-md-offset-1');
    	$('#feed-publico').addClass('col-md-6');
    	$('#feed-privado').show();
    	return false;
    });
});