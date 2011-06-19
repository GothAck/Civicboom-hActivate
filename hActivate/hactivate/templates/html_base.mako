<html>

    <head>
        <link rel="stylesheet" type="text/css" href="/style/style.css" />
        <script type="text/javascript" src="/javascript/jquery.js"></script>
        <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
        <script type="text/javascript" src="/javascript/myjs.js"></script>
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
                <p class="login">
                % if c.logged_in_user:
                Signed in as ${c.logged_in_user.username} <a href="${url(controller='account', action='signout')}">signout</a>
                % else:
                <a href="${url(controller='account', action='signin')}">Signin</a>
                % endif
                </p>
            </div>
            <div style="clear: both; padding: 1em;"></div>
            <div id="menu">
                <ul>
                    <li><a href="${url(controller='misc', action='titlepage')}">Home</a></li>
                    <li><a href="${url(controller='item', action='view_items')}">View Items</a></li>
                    % if c.logged_in_user:
                    <li><a href="${url(controller='item', action='new_item')}">New Item</a></li>
                    <li><a href="${url(controller='item', action='view_user', id=1)}">View User</a></li>
                    <li><a href="${url(controller='item', action='new_search')}">New Search</a></li>
                    % endif
                </ul>
            </div>
            ${next.body()}
            <div style="clear: both"></div>
        </div>

    </body>

</html>
