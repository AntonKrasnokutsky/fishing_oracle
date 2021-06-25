function copyToClipboard(id_to_copy) {
    var copyText = document.getElementById(id_to_copy);
    copyText.select();
    navigator.clipboard.writeText(copyText.value);
    alert("Ссылка скопирована: " + copyText.value)
}

$(function () {
    jQuery.datetimepicker.setLocale('ru');

    jQuery('#id_date').datetimepicker({
        timepicker:false,
        format:'d.m.Y',
        mask: true,
    });

    jQuery('#id_time_start').datetimepicker({
        datepicker:false,
        format:'H:i',
        mask:true,
        step:5,
    });

    jQuery('#id_time_end').datetimepicker({
        datepicker:false,
        format:'H:i',
        mask:true,
        step:5,
    });
})

