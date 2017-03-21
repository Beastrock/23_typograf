$(document).ready(function () {
  //function copies result to clipboard
  $("#js-copy-text-btn").click(function() {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($("#js-typographed-text-area").text()).select();
    document.execCommand("copy");
    $temp.remove();
  });
  //function cleans origin text area
  $("#js-clear-text-btn").click(function() {
    if ($("#js-origin-text-area").text() != "") {
      $("#js-origin-text-area").html("");
      $("#js-typographed-text-area").html("");
    };
  });
  //function sends form data on Ctrl+ENTER
  $("#js-origin-text-area").on("keydown", function(e) {
    if (e.ctrlKey && e.keyCode == 13) {
      $("#js-typography-text-btn").submit();
      return false;
    };
  });
});