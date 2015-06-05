var colors = ['#1AAEDF', 'F0992A', '#D91B5B', '#F7D947', '#8DC74D', '#F0DEA4', '#F9C8A7', '#85235B'];

function main(){

	/*var i = 1;
	$('.list-group-item').each(function(){
		$(this).prepend("<img src='/static/caafi/images/" +i+ ".png' width='10%' height='10%' />");
		i++;
	});*/

	$('#categories').DataTable();

	var i = 0;
	$('.category-content').each(function(){
		$(this).css('background-color', colors[i])
		i++;
	});

	if($('.title').text() === 'Categorías'){
		$('body').css('background-color', '#EEEEEE');
	}

	$('.subcategory:first-child').addClass('active');

	$('#categories tbody tr').on('click', function(){
		$('#btn-reported').removeClass('btn-custom');
		$(this).css('background', '#AAAAAA');
		$(this).attr('id', 'row-selected');
		alert($(this).attr('id'));
	});

	/*$('body').not('#categories tbody tr').on('click', function(){
		$('#btn-reported').addClass('btn-custom');
	})*/

function reportedUrl(){
	$('#reported_url').on('submit', function(e){
		e.preventDefault();
		$ajax({
			url : 'url/add',
			method : 'POST',
			success : function(data){
				console.log(data);
			},
			error : function(){
				console.log(data);
			}
		});
	});
}
}

$(document).on('ready', main);

