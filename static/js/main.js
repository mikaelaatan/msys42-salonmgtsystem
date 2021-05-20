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


///from the vid
// $(document).ready( function () {
//   var dataTable = $('#filtertable').DataTable({
//       "pageLength":5,
//       'aoColumnDefs':[{
//         'bSortable':false,
//         'aTargets':[nosort],
//   }],
//   columnDefs:[
//     {type:'name-char',aTargets:[5]}
//   ],
//   "aoColumns":[
//     null,
//     null,
//     null,
//     null,
//     null,
//     null,
//     null
//   ],
//   "order":false,
//   "bLengthChange":false,
//   "dom":'<"top">ct<"top"p><"clear">'
// });
// $("#filterbox").keyup(function(){
//   dataTable.search(this.value).draw();
// });
// } );

//from the site
// $(document).ready( function () {
//   $('#filtertable').DataTable();
// } );