$(document).ready(function(){
    $('.nav-link').on('click',function() { $('.navbar-collapse').collapse('hide'); });

    $("form").submit(function(e){
        e.preventDefault();
	concept = $("#txtConcept").val();
	type = $("#radioType input:radio:checked").val();
	amount = $("#amount").val();
	account = $("#inputGroupSelect01").val()
	date = $("#dateItem").val();
	item = {
	    concept: concept,
	    type: type,
	    amount: amount,
	    account: account,
	    date: date
	};
	console.log(item);
    });
});
