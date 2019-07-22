$(function() {
    lcxLoadUploadLibrary();
    if ( window.location.pathname.search(/\/admin\/news_\w{1,8}\/pushrule\//g) >= 0 ) {
        $('.submit-row button[name=_addanother]').hide();
        $('.submit-row button[name=_continue]').hide();
        $('.submit-row button[name=_save]').text('Send').bind("click", function(event) {
            var button = $(event.currentTarget);
            var fullwidth = ["，", "‘", "’", "“", "”"];
            var push_title = $("input[name='push_title']").val() || "";
            var entry_title = $("input[name='title']").val() || "";
            var lcx_area = $('#id_lcx_area').val() || "";
            if ( intersect(push_title.split(''),fullwidth).length>0 || intersect(entry_title.split(''),fullwidth).length>0 ) {
                alert("Full width punctuation characters not allowed in news title !");
                return false;
            }
            if ( lcx_area && window.location.pathname=='/admin/news_af/pushrule/add/' && lcx_area.split(',').filter(function(x) { return ["gh","ke","ng","tz","za"].indexOf(x) < 0 }).length>0 ) {
                alert("Multiple country only allowed: gh,ke,ng,tz,za");
                return false;
            }
            if ( $('#id_flags_6').is(':checked') && !push_title ) { // Alert needs Picture Push
                alert("Please Fill PushTitle OR Uncheck Alert Option");
                return false;
            }
            //document.forms["pushrule_form"].submit();
        });
        //$("input[name='city']").css('background-color','#fbeed5');
        $(window).load(function() {
            $('#id_push_entire').triggerHandler('change');
            if ( window.location.pathname.search(/\/admin\/news_af\/pushrule\//g) >= 0 ) {
                $(".inner-right-column").css("position", "static");
            } else {
                document.getElementById("fieldsetcollapser0").click();
            }
            var rulenodeset = document.querySelector("#pushrulenode_set-group");
            if( false && rulenodeset ) {
                rulenodeset.parentNode.insertBefore(rulenodeset, rulenodeset.parentNode.firstElementChild);
                document.getElementById("id_pushrulenode_set-0-entry_id").focus();
            }
        });
        if ( window.location.pathname.search(/\/admin\/news_\w{1,8}\/pushrule\/\d+\//g) >= 0 ) {
            var param = lcxGetQueryDict();
            $(".delete").html('<a class="inline-deletelink" href="javascript:alert(\'Can not delete news-list item already pushed.\\nYou can delete this rule instead.\')">Remove</a>');
        }
        if ( window.location.pathname=='/admin/news_af/pushrule/add/' || window.location.pathname=='/admin/news_zz/pushrule/add/' ) {
            setTimeout(function() {
                if ( $('#user-tools strong').text().trim()!='lcx' ) return;
                $('.submit-row button[name=_save]').parent().append('<input id="id_lcx_area" maxlength="30" name="lcx_area" placeholder="comma split country" style="width:130px;" type="text">');
            }, 1000);
            $('#pushrulenode_set-group').on('DOMSubtreeModified', function() {
                var lcx_area = $('#id_lcx_area');
                if ( $('#pushrulenode_set-1').size() ) {
                    if(lcx_area.val()) lcx_area.val('');
                    lcxSetVisible(lcx_area, false);
                } else {
                    lcxSetVisible(lcx_area, true);
                }
            });
        }
    }
    $('#pushrulenode_set-group h2').text('AddPushNews：');
    //$("#id_push_icon").css({"width":"calc(80%-88px)" ,"margin-right":"10px"})
    return; // cancel after 20170315 meeting
    $("#id_push_type").bind("change", function() {
        var push_type = $("#id_push_type").val();
        if ( push_type == "immediately" ) {
            $("#id_push_time_0").next().children()[0].click();
            $("#id_push_time_1").next().children()[0].click();
        } else {
            $("#id_push_time_0").val("");
            $("#id_push_time_1").val("");
        }
    });
});
function url_domain(data) { // https://stackoverflow.com/questions/8498592/extract-hostname-name-from-string
  var a = document.createElement('a');
  a.href = data;
  if ( !data.includes(a.hostname) ) return '';
  return a.hostname.replace(new RegExp("^www."), '');
}
function intersect(a, b) { // https://stackoverflow.com/questions/16227197/compute-intersection-of-two-arrays-in-javascript
    var t;
    if (b.length > a.length) t = b, b = a, a = t; // indexOf to loop over shorter
    return a.filter(function (e) {
        return b.indexOf(e) > -1;
    });
}
function get_icon_url_from_json(json, noicon) {
    if ( json.no_of_pictures > 0 && (json.id || json.news_id) ) {
        var icon_url_suffix = '/';
        var suffix = '?width=78&height=78';
        if ( 'thumbnail' in json && json.thumbnail.image_server && json.thumbnail.id ) {
            return 'http://img.transcoder.opera.com/assets/v2'+icon_url_suffix+fix_news_id(json.thumbnail.id)+suffix;
        } else if ( json.imageserver ) {
            return 'http://img.transcoder.opera.com/assets/v2'+icon_url_suffix+fix_news_id(json.id ? json.id : json.news_id)+suffix;
        } else {
            return 'http://img.transcoder.opera.com/assets/v2'+icon_url_suffix+fix_news_id(json.id ? json.id : json.news_id)+suffix;
        }
    } else {
        return noicon ? noicon : '';
    }
}
function get_icon_url_from_json_v1(json, noicon) {
    if ( json.no_of_pictures > 0 ) {
        var icon_url_suffix = '/crop/xl/c/';
        if ( json.thumbnail.image_server && json.thumbnail.id ) {
            return json.thumbnail.image_server                +icon_url_suffix+fix_news_id(json.thumbnail.id);
        } else if ( json.imageserver ) {
            return json.imageserver                           +icon_url_suffix+fix_news_id(json.id);
        } else {
            return 'http://img.transcoder.opera.com/assets/v1'+icon_url_suffix+fix_news_id(json.id);
        }
    } else {
        return noicon ? noicon : '';
    }
}
function set_push_icon(img, transcoder, pk, ps) {
    var delay = ( ps - 1 - pk % ps ) * 500;
    img.style.height = '70px';
//  $(".field-_x_image img").each(function(i, item) {
//      item.style.height = '70px';
//  });
    setTimeout(function() {
        if ( window.image_loaded == undefined )
            window.image_loaded = new Array();
        if ( transcoder in window.image_loaded )
            return;
        var loading = img.src;
        var img404  = '/static/lcx/404.png';
        var imgerr  = 'data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==';
        $.getJSON(transcoder, function(json) {
            var icon_url = get_icon_url_from_json(json, img404);
            $(img).on('load', function(event) {
                if ( img.src.split('lcx')[1] == img404.split('lcx')[1] ) {
                    img.style.height = '0px';
                    return;
                }
                $("._x_image-column span").text("News_Image");
            }).on('error', function(event) {
                img.src = imgerr;
            });
            img.src = icon_url;
        }).error(function() {
            img.src = '/static/admin/img/icon_error.gif';
        });
        window.image_loaded[transcoder] = true;
    }, delay);
}
function fix_news_id(news_id) {
    return news_id.split('_',1)[0];
}
function lcxGetQueryDict() {
    var url = window.location.search;
    var theRequest = new Object();
    if (url.indexOf("?") != -1) {
        var str = url.substr(1);
        strs = str.split("&");
        for(var i = 0; i < strs.length; i++) {
            theRequest[strs[i].split("=")[0]]=unescape(strs[i].split("=")[1]);
        }
    }
    return theRequest;
}
function lcxSetVisible(id, visible) {
    if ( visible ) {
        if ( !id.is(":visible") ) id.css('display','');
    } else {
        if (  id.is(":visible") ) id.css('display','none');
    }
}
function lcxLoadUploadLibrary() {
    if ( window.lcx_upload_js_loaded === true ) return;
    var script = document.createElement('script');
    script.src = '/static/lcx/simpleUpload.js';
    script.onload = function () {};
    document.head.appendChild(script);
    window.lcx_upload_js_loaded = true;
}
function lcxBuildUploadServerPrefix() {
    var trans_map = {
        'po': '/remote/image/old',
        'pn': '/remote/image/new',
        'pt': '/remote/image/test',
        'dt': 'http://107.167.122.41',
        'do': 'http://img-src.transcoder.opera.com',
        'dn': 'http://img-cms.transcoder.opera.com',
    };
    return trans_map[window.lcx_imgup_prefix] || 'http://img-cms.transcoder.opera.com';
}
function lcxGetNewsInfoJson(event) {
    try {

        var button   = $(event.currentTarget);
        var prefix   = button.prev().attr('name').slice(0,-8);
        var fieldset = button.closest('fieldset');
        var entry_id = button.prev().val();
        var country  = fieldset.find("input[name='"+prefix+"country']").val();
        var language = fieldset.find("input[name='"+prefix+"language']").val();
        var url_ad   = fieldset.find("input[name='"+prefix+"url']").val();
        var newstype = $("select[name='news_type']").val();
        var transapi = "/api/v1/transcode/?entry_id="+entry_id+"&country="+country+"&language="+language+"&newstype="+newstype+"&url="+url_ad;
        if( !entry_id ) {
            alert('Enter entry_id');
            return false;
        } else if ( country == "all" ) {
            alert('Transcode API does NOT support country value is [all]');
            return false;
        } else if ( entry_id.toLowerCase()=="ad" ) {
            if ( newstype=="ads" ) {
                if (!country || !language || !url_ad) {
                    alert('Need Country/Language and OpenType=original when push Advertisement');
                    return false;
                }
            } else if ( newstype=="web_activity" ) {
                if (!country || !language || !url_ad) {
                    alert('Need Country/Language and OpenType=original when push Web Activity');
                    return false;
                }
            } else if ( newstype=="shake" ) {
                if (!country || !language) {
                    alert('Need Country/Language and OpenType=original when push Shake');
                    return false;
                }
            } else {
                alert('ArticleType/OpenType mismatch when entry_id is ad.');
                return false;
            }
        }
        button.attr("disabled", true);
        $.getJSON(transapi, function(json) {
            if ( 'id' in json ) {
                $("input[name='"+prefix+"url']").val(json.url);
                $("input[name='"+prefix+"title']").val(json.title);
                $("input[name='"+prefix+"country']").val(json.country);
                $("input[name='"+prefix+"category']").val(json.category);
                $("input[name='"+prefix+"language']").val(json.language);
                $("input[name='"+prefix+"trans_url']").val(json.trans_url);
                $("input[name='"+prefix+"news_id']").val(json.id);
                $("input[name='"+prefix+"domain']").val(json.domain);
                $("input[name='"+prefix+"summary']").val(json.summary);
                $("input[name='"+prefix+"push_icon']").val(json.push_icon);
                if( json.lcx_last_user ) {
                    button.after('<div><b style="position:absolute;"><a target="_blank" href="'+window.location.pathname.replace('/add/','/')+'?entry_id='+entry_id+'" style="color:#b94a48;font-size:12px;display:block;">Record already inserted by '+json.lcx_last_user+' within last 3 days ！！！</a></b><b>&nbsp</b></div>');
                } else if (json.lcx_error) {
                    button.after('<div><a target="_blank" href="'+transapi+'" style="color:#b94a48;font-size:12px;display:block;position:absolute;text-decoration:none;">'+json.lcx_error+'</a><b>&nbsp;</b></div>');
                } else if (json.lcx_warn) {
                    button.after('<div><a target="_blank" href="'+transapi+'" style="color:#999;font-size:12px;display:block;position:absolute;text-decoration:none;">'+json.lcx_warn+'</a><b>&nbsp;</b></div>');
                } else {
                    button.next().remove();
                }
                if( entry_id.length < 5 ) {
                    button.prev().val(json.entry_id);
                }
            } else {
                alert(JSON.stringify(json));
            }
        }).fail(function(xhr, status, error) {
            button.prev().val("");
        }).always(function() {
            button.attr("disabled", false);
        });
    } catch(e) {
        alert(e);
    }
}
function lcxGetNewsIconPath(event) {
    try {
        var button   = $(event.currentTarget);
        var image    = button.parent().find('input');
        var fieldset = button.closest('fieldset');
        var progbar  = fieldset.find('#icon_upload_progress');
        var push_icon_url = image.val();
        progbar.text('');
        image.attr('readonly',true).val('');
        if( !push_icon_url ) {
            alert('Empty push_icon_url');
            return false;
        }
        progbar.text('contact with image server ...');
        $.ajax({
            url: lcxBuildUploadServerPrefix() + '/assets/v2/download',
            type: 'post',
            data: '{"url":"' + push_icon_url + '"}',
            headers: {
                "Content-Type": 'application/json', // 'text/plain' can prevent trigger CORS preflight
            },
            dataType: 'json',
            success: function (json) {
                if ( 'id' in json ) {
                    image.attr('readonly',false).val( json.img_server_url+'/'+json.id+'?width=116&height=116' );
                    image.attr('readonly',false).val( 'http://img.transcoder.opera.com/assets/v2/'+json.id+'?width=116&height=116' );
                } else {
                    alert(json);
                }
                progbar.text('');
            },
            error: function (jqXHR, textStatus, errorThrown) {
                progbar.text( 'ImageServerError：（'+errorThrown+'， '+push_icon_url+'）' );
            }
        });
    } catch(e) {
        alert(e);
    }
}
function lcxGetUploadImgPath(event) {
    try {
        lcxLoadUploadLibrary();
        var button   = $(event.currentTarget);
        var fieldset = button.closest('fieldset');
        var prefix   = fieldset.find('.field-push_icon input').attr('name').slice(0,-9);
        var image    = fieldset.find('.field-push_icon input');
        var upload   = fieldset.find('#local_icon_upload');
        var progbar  = fieldset.find('#icon_upload_progress');
        var filename = button.val();
        button.simpleUpload(lcxBuildUploadServerPrefix()+"/assets/v1/local/upload", {
            start: function(file){
                image.attr('readonly',true).val('');
                upload.prop('disabled',true);
                progbar.css('margin-left','10px').text('reading');
            },
            progress: function(progress){
                progbar.text(Math.round(progress) + '%');
                if(progress>99) $('#icon_upload_progress').text('waiting');
            },
            success: function(data){
                progbar.text('loading');
                image.attr('readonly',false).val( data.img_server_url+'/'+data.id+'?width=116&height=116' );
                image.attr('readonly',false).val( 'http://img.transcoder.opera.com/assets/v2/'+data.id+'?width=116&height=116' );
                setTimeout(function() {
                    upload.prop('disabled',false);
                    progbar.css('margin-left','10px').text('success');
                }, 500);
            },
            error: function(error){
                progbar.text(error.name + ': ' + error.message);
                upload.prop('disabled',false);
            }
        });
    } catch(e) {
        alert(e);
    }
}
function lcxSetNewsIconPath(element) {
    try {
        var jstyle   = $(element);
        var fieldset = jstyle.closest('fieldset');
        var button   = jstyle.parent().find('button');
        var prefix   = jstyle.parent().find('input').attr('name').slice(0,-9);
        var preview  = fieldset.find("#icon_preview");
        var upload   = fieldset.find("#local_icon_upload");
        var push_icon_url = jstyle.parent().find('input').val();
        var push_icon_disabled = $("input[name='"+prefix+"push_icon']").is('[readonly]');
        var g_push_icon_url = prefix.replace('-','_').replace('-','_') + 'push_icon_url';
        if ( g_push_icon_url.indexOf('__prefix__')>=0 ) return;
        if ( push_icon_url.length>8 && !push_icon_url.match("^https?://") ) {
            push_icon_url = 'http://' + push_icon_url;
            jstyle.parent().find('input').val(push_icon_url);
        }
        if ( preview.attr('src') != push_icon_url ) {
            preview.attr('src', push_icon_url.length>8 ? push_icon_url : '');
        } else if ( preview.attr('e')!='0' && preview.prop('complete') && push_icon_url.indexOf('img.transcoder.opera.com')>0 ) {
            if ( ((Date.now() - parseInt( preview.attr('t') ))||86400000) > 10000 ) {
                preview.attr('src', push_icon_url);
                preview.attr('t', Date.now());
            }
        }
        if ( push_icon_url == '' ) {
            var local_icon_upload_visible = push_icon_disabled ? false : true;
            lcxSetVisible(upload, local_icon_upload_visible);
            lcxSetVisible(button, false);
        } else {
            var transicon_url_click_visible = push_icon_disabled ? false : true;
            lcxSetVisible(upload, false);
            lcxSetVisible(button, transicon_url_click_visible);
            button.attr('disabled', preview.attr('e')!='0');
        }
    } catch(e) {
        alert(e);
    }
}
function lcxOnArticleTypeChange(event) {
    try {
        var select   = event.currentTarget;
        var toggle   = document.getElementById("fieldsetcollapser0");
        if ( select.options[select.selectedIndex].value == "breaking" ) {
            if ( toggle.text.toLowerCase() == "show" ) toggle.click();
            window.scrollTo(0, $(toggle).offset().top-430);
        }
    } catch(e) {
        alert(e);
    }
}
function lcxOnPushAllChange(event) {
    try {
        var checkbox = $(event.currentTarget ? event.currentTarget : event.target);
        var checked  = checkbox.is(':checked');
        var football = $("#id_prefer_football");
        var keyword  = $("#id_prefer_keyword");
        var city     = $("#id_city");
        var controls = $("#id_prefer_category_from").parent().parent().parent();
        if (checked) {
            controls.css('position', 'relative');
            $("#id_prefer_category_to").on("DOMNodeInserted", function(event) {
                $("#id_prefer_category_remove_all_link")[0].click();
                //alert("Can not set subscription info when push to all users !");
            });
            if ( controls.children().last().hasClass("selector") )
                controls.append('<div id="lcx_disabled" style="width: 100%;height: 100%;position: absolute;top: 0;left: 0;opacity: 0.2;background-color: #eeeeee;"></div>');
        } else {
            controls.css('position', '');
            $("#id_prefer_category_to").off("DOMNodeInserted");
            $("#lcx_disabled").remove();
        }
        football.attr("disabled", checked);
        keyword.attr("disabled", checked);
        city.attr("disabled", checked);
        if(checked) $("#id_prefer_category_remove_all_link")[0].click();
        if(checked) football.val("");
        if(checked) keyword.val("");
        if(checked) city.val("");
    } catch(e) {
        alert(e);
    }
}
function lcxOnHoverTransButton(event) {
    try {
        var span     = $(event.currentTarget);
        if ( event.type == "mouseover" ) {
            var prefix   = span.prev().attr('name').slice(0,-8);
            var entry_id = span.prev().val().trim();
            var url_ad   = $("input[name='"+prefix+"url']").val().trim() || $("input[name='"+prefix+"trans_url']").val().trim();
            if( !entry_id && url_ad ) {
                span.children()[1].style.display = 'inline-block';
            }
        } else if ( event.type == "mouseout" ) {
            span.children()[1].style.display = 'none';
        }
    } catch(e) {
        alert(e);
    }
}
function lcxGetAdsInfoJson(event) {
    try {
        var button   = $(event.currentTarget);
        var span     = button.parent();
        var prefix   = span.prev().attr('name').slice(0,-8);
        var fieldset = span.closest('fieldset');
        var country  = fieldset.find("input[name='"+prefix+"country']").val();
        var url_ad   = $("input[name='"+prefix+"url']").val().trim() || $("input[name='"+prefix+"trans_url']").val().trim();
        if( !url_ad || !country ) {
            alert('Enter entry_id and Country/Language');
            return false;
        }
        span.prev().val("auto");
        $("input[name='"+prefix+"url']").val(url_ad);
        $("input[name='"+prefix+"category']").val("Advertisement");
        $("input[name='"+prefix+"trans_url']").val(url_ad);
        $("input[name='"+prefix+"news_id']").val("auto");
        $("input[name='"+prefix+"domain']").val( url_domain(url_ad) );
    } catch(e) {
        alert(e);
    }
}
