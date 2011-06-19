var map;

$(document).ready(function() {
    var latlng = new google.maps.LatLng(-30.0, 30.0);
    
    var myOpts = {
        zoom: 8,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP // optons = ROADMAP, SATELLITE, HYBRID, TERRAIN
    };
    
    var map = new google.maps.Map(document.getElementById("map_canvas"), myOpts);

    for (item in itemArray) {
        var marker = new google.maps.Marker({
            position: latlng,
            map: map,
            title: i["id"],
            draggable: false
        });
        
        google.maps.event.addListener(marker, 'click', function() {
            populate_item(marker.getTitle());
        });
        
        marker.setMap(map);
    }
});

function populate_item(item_id) {
    item = itemArray[item_id];
    var content = "<b>Item ID</b><br />" + item["id"] + "<br /><b>Title</b><br />" + item["title"] + "<br /><b>Description</b><br />" + item["description"];
    var canvas = $('#item_canvas');
    canvas.html(content);
}