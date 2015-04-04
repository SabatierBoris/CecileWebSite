<%inherit file="base.mak"/>
<div class="picture">
	<span class="image">
		<img class="img-responsive center-block" src="${request.route_url('original_picture',idPicture=picture.uid,namePicture=picture.name)}" alt="${picture.name}"/>
		<% prev = picture.previous %>
		% if prev:
			<div class="img-button prev">
				<a href="${prev.view_url(request)}">&#x2039;</a>
			</div>
		% endif
		<% next = picture.next %>
		% if next:
			<div class="img-button next">
				<a href="${next.view_url(request)}">&#x203a;</a>
			</div>
		% endif
	</span>
	<div class="description">
		<h1>Title</h1>
		blablzdf<br/>
		blablzdf<br/>
		blablzdf<br/>
		blablzdf<br/>
		blablzdf<br/>
		blablzdf<br/>
		blablzdf<br/>
		blablzdf<br/>

	</div>
</div>
