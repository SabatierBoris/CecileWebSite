<%inherit file="../base.mak"/>
			<div class="col-md-12">
				<a class="button-with-margin btn btn-primary btn-xs" href="${request.route_url('user_list:new',new='new')}">
					<i class="fa fa-plus-square fa-fw"></i> Ajouter
				</a>
			</div>

			% if user_list:
				<form id="userList" class="col-md-12 table-responsive" role="form" method="post">
					<table class="table">
						<thead>
							<tr>
								<th>Login</th>
								<th>Password</th>
								<th>Prenom</th>
								<th>Nom</th>
								<th>E-mail</th>
								% for group in group_list:
									<th>${group.name}</th>
								% endfor
								<th></th>
							</tr>
						</thead>
						<tbody>
							% for key,user in enumerate(user_list):
								<tr>
									<td class="col-md-2">
										${forms[key].csrf_token()}
										${forms[key].login(placeholder="Login",class_="form-control")}
									</td>
									<td class="col-md-2">
										${forms[key].password(placeholder="Password",class_="form-control")}
									</td>
									<td class="col-md-2">
										${forms[key].firstname(placeholder="Prenom",class_="form-control")}
									</td>
									<td class="col-md-2">
										${forms[key].lastname(placeholder="Nom",class_="form-control")}
									</td>
									<td class="col-md-4">
										${forms[key].email(placeholder="E-mail",class_="form-control")}
									</td>
									% for group in forms[key].groups:
										<td class="col-md-1">
											${group.groupName}
											${group.access(class_="form-control")}
										</td>
									% endfor
									<td>
										% if user.uid:
											<a class="btn btn-primary" href="${request.route_url('user_delete',uid=user.uid)}">
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
