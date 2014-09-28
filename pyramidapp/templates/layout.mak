<!DOCTYPE html>
<html lang="${request.locale_name}">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta name="description" content="Cécile website">
		<meta name="author" content="Boris SABATIER" />

		<link rel="shortcut icon" href="http://placehold.it/60x60">
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
	</body>
</html>
