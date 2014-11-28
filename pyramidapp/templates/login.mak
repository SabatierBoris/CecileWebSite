<%inherit file="base.mak"/>
	<form class="form-horizontal col-sm-10" role="form" method="post">
		${form.csrf_token()}
		% if 'user' in form.errors:
			<div class="col-sm-offset-2 col-sm-10 bg-danger text-danger">
				${form.errors['user']}
			</div>
		% endif
		% if 'login' in form.errors:
			<div class="form-group has-error">
		% else:
			<div class="form-group">
		% endif
			<label class="col-sm-2 control-label">Login</label>
			<div class="col-sm-10">
				${form.login(placeholder="Login",autofocus=True,required=True,class_="form-control")}
			</div>
			% if 'login' in form.errors:
				% for error in form.errors['login']:
					<div class="col-sm-offset-2 col-sm-10 text-danger">
						${error}
					</div>
				% endfor
			% endif
		</div>
		% if 'password' in form.errors:
			<div class="form-group has-error">
		% else:
			<div class="form-group">
		% endif
			<label class="col-sm-2 control-label">Password</label>
			<div class="col-sm-10">
				${form.password(placeholder="Password",required=True,class_="form-control")}
			</div>
			% if 'password' in form.errors:
				% for error in form.errors['password']:
					<div class="col-sm-offset-2 col-sm-10 text-danger">
						${error}
					</div>
				% endfor
			% endif
		</div>
		<div class="form-group">
			<div class="col-sm-offset-2 col-sm-10">
				<button class="btn btn-primary" type="submit">
					<i class="fa fa-check-square fa-fw"></i> Connexion
				</button>
			</div>
		</div>
	</form>
