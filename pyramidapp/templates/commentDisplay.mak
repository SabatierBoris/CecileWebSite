<%page args="item"/>

<%def name="displayComment(comment)">
	<div class="comment">
		<header>
			${comment.created_on.strftime("Le %d/%m/%Y à %H:%M:%S")} par ${comment.name} 
		</header>
		${comment.comment}
		% for child in comment.children:
			${displayComment(child)}
		% endfor
	</div>
</%def>

% if item.comments.filter_by(valid=True).count():
	<h1>Commentaires (${item.comments.filter_by(valid=True).count()})</h1>
	% for comment in item.comments.filter_by(valid=True).filter_by(parent=None):
		${displayComment(comment)}
	% endfor
% else:
	<h1>Aucun commentaire</h1>
% endif

<form class="col-lg-5 col-md-6 col-sm-9" role="form" method="post">
	<%
		css_class = ""
		if form.errors.get('name'):
			css_class = "has-error"
	%>
	<div class="${css_class} form-group">
		${form.name.label(class_="control-label col-sm-5")}
		<div class="col-sm-7">
			${form.name(placeholder="Pseudo",class_="form-control")}
		</div>
		${form.csrf_token()}
	</div>

	<div class="${css_class} form-group">
		${form.comment.label(class_="control-label col-sm-5")}
		<div class="col-sm-7">
			${form.comment(placeholder="Commentaire",class_="form-control")}
		</div>
	</div>

	<button class="button-with-margin btn btn-primary btn-xs" type="submit">
		<i class="fa fa-check-square fa-fw"></i> Commenter
	</button>
</form>
