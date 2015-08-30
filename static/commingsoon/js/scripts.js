
jQuery(document).ready(function() {	
	
    /*
        Background slideshow
    */
	$('.top-content').backstretch([
	                     "static/commingsoon/img/backgrounds/1.jpg"
	                   , "static/commingsoon/img/backgrounds/2.jpg"
	                   , "static/commingsoon/img/backgrounds/3.jpg"
	                  ], {duration: 3000, fade: 750});
    
    $('#top-navbar-1').on('shown.bs.collapse', function(){
    	$('.top-content').backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
    	$('.top-content').backstretch("resize");
    });
    
    /*
        Wow
    */
    new WOW().init();
    
    /*
	    Countdown initializer
	*/
	var now = new Date(2016,9,11);
	var countTo = 25 * 24 * 60 * 60 * 1000 + now.valueOf();    
	$('.timer').countdown(countTo, function(event) {
		$(this).find('.days').text(event.offset.totalDays);
		$(this).find('.hours').text(event.offset.hours);
		$(this).find('.minutes').text(event.offset.minutes);
		$(this).find('.seconds').text(event.offset.seconds);
	});
    	
	/*
	    Subscription form
	*/
	//$( "#email" ).click(function() {
	//  	$('.error-message').hide();
	//	$('.success-message').hide();
	//	$('.subscribe form').hide();
	//	$('.success-message').html('Thank you for subscribe.');
	//	$('.success-message').fadeIn('fast', function(){
	//		$('.top-content').backstretch("resize");
	//	});
	//});
	//For getting CSRF token
	function getCookie(name) {
			  var cookieValue = null;
			  if (document.cookie && document.cookie != '') {
					var cookies = document.cookie.split(';');
			  for (var i = 0; i < cookies.length; i++) {
				   var cookie = jQuery.trim(cookies[i]);
			  // Does this cookie string begin with the name we want?
			  if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				  break;
				 }
			  }
		  }
	 return cookieValue;
	}

	$('.subscribe form').submit(function(e) {
		e.preventDefault();
		//Prepare csrf token
 		var csrftoken = Cookies.get('csrftoken');
		//Collect data from fields
 		var email = $('#subscribe-email').val();
	    var postdata = $('.subscribe form').serialize();
	    $.ajax({
	        type: 'POST',
	        url: window.location.href,
	        data: { csrfmiddlewaretoken : csrftoken,
				   email : email
					},
	        dataType: 'json',
	        success: function(json) {
	            if(json.valid == 0) {
	                $('.success-message').hide();
	                $('.error-message').hide();
	                $('.error-message').html(json.message);
	                $('.error-message').fadeIn('fast', function(){
	                	$('.subscribe form').addClass('animated shake').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
	            			$(this).removeClass('animated shake');
	            		});
	                });
	            }
	            else {
	                $('.error-message').hide();
	                $('.success-message').hide();
	                $('.subscribe form').hide();
	                $('.success-message').html(json.message);
	                $('.success-message').fadeIn('fast', function(){
	                	$('.top-content').backstretch("resize");
	                });
	            }
	        },
			error:  function(xhr,errmsg,err) {
					 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
					 }
	    });
	});

});


jQuery(window).load(function() {
	
	/*
		Loader
	*/
	$(".loader-img").fadeOut();
	$(".loader").delay(1000).fadeOut("slow");
	
});
