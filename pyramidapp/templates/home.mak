<%inherit file="base.mak"/>
	% for content in contents:
		<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
			<a href="${getContentLink(content)}">
				<img class="img-responsive " src="${content.thumbnail}" alt="${content.name}"/>
			</a>
		</div>
	% endfor

	<div class="col-lg-12 text-center">
		<ul class="pagination">
			<li>
				<a href="">&laquo;</a>
			</li>
			<li>
				<a href="">11</a>
			</li>
			<li>
				<a href="">12</a>
			</li>
			<li class="active">
				<a href="">13</a>
			</li>
			<li>
				<a href="">14</a>
			</li>
			<li>
				<a href="">15</a>
			</li>
			<li>
				<a href="">&raquo;</a>
			</li>
		</ul>
	</div>

<%block name="css">
	${parent.css()}
	<link rel="stylesheet" href="${request.static_url('pyramidapp:static/css/4-col-portfolio.css')}"/>
</%block>

<%def name="getContentLink(content)">
	% if content.__class__.__name__ == 'Category':
		${getCategoryLink(content)}
	% endif
</%def>

<%def name="getCategoryLink(category)">
	${request.route_url('view_category',idCategory=category.uid,nameCategory=category.name)}
</%def>
