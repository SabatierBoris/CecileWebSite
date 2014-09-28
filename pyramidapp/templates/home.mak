<%inherit file="base.mak"/>
	<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
		<img class="img-responsive " src="http://placehold.it/2970x2100/090909/777777&text=Image" alt="2970x2100/090909/777777&text=Image"/>
	</div>
	<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
		<img class="img-responsive " src="http://placehold.it/2970x2100/090909/777777&text=Image" alt="2970x2100/090909/777777&text=Image"/>
	</div>
	<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
		<img class="img-responsive " src="http://placehold.it/2970x2100/090909/777777&text=Image" alt="2970x2100/090909/777777&text=Image"/>
	</div>
	<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
		<img class="img-responsive " src="http://placehold.it/2970x2100/090909/777777&text=Image" alt="2970x2100/090909/777777&text=Image"/>
	</div>
	<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
		<img class="img-responsive " src="http://placehold.it/2970x2100/090909/777777&text=Image" alt="2970x2100/090909/777777&text=Image"/>
	</div>
	<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
		<img class="img-responsive " src="http://placehold.it/2970x2100/090909/777777&text=Image" alt="2970x2100/090909/777777&text=Image"/>
	</div>
	<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
		<img class="img-responsive " src="http://placehold.it/2970x2100/090909/777777&text=Image" alt="2970x2100/090909/777777&text=Image"/>
	</div>
	<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
		<img class="img-responsive " src="http://placehold.it/2970x2100/090909/777777&text=Image" alt="2970x2100/090909/777777&text=Image"/>
	</div>
	<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
		<img class="img-responsive " src="http://placehold.it/2970x2100/090909/777777&text=Image" alt="2970x2100/090909/777777&text=Image"/>
	</div>
	<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
		<img class="img-responsive " src="http://placehold.it/2970x2100/090909/777777&text=Image" alt="2970x2100/090909/777777&text=Image"/>
	</div>
	<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
		<img class="img-responsive " src="http://placehold.it/2970x2100/090909/777777&text=Image" alt="2970x2100/090909/777777&text=Image"/>
	</div>
	<div class="col-md-3 col-sm-4 col-xs-6 portfolio-item">
		<img class="img-responsive " src="http://placehold.it/2970x2100/090909/777777&text=Image" alt="2970x2100/090909/777777&text=Image"/>
	</div>

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

##<%def name="fooTest(param)">
##	Test : ${param.value}
##</%def>
##
##<%def name="fooSubTest(param)">
##	SubTest : ${param.value}
##</%def>
##
##<%def name="foo(param)">
##	% if hasattr(param, "new_value"):
##		${fooSubTest(param)}
##	% else:
##		${fooTest(param)}
##	% endif
##</%def>
##
##<div id="page">
##	${project}
##</div>
##
##
##% for row in plop:
##	${foo(row)}
##% endfor
