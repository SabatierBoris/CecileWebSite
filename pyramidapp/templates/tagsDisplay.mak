<%page args="item"/>

<%def name="displayTag(tag)">
	<a class="tag" href="#TODO">${tag.name}</a>
</%def>

% for tag in item.tags:
	${displayTag(tag)}
% endfor
