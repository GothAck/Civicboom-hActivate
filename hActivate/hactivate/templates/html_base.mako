<html>

    <head>
        <link rel="stylesheet" type="text/css" href="/style/style.css" />
        <script type="text/javascript" src="/javascript/jquery.js"></script>
        <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
        <title>FreeHoc</title>
    </head>
    
    <body>

        <div class="header">
            % if c.flash:
            <p class="flash_message">${c.flash}</p>
            % endif
            % if c.logged_in_user:
            <p>Signed in as ${c.logged_in_user.username}</p>
            % else:
            <a href="${url(controller='account', action='signin')}">Signin</a>
            % endif
        </div>

        <div id="wrapper">
            <div id="title_bar">
                <img class="logo" src="/logo.png" />
            </div>
            <div style="clear: both;"></div>
            ${next.body()}
        </div>

    </body>

</html>
