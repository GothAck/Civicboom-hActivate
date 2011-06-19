<%inherit file="html_base.mako"/>

<%def name="body()">
    <div id="menu">
        <ul>
            <li><a href="${url(controller='misc', action='titlepage')}">Home</a></li>
            <li><a href="${url(controller='misc', action='test')}">Test</a></li>
            <li><a href="${url(controller='item', action='view_items')}">View Items</a></li>
            <li><a href="${url(controller='misc', action='test')}">Test</a></li>
        </ul>
    </div>
</%def>