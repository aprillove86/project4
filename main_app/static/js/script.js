const dateEl = document.getElementById('id_date');
const afterEl = document.getElementById('id_start_date');
const beforeEl = document.getElementById('id_end_date');


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