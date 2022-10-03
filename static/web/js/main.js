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
 



    

  
    