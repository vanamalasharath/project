/*maps*/
$(function(){


  
  /*animate on scroll*/
  /*$('#element-to-animate').css('opacity', 0);*/
  $('#element-to-animate').css('opacity', 0);
 
  $('#element-to-animate').waypoint(function() {
      $('#element-to-animate').addClass('fadeInLeft');
  }, { offset: '50%' });
  
  
  /*function initMap() {
  // The location of Uluru
  var uluru = {lat: -25.344, lng: 131.036};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 4, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
}
*/
  /*maps*/
  
  /*new GMaps({
  div: '#map',
  lat: -12.043333,
  lng: -77.028333
});*/
  
  
});