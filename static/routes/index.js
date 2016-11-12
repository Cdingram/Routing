// globals (should be passed)
var count = 1;
var forms = [];

function remove_element_from_array_by_id(element, list) {
    for (var i = list.length - 1; i >= 0; i--) {
        if(list[i].attr("id") == element.attr("id")) {
            var index = $.inArray(list[i], list);
            list.splice(index, 1);
        }
    };
}

function create_form() {
    var copy = $("div.container-fluid div.row .address-form.template").clone();
    copy.removeClass("template");
    copy.attr("id", count);
    
    forms.push(copy);

    // show element
    copy.show();

    // add copy to dom
    $("div.container-fluid div.row").prepend(copy);

    // add id to geocode input
    copy.find("div.geocode-container input").attr("id", "geocode-search-"+count);

    // exit button
    copy.find("div.exit").unbind("click").click(function() {
        $(this).parent().remove();
        // remove the deleted element from array
        remove_element_from_array_by_id($(this).parent(), forms);
    });

    // delay variable to call on keyup
    var delay = (function(){
      var timer = 0;
      return function(callback, ms){
        clearTimeout (timer);
        timer = setTimeout(callback, ms);
      };
    })();


    // on click show geocoding search bar
    copy.find("a#address-geocode-button")
        .unbind("click")
        .click(function() {
            // show search bar hide buttons
            copy.find("div.geocode-container").show();
            copy.find("div.button-container").hide();
            // bind keyup to geocode
            var current_count = copy.closest("div.address-form.addy").attr("id");
            copy.find("input#geocode-search-"+current_count)
                .unbind("keyup")
                .keyup(function() {
                    delay(function() {
                        geocode_keyup($("input#geocode-search-"+current_count).attr("id"));
                    }, 500);
                });
        });

    // hide geocode input
    copy.find("div.geocode-container").hide();

    // increase count now that we've used it for id's
    count += 1;
}

function show_results(searchbar, results) {
    // get actual searchbar element
    searchbar = $("input#"+searchbar);

    // for each json object add it to a datalist
    searchbar.attr("list", "results");
    searchbar.after("<div class='form-control' id='results'></div>");

    for (var i = results.length - 1; i >= 0; i--) {
        searchbar.siblings("div#results").append("<option value='" + results[i].formatted_address + "'>" + results[i].formatted_address + "</option>")
    };
}