<%inherit file="../base.mak"/>
			<div class="col-md-12">
				<a class="button-with-margin btn btn-primary btn-xs" href="${request.route_url('group_list:new',new='new')}">
					<i class="fa fa-plus-square fa-fw"></i> Ajouter
				</a>
			</div>
			% if group_list:
				<form id="groupList" class="col-md-12 table-responsive" role="form" method="post">
					<table class="table">
						<thead>
							<tr>
								<th></th>
								% for right in right_list:
									<th>${right.name}</th>
								% endfor
								<th></th>
							</tr>
						</thead>
						<tbody>
							% for key,group in enumerate(group_list):
						##		<%
						##			css_class = ["form_group","form_inline"]
						##		%>
						##		% for field_errors in forms[key].errors.items():
						##			% for error in errors:
						##				<%
						##					css_class.append("has-error")
						##				%>
						##				<div class="bg-danger">
						##					${error}
						##				</div>
						##			% endfor
						##		% endfor
								<tr>
									<td class="col-md-3">
										${forms[key].csrf_token()}
										${forms[key].name(placeholder="Nom du droit",class_="form-control")}
									</td>
									% for right in forms[key].rights:
										<td class="col-md-1">
											${right.rightName}
											${right.access(class_="form-control")}
										</td>
									% endfor
									<td>
										% if group.uid:
											<a class="btn btn-primary" href="${request.route_url('group_delete',uid=group.uid)}">
										% else:
											<a class="btn btn-primary" href="${request.route_url('group_list')}">
										% endif
											<i class="fa fa-trash-o fa-fw"></i>
										</a>
									</td>
								</tr>
							% endfor
						</tbody>
					</table>
					<button class="btn btn-primary btn-xs" type="submit">
						<i class="fa fa-check-square fa-fw"></i> Enregistrer
					</button>
				</form>
			% endif

<%block name="css">
	${parent.css()}
	<link rel="stylesheet" href="${request.static_url('pyramidapp:static/css/font-awesome.min.css')}"/>
</%block>

