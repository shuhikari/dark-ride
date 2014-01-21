django.jQuery(document).ready(function () {
	$ = django.jQuery;    
	$('.field-suggestion').on('click', 'a', function(){
		var key = $(this).data('key')
		$('#id_category').find('option[value="' + key + '"]').attr('selected', true);
	});

});