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
    // Cache our vars for the fixed sidebar on scroll
    var $sidebar = $('#sidebar-nav');
    // Get & Store the original top of our #sidebar-nav so we can test against it
    var sidebarTop = $sidebar.position().top;
    // Edit the `- 10` to control when it should disappear when the footer is hit.
    var blogHeight = $('#content').outerHeight() - 10;

    // Add the function below to the scroll event
    $(window).scroll(fixSidebarOnScroll);

    // On window scroll, this fn is called (binded above)
    function fixSidebarOnScroll() {
        // Cache our scroll top position (our current scroll position)
        var windowScrollTop = $(window).scrollTop();

        // Add or remove our sticky class on these conditions
        if (windowScrollTop >= blogHeight || windowScrollTop <= sidebarTop) {
            // Remove when the scroll is greater than our #content.OuterHeight()
            // or when our sticky scroll is above the original position of the sidebar
            $sidebar.removeClass('sticky');
        }
        // Scroll is past the original position of sidebar
        else if (windowScrollTop >= sidebarTop) {
            // Otherwise add the sticky if $sidebar doesnt have it already!
            if (!$sidebar.hasClass('sticky')) {
                $sidebar.addClass('sticky');
            }
        }
    }