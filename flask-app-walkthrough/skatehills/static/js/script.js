
// sidebar nav materialize
document.addEventListener('DOMContentLoaded', function () {
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);
  
  let select = document.querySelectorAll('select');
  M.FormSelect.init(select);
  
  let datepicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker, 
    {
      format: 'dd/mm/yyyy',
      showClearBtn: true,
      i18n: {
        done: 'Select'
      }
    }
  );
});


// CODE PEN FROM: https://codepen.io/j_holtslander/pen/MRbpLX
// SIDENA


// SWAP ICON ON CLICK
// Source: https://stackoverflow.com/a/34254979/751570
$('.dark-toggle').on('click',function(){
  if ($(this).find('i').text() == 'brightness_4'){
      $(this).find('i').text('brightness_high');
  } else {
      $(this).find('i').text('brightness_4');
  }
});


