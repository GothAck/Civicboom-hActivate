<%inherit file="html_base.mako"/>

<%def name="body()">
    <div id="content">
        <form action="">
            Keywords<input type="text" name="keywords" /> (comma separated) <br/>
            Radius<input type="text" name="radius" />(in kilometers) <br/>
            Lon        <input id="lng" type="text" name="lon"        /><br />
            Lat        <input id="lat" type="text" name="lat"        />
            
            <input type="submit" name="submit" value="submit"/>
        </form>
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