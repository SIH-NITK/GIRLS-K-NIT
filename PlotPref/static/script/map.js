var map;
var marker = false;
function initMap() {
    var lat = 12.906209879341384;
    var lng = 74.82774867120163;
    var centerOfMap = new google.maps.LatLng(lat, lng);

    var options = {
      center: centerOfMap, 
      zoom: 7 
    };
    map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 9
        });
        infoWindow = new google.maps.InfoWindow;

        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };

            infoWindow.setPosition(pos);
            infoWindow.setContent('Location found.');
            infoWindow.open(map);
            map.setCenter(pos);
          }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
          });
        } else {
          handleLocationError(false, infoWindow, map.getCenter());
        }

    google.maps.event.addListener(map, 'click', function(event) {                
        var clickedLocation = event.latLng;
        if(marker === false){
            marker = new google.maps.Marker({
                position: clickedLocation,
                map: map,
                draggable: true 
            });
            google.maps.event.addListener(marker, 'dragend', function(event){
                markerLocation();
            });
        } else{
            marker.setPosition(clickedLocation);
        }
        markerLocation();
    });
}
        
function markerLocation(){
    var currentLocation = marker.getPosition();
    document.getElementById('lat').value = currentLocation.lat();
    document.getElementById('lng').value = currentLocation.lng(); 
}
        
        
google.maps.event.addDomListener(window, 'load', initMap);
