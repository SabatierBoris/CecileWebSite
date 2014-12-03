<%inherit file="base.mak"/>
	% for content in contents:
		<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
			<% url = getContentLink(content) %>
			<a href="${url}">
				<img class="img-responsive " src="${content.thumbnail}" alt="${content.name}"/>
			</a>
		</div>
	% endfor

	<div class="col-xs-12 text-center">
		<ul class="pagination">
			% for link in pagesLink:	
				% if link[2]:
					<li class="active">
				% else:
					<li>
				% endif
					<a href="${link[1]}">${link[0]}</a>
				</li>
			% endfor
		</ul>
	</div>

<%block name="css">
	${parent.css()}
	<link rel="stylesheet" href="${request.static_url('pyramidapp:static/css/4-col-portfolio.css')}"/>
</%block>

<%def name="getContentLink(content)">
	% if content.__class__.__name__ == 'Category':
		<% return getCategoryLink(content) %>
	% endif
</%def>

<%def name="getCategoryLink(category)">
	<% return request.route_url('view_category',idCategory=category.uid,nameCategory=category.name) %>
</%def>
