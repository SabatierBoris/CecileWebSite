<%inherit file="../base.mak"/>
<table class="table table-stripped">
		<thead>
			<tr>
				<th>
					objet
				</th>
				<th>
					auteur
				</th>
				<th>
					commentaire
				</th>
				<th>
					actions
				</th>
			</tr>
		</thead>
		<tbody>
	% for content in contents:
		<tr>
			<td>
				<a href="${content.item.view_url(request)}">
					<img class="img-responsive img-comment" src="${request.route_url('thumbnail',idItem=content.item.uid,nameItem=content.item.name)}" alt="${content.item.name}"/>
				</a>
			</td><td>
				${content.name}	
			</td><td>
				${content.comment}	
			</td><td>
				<a href="${request.route_url('validate_comment', idComment=content.uid)}">Valider</a> /
				<a href="${request.route_url('delete_comment', idComment=content.uid)}">Supprimer</a>
			</td>
		</tr>
	% endfor
		</tbody>
	</table>
