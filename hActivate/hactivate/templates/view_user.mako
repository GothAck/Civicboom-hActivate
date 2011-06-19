<%inherit file="html_base.mako"/>

<%def name="body()">
    % if not c.user:
      No user
    % else:
      ${content()}
    % endif
</%def>

<%def name="content()">
    <%
    %>
    <div id="map_canvas"></div>
    
    <div id="content">
        <b>User ID</b> ${c.user.id} <br />
        
        <b>Username</b> ${c.user.username} <br />
        
        <b>Name</b> ${c.user.name} <br />
        
        <b>Join Date</b> ${c.user.join_date} <br />
    </div>
    
    <script type="text/javascript">
        var searchArray = new Array();
        var map;
        
    
        $(document).ready(function() {
            // Init shit
            var latlng = new google.maps.LatLng(51.532255, -0.120335); //(51.5, -0.5);
            var myOpts = {
                zoom: 10,
                center: latlng,
                mapTypeId: google.maps.MapTypeId.ROADMAP, // optons = ROADMAP, SATELLITE, HYBRID, TERRAIN
            };
            map = new google.maps.Map(document.getElementById("map_canvas"), myOpts);
        
            // Create markers for items
            % for search in c.user.searchs:
                var ll = new google.maps.LatLng(${search.lat}, ${search.lon});
                var areaOpts = {
                    id: ${search.id},
                    strokeColor: "#FF0000",
                    strokeOpacity: 0.8,
                    strokeWeight: 1,
                    fillColor: "#FF0000",
                    fillOpacity: 0.25,
                    map: map,
                    center: ll,
                    radius: ${search.raduis}*1000,
                    keywords:   "Searching this area for:<br /><p>${search.keywords}</p>",
                };
                var area = new google.maps.Circle(areaOpts);
                add_listener(area);
            % endfor
        });
        
        function add_listener(area) {
            var window = new google.maps.InfoWindow();
            google.maps.event.addListener(area, 'click', function() {
                window.setPosition(area.getCenter());
                window.setContent(area.keywords);
                window.open(map);
            });
        }
    </script>
</%def>