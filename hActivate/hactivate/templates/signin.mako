<%inherit file="html_base.mako"/>

<%def name="body()">
    <form action="" method="POST">
    <center>
    <input id="inp" type="text" name="username"/>
    <input type="submit" name="submit" value="signin"/>
    </center>
    </form>
    
    <script type="text/javascript">
        $("#inp").focus();
    </script>
</%def>