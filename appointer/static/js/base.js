$(function() {

var appendesc   =  ("<div class='esc-info'>PRESS ESC TO CLOSE</div>");
var appendmodal =  ("<div class='modal-overlay'></div>");

  $('button[data-modal-id]').click(function(){
    $("body").append(appendmodal);
    $("body").append(appendesc);
    $(".modal-overlay").slideDown().fadeTo(500, 0.9);
    //$(".js-modalbox").fadeIn(500);
    var modalBox = $(this).attr('data-modal-id');
    $('#'+modalBox).slideDown($(this).data());
    document.onkeydown = function(evt) {
    evt = evt || window.event;
    var isEscape = false;
    if ("key" in evt) {
        isEscape = (evt.key == "Escape" || evt.key == "Esc");
    } else {
        isEscape = (evt.keyCode == 27);
    }
    if (isEscape) {
      $(".modal, .modal-overlay, .esc-info").slideUp(function() {
        $(".modal-overlay, .esc-info").fadeTo(500, 0.1).remove();
      });
      }
    };
  });

  $(".modal-overlay, .js-modal-close").click(function() {
    $(".modal, .modal-overlay, .esc-info").slideUp(function() {
      $(".modal-overlay, .esc-info").fadeTo(500, 0.1).remove();
    });
  });
});
