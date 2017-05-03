$(document).ready(function(){
  $('.slideshow').slick({
	  autoplay: true,
  	  autoplaySpeed: 4000,
  	  lazyLoad: 'ondemand',
	  infinite: true
  });
});

$(document).ready(function () {
  $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
    $('.slideshow').slick('setPosition');
  });
});