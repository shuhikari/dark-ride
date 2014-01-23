$(document).ready(function(){
	$('#id_category').chosen({
		no_results_text: "Sem resultados para",
	    placeholder_text_single: "Selecione uma opção",
	    placeholder_text_multiple: "Selecione as opções",
	    width: '350px',
	    search_contains: true,	    
	}).change(function(){
		$('#id_category').trigger("chosen:updated");
	});	
	$('#id_category').trigger("chosen:updated");
	$('.field-suggestion').on('click', 'a', function(){
		var key = $(this).data('key');
		$('#id_category').find('option[value="' + key + '"]').attr('selected', true);
		$('#id_category').trigger("chosen:updated");
	});	
});