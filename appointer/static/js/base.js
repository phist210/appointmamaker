$(function() {
  $('#search_submit').click( function() {
    var q = $('#search').val();

    if (q) {
      $.ajax({
        type:"POST",
        url:"/?search=" + q,
        data:{
          q,
          'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType: 'html'
      });

      function searchSuccess(data, textStatus) {
        $('body').load("/?search=" + q, function() {
          $("#appointments").show();
          $("#search_cancel").show().click(function() {
            $("#appointments").hide();
            $("#search_cancel").hide();
            $('body').load("/?search= ");
          });
        });
      }

  } else {
      $("#appointments").show();
      $("#search_cancel").show().click(function() {
        $("#appointments").hide();
        $("#search_cancel").hide();
        $('body').load("/?search= ");
      });
    }
  });
});


$(function() {
  $("#new").click(function() {
    $(".buttons").hide();
    $(".other_buttons").show();
    $("#cancel").click(function () {
      $(".buttons").show();
      $(".other_buttons").hide();
    });
  });
});


$( document ).ajaxStart( function() {
  $( '#spinner' ).show();
}).ajaxStop( function() {
  $( '#spinner' ).hide();
});
