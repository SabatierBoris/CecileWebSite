<!DOCTYPE html>
<html lang="${request.locale_name}">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta name="description" content="CécileM website, ${', '.join(str(t) for t in tags)}">
		<meta name="author" content="Boris SABATIER" />

		## Pinterest
		<meta name="p:domain_verify" content="2334f388ffafa5d6b80c33b4debcc886"/>

		<link rel="shortcut icon" type="image/png" href="${request.static_url('pyramidapp:static/images/favicon.png')}"/>
		<title>Cécile website</title>

		<%block name="css">
			<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Oxygen+Mono" />
			<link rel="stylesheet" type="text/css" href="${request.static_url('pyramidapp:static/css/bootstrap.css')}"/>
		</%block>

		<%block name="js">
			<script src="${request.static_url('pyramidapp:static/js/jquery-1.11.1.min.js')}"></script>
			<script src="${request.static_url('pyramidapp:static/js/bootstrap.js')}"></script>
		</%block>

		<meta name="viewport" content="width=device-width, initial-scale=1" />
	</head>
	<body>
##		<div id="wrapper">
		${next.body()}
##		</div>
		<script>
			(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
			ga('create', 'UA-74182951-1', 'auto');
			ga('send', 'pageview');
		</script>
	</body>
</html>
