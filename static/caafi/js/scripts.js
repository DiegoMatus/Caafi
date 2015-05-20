var colors = ['#1AAEDF', 'F0992A', '#D91B5B', '#F7D947', '#8DC74D', '#F0DEA4', '#F9C8A7', '#85235B'];

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

function changeColor(){
	var i = 0;
	$('.category-content').each(function(){
		$(this).css('background-color', colors[i])
		i++;
	})
}

function changeTitle(){
	if($('.title').text() === 'Categorías'){
		$('body').css('background-color', '#EEEEEE');
	}
}

function putActive(){
	$('.subcategory:first-child').addClass('active');
}

$(document).on('ready', loadData);
$(document).on('ready', changeColor);
$(document).on('ready',changeTitle );
$(document).on('ready', putActive);