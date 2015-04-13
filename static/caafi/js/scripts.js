function loadIcons(){
	var i = 1;
	$('.list-group-item').each(function(){
		$(this).prepend("<img src='/static/caafi/images/" +i+ ".png' width='10%' height='10%' />");
		i++;
	});
}

function loadData(){
	$('#categories').DataTable();
}

$(document).on('ready', loadIcons);
$(document).on('ready', loadData);