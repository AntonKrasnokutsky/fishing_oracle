function copyToClipboard(id_to_copy) {
    var t = document.getElementById(id_to_copy);
    navigator.clipboard.writeText(t.value);
    alert("Ссылка скопирована: " + t.value);
}

$(function () {
    jQuery.datetimepicker.setLocale('ru');

    jQuery('#id_date').datetimepicker({
        timepicker:false,
        format:'d.m.Y',
        mask: true,
    });

    jQuery('#id_published_date').datetimepicker({
        timepicker:false,
        format:'d.m.Y',
        mask: true,
    });
    
    jQuery('#id_created_date').datetimepicker({
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

