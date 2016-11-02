function submit_all_forms(event) {
    // call post to submit form?
    // var forms = event.data.form_list;
    // for (var i = forms.length - 1; i >= 0; i--) {
    //     forms[i].find("form").submit();
    // };
    var data = $("form#routes-form").serializeArray();
    $.post(FORM_URL, data);
}

function remove_element_from_array_by_id(element, list) {
    for (var i = list.length - 1; i >= 0; i--) {
        if(list[i].attr("id") == element.attr("id")) {
            var index = $.inArray(list[i], list);
            list.splice(index, 1);
        }
    };
}

$(document).ready(function() {
    var count = 1;
    var forms = [];
    $(".container-fluid .row .address-form.template").hide();
    // on click prepend a new template
    $(".container-fluid .row .address-form.add").unbind("click").click(function() {
        var copy = $(".container-fluid .row .address-form.template").clone();
        copy.removeClass("template");
        copy.attr("id", count);
        count += 1;
        forms.push(copy);
        $(".container-fluid form#routes-form").prepend(copy);
        copy.show();
        $(".exit").unbind("click").click(function() {
            $(this).parent().remove();
            // remove the deleted element from array
            remove_element_from_array_by_id($(this).parent(), forms);
        });
    });
    $(".create-route").unbind("click").click(submit_all_forms);
});