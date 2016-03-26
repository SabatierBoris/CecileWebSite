<%inherit file="../base.mak"/>
	<form class="form-horizontal col-md-4 col-sm-6" role="form" method="post" accept-charset="utf-8">
		<%
			css_class = ""
			if form.errors.get('name'):
				css_class = "has-error"
		%>
		<div class="${css_class} form-group">
			${form.name.label(class_="control-label col-sm-4")}
			<div class="col-sm-8">
				${form.name(placeholder="Nom du lien",class_="form-control")}
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
			if form.errors.get('link'):
				css_class = "has-error"
		%>
		<div class="${css_class} form-group">
			${form.link.label(class_="control-label col-sm-4")}
			<div class="col-sm-8">
				${form.link(placeholder="URL du lien",class_="form-control")}
			</div>
		</div>
		% if form.errors.get('link'):
				% for error in form.errors['link']:
					<div class="bg-danger col-md-offset-4 col-sm-8">
						${error}
					</div>
				% endfor
		% endif

		<button class="btn btn-primary btn-xs" type="submit">
			<i class="fa fa-check-square fa-fw"></i> Enregistrer
		</button>
		% if item.link:
			<br/>
			<a class="btn btn-primary btn-xs" href="${request.route_url('delete_link', idLink=item.link.uid)}">
				<i class="fa fa-trash-o fa-fw"></i> Supprimer
			</a>
		% endif 
	</form>
