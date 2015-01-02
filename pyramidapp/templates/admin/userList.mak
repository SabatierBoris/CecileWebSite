<%inherit file="../base.mak"/>
			<div class="col-md-12">
				<a class="btn btn-primary btn-xs" href="${request.route_url('user_list:new',new='new')}">
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
									% if 'login' in forms[key].errors:
										<td class="has-error col-md-2">
									% else:
										<td class="col-md-2">
									% endif
										${forms[key].csrf_token()}
										${forms[key].login(placeholder="Login",class_="form-control")}
										% if 'login' in forms[key].errors:
											<div class="bg-danger">
												% for error in forms[key].errors['login']:
													${error}
												% endfor
											</div>
										% endif
									</td>
									% if 'password' in forms[key].errors:
										<td class="has-error col-md-2">
									% else:
										<td class="col-md-2">
									% endif
										${forms[key].password(placeholder="Password",class_="form-control")}
										% if 'password' in forms[key].errors:
											<div class="bg-danger">
												% for error in forms[key].errors['password']:
													${error}
												% endfor
											</div>
										% endif
									</td>
									% if 'firstname' in forms[key].errors:
										<td class="has-error col-md-2">
									% else:
										<td class="col-md-2">
									% endif
										${forms[key].firstname(placeholder="Prenom",class_="form-control")}
										% if 'firstname' in forms[key].errors:
											<div class="bg-danger">
												% for error in forms[key].errors['firstname']:
													${error}
												% endfor
											</div>
										% endif
									</td>
									% if 'lastname' in forms[key].errors:
										<td class="has-error col-md-2">
									% else:
										<td class="col-md-2">
									% endif
										${forms[key].lastname(placeholder="Nom",class_="form-control")}
										% if 'lastname' in forms[key].errors:
											<div class="bg-danger">
												% for error in forms[key].errors['lastname']:
													${error}
												% endfor
											</div>
										% endif
									</td>
									% if 'email' in forms[key].errors:
										<td class="has-error col-md-'">
									% else:
										<td class="col-md-4">
									% endif
										${forms[key].email(placeholder="E-mail",class_="form-control")}
										% if 'email' in forms[key].errors:
											<div class="bg-danger">
												% for error in forms[key].errors['email']:
													${error}
												% endfor
											</div>
										% endif
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
											<a class="btn btn-primary" href="${request.route_url('user_list')}">
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
