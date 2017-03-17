$(document).ready(function () {
  //function copies result to clipboard
  $('#copy-text-btn').click(function() {
  	var $temp = $('<input>');
  	$('body').append($temp);
  	$temp.val($('#typographed-text-area').text()).select();
  	document.execCommand('copy');
  	$temp.remove();
  });
  //function cleans origin text area
  $('#clear-text-btn').click(function() {
  	if ($('#origin-text-area').text() != '') {
  	  $('#origin-text-area').html('');
  	  $('#typographed-text-area').html('')
  	}
  });
  	$('body').on('keydown', function(e) {
  	  if (e.ctrlKey && e.keyCode == 13) {
  	    $("#typography-text-btn").click();
  	        return false;
  	    }
  	});
  });
