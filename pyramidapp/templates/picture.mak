<%inherit file="base.mak"/>
<div class="picture">
	<span class="image">
		<img class="img-responsive center-block" src="${request.route_url('original_picture',idItem=item.uid,nameItem=item.name)}" alt="${item.name}"/>
		<% prev = item.previous %>
		% if prev:
			<div class="img-button prev">
				<a href="${prev.view_url(request)}">&#x2039;</a>
			</div>
		% endif
		<% next = item.next %>
		% if next:
			<div class="img-button next">
				<a href="${next.view_url(request)}">&#x203a;</a>
			</div>
		% endif
	</span>
	<div class="description">
		<%include file="tagsDisplay.mak" args="item=item"/>
		<%include file="commentDisplay.mak" args="item=item"/>
	</div>
</div>

<%block name="css">
	${parent.css()}
	<link rel="stylesheet" href="${request.static_url('pyramidapp:static/css/font-awesome.min.css')}"/>
</%block>
