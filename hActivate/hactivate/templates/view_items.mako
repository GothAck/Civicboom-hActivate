<%inherit file="html_base.mako"/>

View Map of items

<%doc>
    Test stuff for Greg
    
<%
  import json
  
  items_array = []
  for item in c.items
    items_array.append({'title': item.title, 'descriptino': item.description})
    
  items_json = json.dumps(items_array)
  
  
  
  
%>


<script type="text/javascript">
    % for item in c.items:
       
    %endfor
</script>

</%doc>