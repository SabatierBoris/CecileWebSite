<%inherit file="../base.mak"/>
	% for page in pages:
		<div class="col-md-12 col-xs-12">
			<a class="button-with-margin btn btn-primary btn-xs col-md-1 col-xs-6" href="${request.route_url(pages[page])}">
				${page}
			</a>
		</div>
	% endfor

<%block name="css">
	${parent.css()}
	<link rel="stylesheet" href="${request.static_url('pyramidapp:static/css/font-awesome.min.css')}"/>
</%block>

