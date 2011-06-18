<%inherit file="html_base.mako"/>

% if not c.user:
  No user
% else:
  User: ${c.user.username}
% endif
