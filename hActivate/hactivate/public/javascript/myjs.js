var map;
var markerArray = new Array();

var itemArray = new Array();
itemArray['123'] = new Array();
itemArray['123']['description'] = "This is the items description";

$(document).ready(function() {
    var latlng = new google.maps.LatLng(-30.0, 30.0);
    
    var myOpts = {
        zoom: 8,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP // optons = ROADMAP, SATELLITE, HYBRID, TERRAIN
    };
    
    var map = new google.maps.Map(document.getElementById("map_canvas"), myOpts);

    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        title: "123",
        draggable: false
    });
    
    google.maps.event.addListener(marker, 'click', function() {
        populate_item(marker.getTitle());
    });
    
    marker.setMap(map);
    
    markerArray.push(marker);
});

function populate_item(item_id) {
    var content = "<b>Item ID</b><br />" + item_id + "<br /><b>Title</b><br />Item title goes here<br /><b>Description</b><br />" + itemArray[item_id]['description'];
    var canvas = $('#item_canvas');
    canvas.html(content);
}