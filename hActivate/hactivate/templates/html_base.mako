<html>

    <head>
        <title>FreeHoc</title>
    </head>
    
    <body>
        % if c.flash:
        <p class="flash_message">${c.flash}</p>
        % endif
        ${next.body()}
    </body>

</html>
