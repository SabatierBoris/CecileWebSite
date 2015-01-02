<%inherit file="../base.mak"/>
			<div class="col-md-12">
				<a class="btn btn-primary btn-xs" href="${request.route_url('right_list:new',new='new')}">
					<i class="fa fa-plus-square fa-fw"></i> Ajouter
				</a>
			</div>
			% if right_list:
				<form class="col-md-4 col-sm-6" role="form" method="post">
					% for key,right in enumerate(right_list):
						<%
							css_class = ""
							if forms[key].errors:
								css_class = "has-error"
						%>
						<div class="${css_class} form-group">
							<div class="input-group">
								${forms[key].name(placeholder="Nom du droit",class_="form-control",required='required')}
								${forms[key].csrf_token()}
								% if right.uid:
									<a class="input-group-addon" href="${request.route_url('right_delete',uid=right.uid)}">
								% else:
									<a class="input-group-addon" href="${request.route_url('right_list')}">
								% endif
									<i class="fa fa-trash-o fa-fw"></i>
								</a>
							</div>
						</div>
					% endfor
					% for field,errors in forms[key].errors.items():
						% for error in errors:
							<div class="bg-danger">
								${error}
							</div>
						% endfor
					%endfor
					<button class="button-with-margin btn btn-primary btn-xs" type="submit">
						<i class="fa fa-check-square fa-fw"></i> Enregistrer
					</button>
				</form>
			% endif

<%block name="css">
	${parent.css()}
	<link rel="stylesheet" href="${request.static_url('pyramidapp:static/css/font-awesome.min.css')}"/>
</%block>
