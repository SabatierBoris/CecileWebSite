<%def name="menuCategories(list)">
	% if list:
		<ul class="nav navbar-nav">
			% for page in sorted(list):
				% if list[page].category.uid == idCategory:
					<li class="active">
				% else:
					<li>
				% endif
					<a href="${request.route_url('view_category',idItem=list[page].category.uid,nameItem=list[page].category.name)}">
						${list[page].category.name}
					</a>
					${menuCategories(list[page].sublist)}
				</li>
			% endfor
		</ul>
	% endif
</%def>
<%inherit file="layout.mak"/>
		<nav class="navbar navbar-inverse navbar-fixed-left" role="navigation">
			<header class="navbar-header">
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class="navbar-brand" href="${request.route_url('home')}">Cécile MUSSIER</a>
			</header>
			<div id="real-nav" class="collapse navbar-collapse">
				${menuCategories(categories_pages)}
				% if administration_pages:
					<ul class="nav navbar-nav top-separator">
						% for page in sorted(administration_pages):
							% if request.url==administration_pages[page].url:
								<li class="active">
							% else:
								<li>
							% endif
								<a href="${administration_pages[page].url}">
									${administration_pages[page].display}
								</a>
							</li>
						% endfor
					</ul>
				% endif
				% if request.authenticated_userid:
					<ul class="nav navbar-nav top-separator">
						<li><a href="${request.route_url('logout')}">Deconnexion</a></li>
					</ul>
				% endif
			</div>
			<footer class="collapse navbar-collapse text-right">
				Par Bobby
##				HTML5 valid
##				CSS valid
				<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a>
			</footer>
		</nav>
		<section id="page-content-wrapper">
			% if title:
				<h1 class="page-header">
					${title}
				</h1>
			% endif
			${self.body()}	
		</section>

<%block name="css">
	${parent.css()}
	<link rel="stylesheet" href="${request.static_url('pyramidapp:static/css/main.css')}"/>
</%block>
