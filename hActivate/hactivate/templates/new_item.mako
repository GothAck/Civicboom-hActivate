<%inherit file="html_base.mako"/>

<%def name="body()">
    <form action="">
        Title      <input type="text" name="title"      /><br />
        Description<input type="text" name="description"/><br />
    
        ## Javascript map selector to go here    
        
        Lon        <input id="lng" type="text" name="lon"        /><br />
        Lat        <input id="lat" type="text" name="lat"        />
        
        <input type="submit" name="submit" value="create item"/>
    </form>
    
    <div id="map_canvas"></div>
    
    <script type="text/javascript">
        $(document).ready(function() {
            // Init shit
            var latlng = new google.maps.LatLng(0.0, 0.0);
            var myOpts = {
                zoom: 8,
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