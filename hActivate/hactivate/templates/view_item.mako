<%inherit file="html_base.mako"/>

View single item

with requests

% if not c.item:
  No item
% else:
  Item: ${c.item.id}
% endif
