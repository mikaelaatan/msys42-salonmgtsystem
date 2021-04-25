AOS.init({
 duration: 800,
 easing: 'slide',
 once: true
});

jQuery(document).ready(function($) {

 "use strict";

 var siteDatePicker = function() {

   if ( $('.datepicker').length > 0 ) {
     $('.datepicker').datepicker();
   }

 };
 siteDatePicker();

});
