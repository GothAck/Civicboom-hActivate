<%inherit file="html_base.mako"/>

<h1>FreeHoc</h1>

% if c.logged_in_user:
<p>Signed in as ${c.logged_in_user.username}</p>
% else:
<a href="${url(controller='account', action='signin')}">Signin</a>
% endif

<ul>
    <li><a href="${url(controller='item', action='view_items')}">View Items</a></li>
    <li><a href="${url(controller='item', action='new_item')}">New Item</a></li>
</ul>
