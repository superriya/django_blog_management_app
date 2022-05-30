// console.log("hiiii");
// $( "#replytitle" ).click(function(e) {
//     e.preventDefault();
//     $( "#comment-form-block" ).slideToggle( "slow", function() {
//         // Animation complete.
//     });
// });

$(document).ready(function() {
    $('#replytitle').click(function() {
      $('.comment-form-block').slideToggle("slow");
      // Alternative animation for example
      // slideToggle("fast");
    });
});