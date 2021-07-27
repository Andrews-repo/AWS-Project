$(document).ready(function() {
  $.ajax({
    type: "POST",
    data: 'json',
    contentType: 'json',
    url: 'https://api.apcloudtech.com/get',
    success: function(result) {
      console.log(result)
      $( ".fortune" ).text(result);
    },
    error: function(result) {
      console.log('error', result)
      $(".error").text(result.error)
    }
  });                              
  
  
  
  $("form").submit(function(e) {
      console.log(e)
      console.log("form serialized", $('form').serialize());
      e.preventDefault();
      $.ajax({
        type: "POST",
        data: $('form').serialize(),
        dataType: 'json',
        url: 'https://api.apcloudtech.com/',
        success: function(result) {
          console.log(result)
          $( ".added" ).text(result);
        },
        error: function(result) {
          console.log('error', result)
          $(".error").text(result.error)
        }
      });                                                                                               
    });
});

