<%inherit file="../base.mak"/>
	<form class="form-horizontal col-md-4 col-sm-6" role="form" method="post">
		<div class="form-group">
			<label for="name" class="control-label col-sm-2">Nom</label>
			<div class="col-sm-10">
				${form.name(placeholder="Nom de la categorie",class_="form-control")}
			</div>
			${form.csrf_token()}
		</div>
		<button class="btn btn-primary btn-xs" type="submit">
			<i class="fa fa-check-square fa-fw"></i> Enregistrer
		</button>
	</form>

<%block name="css">
	${parent.css()}
	<link rel="stylesheet" href="${request.static_url('pyramidapp:static/css/font-awesome.min.css')}"/>
</%block>
