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
				<ul class="nav navbar-nav">
					<li><a href="">Dessins</a></li>
					<li><a href="" >Architecture</a>
						<ul class="nav navbar-nav">
							<li><a href="#">L1</a></li>
							<ul class="nav navbar-nav">
								<li class="active"><a href="#">P1</a></li>
								<li><a href="#">P2</a></li>
								<li><a href="#">P3</a></li>
								<li><a href="#">P4</a></li>
							</ul>
						</ul>
					</li>
					<li><a href="">Photos</a></li>
					<li><a href="">Muss</a></li>
					<li><a href="">Texts</a></li>
					<li><a href="">Objets</a></li>
					% if request.authenticated_userid:
						<li><a href="${request.route_url('logout')}">Deconnexion</a></li>
					% endif
				</ul>
			</div>
			<footer class="collapse navbar-collapse text-center">
				Created by Bobby
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
