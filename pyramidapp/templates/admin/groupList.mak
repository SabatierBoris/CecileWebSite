<%inherit file="../base.mak"/>
			<div class="col-md-12">
				<a class="btn btn-primary btn-xs" href="${request.route_url('group_list:new',new='new')}">
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
								<tr>
									% if 'name' in forms[key].errors:
										<td class="has-error col-md-3">
									% else:
										<td class="col-md-3">
									% endif
										${forms[key].csrf_token()}
										${forms[key].name(placeholder="Nom du droit",class_="form-control",required="required")}
										% if 'name' in forms[key].errors:
											<div class="bg-danger">
												% for error in forms[key].errors['name']:
													${error}
												% endfor
											</div>
										% endif
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
