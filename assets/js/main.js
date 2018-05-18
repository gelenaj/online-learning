$('.cards').hide().delay().fadeIn(1000);
$(function(){$('.courseDetailBox').hide();$('.showCourseDetail').click(function () {
    $(this).closest('div').find('.courseDetailBox').toggle();
});
});
function initMap() {
      var center = {lat: -5.1065854, lng: -36.3224974};
      var map = new google.maps.Map(document.getElementById('my-places'), {
        zoom: 2,
        draggable: true,
        scrollwheel: false,
        center: center
      });
      var locations = [
        ['rio', 'I moved to Brazil to use my Portugese and experience a new culture',-22.9068467, -43.172],
        ['managua', 'I worked for a year here and in Honduras supporting the work of local organizations',12.1149926, -86.2361744],
        ['kampala', 'I was very immersed here working with a local org as part of an internship',0.3475964, 32.5825197],
        ['sjm', 'I lead youth immersion organizations here and stayed a few months longer doing consulting work',18.8096268, -71.2309935],

      ];


    var infowindow = new google.maps.InfoWindow();

    var marker, i;

    for (i = 0; i < locations.length; i++) {
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i][2], locations[i][3]),
        map: map
      });

      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(locations[i][1]);
          infowindow.open(map, marker);
        }
      })(marker, i));
}


     }
