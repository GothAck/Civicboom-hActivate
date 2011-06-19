<html>

    <head>
        <link rel="stylesheet" type="text/css" href="/style/style.css" />
        <script type="text/javascript" src="/javascript/jquery.js"></script>
        <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
        <title>FreeHoc</title>
    </head>
    
    <body>

        <div class="header">
            
        </div>

        <div id="wrapper">
            <div id="title_bar">
                <a href="${url(controller='misc', action='titlepage')}"><img class="logo" src="/logo.png" /></a>
                % if c.flash:
                <p class="flash_message">${c.flash}</p>
                % endif
                % if c.logged_in_user:
                <p>Signed in as ${c.logged_in_user.username} <a href="${url(controller='account', action='signout')}">signout</a></p>
                % else:
                <p><a href="${url(controller='account', action='signin')}">Signin</a></p>
                % endif
            </div>
            <div style="clear: both;"></div>
            <div id="menu">
                <ul>
                    <li><a href="${url(controller='misc', action='titlepage')}">Home</a></li>
                    <li><a href="${url(controller='item', action='view_items')}">View Items</a></li>
                    % if c.logged_in_user:
                    <li><a href="${url(controller='item', action='new_item')}">New Item</a></li>
                    <li><a href="${url(controller='item', action='new_search')}">New Search</a></li>
                    % endif
                </ul>
            </div>
            ${next.body()}
        </div>

    </body>

</html>
