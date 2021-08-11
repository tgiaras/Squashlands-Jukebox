$(function() {
	$('button#play').bind('click', function() {
		$.getJSON('/PlayVLC',
			function(data) {
				//do nothing
			});
			return false;
	});
});

$(function() {
	$('button#pause').bind('click', function() {
		$.getJSON('/PauseVLC',
			function(data) {
				//do nothing
			});
			return false;
	});
});

$(function() {
	$('button#previous').bind('click', function() {
		$.getJSON('/PreviousVLC',
			function(data) {
				//do nothing
			});
			return false;
	});
});

$(function() {
	$('button#next').bind('click', function() {
		$.getJSON('/NextVLC',
			function(data) {
				//do nothing
			});
			return false;
	});
});

