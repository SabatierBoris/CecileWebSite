<%inherit file="../base.mak"/>
	<form class="form-horizontal col-md-4 col-sm-6" role="form" method="post" accept-charset="utf-8" enctype="multipart/form-data">
		<%
			css_class = ""
			if form.errors.get('name'):
				css_class = "has-error"
		%>
		<div class="${css_class} form-group">
			${form.name.label(class_="control-label col-sm-4")}
			<div class="col-sm-8">
				${form.name(placeholder="Nom de l'image",class_="form-control")}
			</div>
			${form.csrf_token()}
		</div>
		% if form.errors.get('name'):
				% for error in form.errors['name']:
					<div class="bg-danger col-md-offset-4 col-sm-8">
						${error}
					</div>
				% endfor
		% endif
		<%
			css_class = ""
			if form.errors.get('image'):
				css_class = "has-error"
		%>
		<div class="${css_class} form-group">
			${form.image.label(class_="control-label col-sm-4")}
			<div class="col-sm-8">
				<div class="input-group">
					<span class="input-group-btn">
						<span class="btn btn-primary btn-file">
							Parcourir &hellip;
							${form.image()}
						</span>
					</span>
					<input type="text" class="form-control" readonly/>
				</div>
			</div>
		</div>
		% if form.errors.get('image'):
				% for error in form.errors['image']:
					<div class="bg-danger col-md-offset-4 col-sm-8">
						${error}
					</div>
				% endfor
		% endif
		<button class="btn btn-primary btn-xs" type="submit">
			<i class="fa fa-check-square fa-fw"></i> Enregistrer
		</button>
	</form>

<%block name="css">
	${parent.css()}
	<link rel="stylesheet" href="${request.static_url('pyramidapp:static/css/font-awesome.min.css')}"/>
</%block>
<%block name="js">
	${parent.js()}
	<script src="${request.static_url('pyramidapp:static/js/browse.js')}"></script>
</%block>
