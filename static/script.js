var app = {};

app.add_layout = function(){
	var fields = ['link', 'body'];
	add_layout = $(".add");
	$('html').on('click', function(){
		if(add_layout.is(":visible")){
			add_layout.hide();
		}
	});
	add_layout.on('click', function(event){
		event.stopPropagation();
	});
	$(".add-button, .login-button").on('click', function(event){
		event.stopPropagation();
	});
	add_layout.find('.submit').on('click', function(){
		var data = {},
			i = fields.length;
		while(i--){
			var field = fields[i],
				value = add_layout.find('.'+field).val();
			if(!value){
				add_layout.find('.'+field).addClass('error');
				return;
			}
			data[field] = value;
		}
		add_layout.find('.submit').text('Добавляю...');
		$.ajax({
		  url: "/add/",
		  type: "post",
		  dataType: "json",
		  data: data
		}).done(function(responce) { 
		  add_layout.find('.submit').text('Добавить');
		  if(responce.status === "ok"){
		  	add_layout.hide();
		  	add_layout.find('textarea, input').val('');
		  	add_layout.find('.error').removeClass('error');

		  	var new_layout = $('#main li:eq(0)').clone();
		  	new_layout.find('a').attr('href', data.link);
		  	new_layout.find('a').text(data.link);
		  	new_layout.find('div').text(data.body);
		  	new_layout.css('background', '#eee');
		  	$('#main ul').prepend(new_layout);
		  } else {
		  	if(responce.field){
		  		add_layout.find('.' + field).addClass('error');
		  	}
		  }
		});
	});
	this.add_layout = function(){
		return add_layout;
	}
	return this.add_layout();
}

app.form = (function(){
	$(function(){
		var add_layout = app.add_layout();
		$(".add-button").on("click", function(){
			add_layout.find('.tab').hide();
			add_layout.find('.add-form').show();
			$('.add').css('left', $(this).offset().left - 395);
			add_layout.toggle();
		});
	});
}());

app.login = (function(){
	$(function(){
		var add_layout = app.add_layout();
		$(".login-button").on("click", function(){
			add_layout.find('.tab').hide();
			add_layout.find('.login').show();
			$('.add').css('left', $(this).offset().left - 395);
			add_layout.toggle();
		});
	});
}());