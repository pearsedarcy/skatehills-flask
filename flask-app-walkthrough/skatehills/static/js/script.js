
// sidebar nav materialize
document.addEventListener('DOMContentLoaded', function () {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
});
  
// SIDENAV
$(document).ready(function(){
  $('.sidenav').sidenav();


// SWAP ICON ON CLICK
// Source: https://stackoverflow.com/a/34254979/751570
$('.dark-toggle').on('click',function(){
  if ($(this).find('i').text() == 'brightness_4'){
      $(this).find('i').text('brightness_high');
  } else {
      $(this).find('i').text('brightness_4');
  }
});


});