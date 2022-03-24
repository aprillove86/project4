const dateEl = document.getElementById('id_memo_create_date');
const afterEl = document.getElementById('id_start_date');
const beforeEl = document.getElementById('id_end_date');

// const $search = document.getElementById('search_memos');

// Side Nav

$(document).ready(function(){
    $('.sidenav').sidenav();
});

// Date Picker Animations


// document.getElementById('search_memos').reset();

// document.querySelector('button[type="reset"]').addEventListener('click', function (e) {
//     e.preventDefault();
  
//     this.parentElement.reset();
//     this.parentElement.submit();
//   })

M.Datepicker.init(dateEl, {
    format: 'yyyy-mm-dd',
    defaultDate: new Date(),
    setDefaultDate: false,
    autoClose: true
});

M.Datepicker.init(afterEl, {
    format: 'yyyy-mm-dd',
    defaultDate: new Date(),
    setDefaultDate: false,
    autoClose: true
});

M.Datepicker.init(beforeEl, {
    format: 'yyyy-mm-dd',
    defaultDate: new Date(),
    setDefaultDate: false,
    autoClose: true
});

