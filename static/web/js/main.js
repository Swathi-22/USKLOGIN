// alert('123')
$(document).ready(function() {
    
    var $submit = $("#submit_prog").hide(),
        $cbs = $('input[name="prog"]').click(function() {
            $submit.toggle( $cbs.is(":checked") );
        });

});



// =================== new_service
$(document).ready(function() {

    // required elements
    var imgPopup = $('.img-popup');
    var imgCont  = $('.container__img-holder');
    var popupImage = $('.img-popup img');
    var closeBtn = $('.close-btn');
  
    // handle events
    imgCont.on('click', function() {
      var img_src = $(this).children('img').attr('src');
      imgPopup.children('img').attr('src', img_src);
      imgPopup.addClass('opened');
    });
  
    $(imgPopup, closeBtn).on('click', function() {
      imgPopup.removeClass('opened');
      imgPopup.children('img').attr('src', '');
    });
  
    popupImage.on('click', function(e) {
      e.stopPropagation();
    });
    
  });





// ======================sidebar
    

      $(document).ready(function(){
        $("#demo").addClass('main-panel-marg')
      })
      $( "#test" ).click(function() {
        $("#demo").toggleClass('main-panel-marg')
        $("#demo2").addClass('content-div')
    
    });
 


// ============== Support request form

$(document).on('submit','form.ajax', function(e) {
  e.preventDefault();
  var $this = $(this);
  var data = new FormData(this);
  var action_url = $this.attr('action');
  var reset = $this.hasClass('reset');
  var reload = $this.hasClass('reload');
  var redirect = $this.hasClass('redirect');
  var redirect_url = $this.attr('data-redirect');

  $.ajax({
      url: action_url,
      type: 'POST',
      data: data,
      cache: false,
      contentType: false,
      processData: false,
      dataType: "json",

      success: function(data) {

          var status = data.status;
          var title = data.title;
          var message = data.message;
          var pk = data.pk;

          if (status == "true") {
              if (title) {
                  title = title;
              } else {
                  title = "Success";
              }

              Swal.fire({
                  title: title,
                  html: message,
                  icon: 'success',
              }).then(function() {
                  if (redirect) {
                      window.location.href = redirect_url;
                  }
                  if (reload) {
                      window.location.reload();
                  }
                  if (reset) {
                      window.location.reset();
                  }
              });

          } else {
              if (title) {
                  title = title;
              } else {
                  title = "An Error Occurred";
              }
              Swal.fire({
                  title: title,
                  html: message,
                  icon: "error"
              });

          }
      },
      error: function(data) {
          var title = "An error occurred";
          var message = "something went wrong";
          Swal.fire({
              title: title,
              html: message,
              icon: "error"
          });
      }
  });
}); 


    

  
    