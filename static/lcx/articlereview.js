function update_category(event, pk, user, changed, entry_id, country, old, url, title) {
    try {
        var button = $(event.currentTarget);
        var record = button.parent();
        var category_div = record.children('input[name=category_new]');
        var category_new = category_div.attr('readonly',true).val().trim();
        var category_old = old.trim();
        var changed  = parseInt(changed);
        var data_00 = {entry_id:entry_id.trim(),src_id:pk,cate_old:category_old,cate_new:category_new,changed:changed,user:user};
        var data_01 = {url:url.trim(),title:title.trim(),country:country.trim(),csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()};
        var api_url = "/nlp/review/?" + $.param(data_00);
        if( changed ) {
            if( !entry_id || !category_new || category_old==category_new ) {
                throw "Invalid new category value ";
            }
        } else {
            if( !entry_id || category_new ) {
                throw "Invalid new category value";
            }
        }
        category_div.val("");
        button.parent().children('input[type=button]').each(function(){$(this).attr('disabled',true);});
        $.post(api_url, $.extend(data_00,data_01), function(json) {
            if( json.err != 0 ) {
                alert( JSON.stringify(json, null, 2) );
            }
        }, "json").done(function() {
            ; // alert("second success");
        }).fail(function(xhr, status, error) {
            alert( "Post new category error: "+error );
        }).always(function() {
            $.getJSON(api_url, function(json) {
                if( json.id ) {
                    category_div.css('background-color','#dff0d8').val(json.cate_new);
                } else {
                    alert( JSON.stringify(json, null, 2) );
                }
            }).fail(function(xhr, status, error) {
                alert( "Get new category error: "+error );
            }).always(function() {
                button.parent().children('input[type=button]').each(function(){$(this).attr('disabled',false);});
                category_div.attr('readonly',false);
            });
        });
    } catch(e) {
        alert(e);
        button.parent().children('input[type=button]').each(function(){$(this).attr('disabled',false);});
        category_div.attr('readonly',false);
    }
}