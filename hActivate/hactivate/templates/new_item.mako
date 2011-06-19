<%inherit file="html_base.mako"/>

<%def name="body()">
    <div id="content">
        <form action="">
            Title      <input type="text" name="title"      /><br />
            Description<input type="text" name="description"/><br />
        
            ## Javascript map selector to go here    
            
            Lon        <input id="lng" type="text" name="lon"        /><br />
            Lat        <input id="lat" type="text" name="lat"        />
            
            <input type="submit" name="submit" value="create item"/>
        </form>
        <p>Click an area on the map to auto-complete the item location</p>
    </div>
    <div id="map_canvas" style="height: 300px; width: 300px;"></div>
    
    <script type="text/javascript">
        $(document).ready(function() {
            // Init shit
            var latlng = new google.maps.LatLng(51.5, -0.5);
            var myOpts = {
                zoom: 5,
                center: latlng,
                mapTypeId: google.maps.MapTypeId.ROADMAP, // optons = ROADMAP, SATELLITE, HYBRID, TERRAIN
            };
            var map = new google.maps.Map(document.getElementById("map_canvas"), myOpts);
            
            google.maps.event.addListener(map, 'click', function(event) {
                var lat = event.latLng.lat();
                var lng = event.latLng.lng();
                
                $("#lat").val(lat);
                $("#lng").val(lng);
                
                //alert("SOMETHING IS HAPPENING");
            });
        });
    </script>
</%def>