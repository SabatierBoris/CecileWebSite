<%page args="item"/>

<%def name="displayTag(tag)">
	<a class="tag" href="#TODO">${tag.name}</a>
</%def>

% if len(item.tags) > 0:
	<div class="tags">
		% if item.link:
			<a target="_blank" class="tag" href="${item.link.link}">${item.link.name}</a><br/>
		% endif
		% for tag in item.tags:
			${displayTag(tag)}
		% endfor
	</div>
% endif
