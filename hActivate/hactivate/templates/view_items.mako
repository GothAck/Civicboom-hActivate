<%inherit file="html_base.mako"/>
<% import json %>

<%def name="body()">
    <script type="text/javascript">
    var itemArray = new Array();
    var map;
    
    % for item in c.items:
        itemArray[${item.id}] = {
            id: ${item.id},
            uid:    ${item.user_id},
            status: "${item.status}",
            title:  "${item.title}",
            description:    "${item.description}",
            type:   "${item.item_type}",
            direction:  "${item.direction_type}",
            lat:    ${float(item.lat)},
            lon:    ${float(item.lon)},
        };
    % endfor    

    $(document).ready(function() {
        var latlng = new google.maps.LatLng(0.0, 0.0);
        
        var myOpts = {
            zoom: 8,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP, // optons = ROADMAP, SATELLITE, HYBRID, TERRAIN
        };
        
        map = new google.maps.Map(document.getElementById("map_canvas"), myOpts);
    
        for (var id in itemArray) {
            item = itemArray[id];
            ll = new google.maps.LatLng(item.lat, item.lon);
            marker = new google.maps.Marker({
                position: ll,
                map: map,
                title: id,
                draggable: false,
            });
            add_listener(marker);
            marker.setMap(map);
        }
        
        
    });
    
    function add_listener(marker) {
        google.maps.event.addListener(marker, 'click', function() {
            populate_item(marker.title);
        });
    }
    
    function populate_item(id) {
        item = itemArray[id];
        content = "<b>Item ID</b><br />" + item.id +
                    "<br /><b>User ID</b><br />" + item.uid +
                    "<br /><b>Status</b><br />" + item.status +
                    "<br /><b>Title</b><br />" + item.title +
                    "<br /><b>Description</b><br />" + item.description +
                    "<br /><b>Type</b><br />" + item.type +
                    "<br /><b>Direction</b><br />" + item.direction;
        canvas = $('#item_canvas');
        canvas.html(content);
    }
    </script>

    <div id="menu">
        <ul>
            <li><a href="${url(controller='misc', action='titlepage')}">Home</a></li>
            <li><a href="${url(controller='misc', action='test')}">Test</a></li>
            <li><a href="${url(controller='item', action='view_items')}">View Items</a></li>
            <li><a href="${url(controller='misc', action='test')}">Test</a></li>
        </ul>
    </div>
    <div id="map_canvas"></div>
    <div id="item_canvas"></div>
</%def>