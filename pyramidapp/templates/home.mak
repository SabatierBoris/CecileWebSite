<%inherit file="base.mak"/>
	% for content in contents:
		<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
			<a href="${content.view_url(request)}" class="hoverimg">
				<img class="img-responsive orignal" src="${request.route_url('thumbnail',idItem=content.uid,nameItem=content.name)}" alt="${content.name}"/>
				<img class="img-responsive hover" src="${request.route_url('thumbnail_over',idItem=content.uid,nameItem=content.name)}" alt="${content.name}"/>
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
</%block>
