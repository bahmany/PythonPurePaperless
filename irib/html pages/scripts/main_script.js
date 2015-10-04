//var FCKeditorAPI = false;

var def_url="py_main.py?mid="

    function openlocaltion(dest_div,mid,param) {
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();

    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var str = xmlhttp.responseText;
	    document.getElementById(dest_div).innerHTML=str;
	}
    }
    
	
	//    xmlhttp.open("GET", def_url+mid+"&"+param, true);
    //"py_get_drop_down_items.py"
    //xmlhttp.send();
	
	window.open(def_url+mid+"&"+param);
	//window.location.url=def_url+mid+"&"+param;
	
	
	
	
}
 

function selected_letter_type(i) {
    $('#div_varede').hide();
    $('#div_sadereh').hide();
    $('#div_dakheli').hide();

    if (i == 1) {
        $('#div_varede').show();
    }
    if (i == 2) {
        $('#div_sadereh').show();
    }
    if (i == 3) {
        $('#div_dakheli').show();
    }

}


function set_Autocomplete_fill(ObjectName, RequestAddress) {
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();

    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var str = xmlhttp.responseText;
            var lines = str.split("!");
            // i[0] is null we start from i[1]
            /* در این قسمت سورس کار پالایش خط ارسال شده بوسیله آژاکس
            که بعد از تست های فراوان مجبور شدم همه را در یک رکویست بفرستم
            انجام میشود
            هر آبجکت به طبق چینش در خط به متقیر بایند میشود */
            for (var i = 1; i < lines.length; i++) {
                var _lines = lines[i].split(":");
                var _obj = ObjectName.split(",");
                var bb = _lines[1].split(",");
                $(_obj[i-1]).autocomplete({
                    source: bb
                });
             }
        }
    }
    xmlhttp.open("GET", RequestAddress, true);
    //"py_get_drop_down_items.py"
    xmlhttp.send();
}




function convert_py_gen_string_to_jtable_array(splitter_step1,splitter_step2,str) {
var st1 = [];
str=str.replace("::0::","::غیرفعال::");
str=str.replace("::1::","::فعال::");

var new_=[];

st1=str.split(splitter_step1)
for (var i=1;i<st1.length;i++) {
	var st2=[];
	var __d=st1[i].split(splitter_step2);
	for (var g=1;g<__d.length;g++) {
		st2.push(__d[g]);
	}
	//st2=st1[i].split(splitter_step2);
	new_.push(st2);
}
return new_;	
}


function gl(controlname_byID)
{
	var sss=controlname_byID;
	sss="#"+controlname_byID;
	var a=[];
	if ($(sss).is(":radio")){
		a[1]=document.getElementById(controlname_byID).checked; 
	}
	if ($(sss).is(":checkbox")){
		a[1]=document.getElementById(controlname_byID).checked; 
	}
	if ($(sss).is(":text")){
		a[1]=document.getElementById(controlname_byID).value;
	}
	if ($(sss).is(":password")){
		a[1]=document.getElementById(controlname_byID).value;
	}
	if ($(sss).is("select")){
		a[1]=document.getElementById(controlname_byID).value;
	}
	
	a[0]=controlname_byID;

	return a;

}

function setValueToObject(objname,value) {
	sss=document.getElementById(objname);
	if ($(sss).is(":radio")){
		if (value[0] == "1") {
		document.getElementById(objname).checked=true; 
		} else {
			document.getElementById(objname).checked=false; 
		}
		
	}
	if ($(sss).is(":checkbox")){
		if (value[0] == "1") {
		document.getElementById(objname).checked=true; 
		} else {
			document.getElementById(objname).checked=false; 
		}
	}
	if ($(sss).is(":text")){
		document.getElementById(objname).value=value
	}
	if ($(sss).is(":password")){
		document.getElementById(objname).value=value;
	}
	if ($(sss).is("select")){
		_value = value.replace(/(\r\n|\n|\r)/gm,"");
		
		    var sel = document.getElementById(objname);
        		var val = _value;
			for(var i = 0, j = sel.options.length; i < j; ++i) {
			    if(sel.options[i].value === val) {
			       sel.selectedIndex = i;
			       break;
			    }
			}
		
		
		//document.getElementById(objname).selectedIndex=_value;
	}
	
}

	

function convert_shamsi_to_milady(shamsi)
{
	var aa="";
	if (shamsi != "")
		{
			var sh = shamsi.split("/");
			var g = JalaliDate.jalaliToGregorian(sh[0],sh[1],sh[2]);
			aa=(g[0]+"/"+g[1]+"/"+g[2]);
		}
	return aa;
	}
	
function convert_Milady_to_shamsi(milady)
{
	var aa="";
	if (milady != "")
		{
			var sh = milady.split("/");
			var g = JalaliDate.gregorianToJalali(sh[0],sh[1],sh[2]);
		y=String(g[0]);
		m=String(g[1]);
		d=String(g[2]);
		if (m.length == 1) {m = "0"+m;	}
		if (d.length == 1) {d = "0"+d;	}
		
			aa=(y+"/"+m+"/"+d);
		}
	return aa;
	}
	
function getCurrentDateAndConvert(where_to_put)
{
var currentTime = new Date();
var month = currentTime.getMonth() + 1;
var day = currentTime.getDate();
var year = currentTime.getFullYear();

var sss=convert_Milady_to_shamsi(String(year)+"/"+String(month)+"/"+String(day))
sss =sss+" "+
(currentTime.getHours().toString())+":"+
(currentTime.getMinutes().toString())+":"+
(currentTime.getSeconds().toString());

document.getElementById(where_to_put).innerHTML = sss;
setTimeout("getCurrentDateAndConvert('timerr');",1000)
}

var frm_letter_alarm = [];
function check_var_existant(_ty,obj_name)
{
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();

    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var str = xmlhttp.responseText;
            if (str == 1){
            	document.getElementById(obj_name).style.backgroundColor="#DDFFDD";
            	var fff=[];
            	
            	for (var i=0;i<frm_letter_alarm.length;i++)
            		{
            		if (frm_letter_alarm[i][0] == obj_name)
            			{
            			
            			} else
            				{
            				fff.push(frm_letter_alarm[i]);
            				}

            		}
            	frm_letter_alarm = fff;
            } else
            	{
            	var fff=[];
            	for (var i=0;i<frm_letter_alarm.length;i++)
        		{
        		if (frm_letter_alarm[i][0] == obj_name)
        			{
        			
        			} else
        				{
        				fff.push(frm_letter_alarm[i]);
        				}

        		}
        	frm_letter_alarm = fff;

        	document.getElementById(obj_name).style.backgroundColor="#FFEFE8";
                var ala = [];
                ala.push(obj_name);
                var lnk = "javascript:add_variant('"+obj_name+"','"+document.getElementById(obj_name).value+"','"+_ty+"')" ;


                if (_ty=='5')
		{
		ala.push("<body><strong><font color=\"#ec0000\">  اطلاعات مربوط به '''"+document.getElementById(obj_name).value+"''' یافت نشد </font></strong><br>");
           		
		}
		else {
		ala.push("<body><strong><font color=\"#ec0000\">  اطلاعات مربوط به '''"+document.getElementById(obj_name).value+"''' یافت نشد - لطفا تصحیح نمایید یا این نام را با    <a h=\"\" href=\""+lnk+"\">      کلیک بروی این قسمت      </a>      اضافه نمایید</font></strong><br>");
           	}
	     frm_letter_alarm.push(ala);
            	}
            var str="";
            for (var i=0;i<frm_letter_alarm.length;i++)
            	{
            	str=str+frm_letter_alarm[i][1];
            	}
            
            document.getElementById("div_alarm").innerHTML = str;
        }
    }
    var _name = document.getElementById(obj_name).value;
    if (_name!="") {
	
    
    xmlhttp.open("GET", "py_existant_checker.py?id="+_ty+"&name="+_name, true);
    xmlhttp.send();
    }
}
	
function add_variant(objname,var_name,var_type)
{
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();

    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            //var str = xmlhttp.responseText;
            
            check_var_existant(var_type,objname);
        }
    }
    
    xmlhttp.open("GET", "py_add_variant.py?id="+var_type+"&name="+var_name, true);
    xmlhttp.send();
}




function check_null(objectname,altertext)
{
	var bl = false;
	
	if (document.getElementById(objectname).value != "")
		{
		bl=true;
		
		} else
			{
			alert(altertext);
			bl=false;
			}
	
	return bl;
	
}




var qs = (function(a) {
    if (a == "") return {};
    var b = {};
    for (var i = 0; i < a.length; ++i)
    {
        var p=a[i].split('=');
        if (p.length != 2) continue;
        b[p[0]] = decodeURIComponent(p[1].replace(/\+/g, " "));
    }
    //alert(b["texts"]);
    return b;
})(window.location.search.substr(1).split('&'));


function handle_att_div(tp,b) {
var htrrr=b.split("?");
var ggg="";

if (tp==1) {
	for (var i=1;i<htrrr.length;i++) {
				fileaddr="files/"+htrrr[i].split(":")[2]+"";
	fileaddr=fileaddr.replace(/(\r\n|\n|\r)/gm,"");
	var yy=" <a  href=\""+fileaddr+"\">"+
	htrrr[i].split(":")[1]+"</a>---<a href='javascript:removeatt("+htrrr[i].split(":")[0]+
	")'>(حذف)</a>|";
	ggg="  "+yy+"  "+ggg;
}
}
if (tp==2) {
	for (var i=1;i<htrrr.length;i++) {
		fileaddr="files/"+htrrr[i].split(":")[2]+"";
		fileaddr=fileaddr.replace(/(\r\n|\n|\r)/gm,"");

	fileaddr=fileaddr.replace(/(\r\n|\n|\r)/gm,"");
	var yy="<a  href=\""+fileaddr+"\">"+
	htrrr[i].split(":")[1]+"</a><a href='javascript:removeatt("+htrrr[i].split(":")[0]+
	")'></a>|";
	ggg="  "+yy+"  "+ggg;
	}

	  
}


return "فایل های ضمیمه :"+ggg;


}

function removeatt(id) {
	
	    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();

    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        document.getElementById("div_att_name_"+id).style.visibility="hidden";
        }
    }
    
    xmlhttp.open("GET", "py_attachment_remove.py?id="+id, true);
    xmlhttp.send();
	
}





   function open_new_window(URL)
   {
   NewWindow = window.open(URL,"_blank","toolbar=no,menubar=0,status=0,copyhistory=0,scrollbars=yes,resizable=1,location=0,Width=500,Height=500") ;
   NewWindow.location = URL;
   }

var problem=0;
function check_on_blur(dest_obj,url,query_item_name,dependency_checkbox) {
	//text = document.getElementById(dest_obj).value;
	$("#"+dest_obj).focus().blur(
		function () {
			if (dependency_checkbox.length!=0) {
				if (document.getElementById(dependency_checkbox).checked == false) {
					return;
				}
			}
	if (document.getElementById(dest_obj).value.length != 0) {
		  var q_item=query_item_name+"="+document.getElementById(dest_obj).value;
		  $.post(url,q_item,function(data){
			  if (data[0] == "0") {
					$("#"+dest_obj).css("background-color","#DDFFCC");
			  } else
			  {
					$("#"+dest_obj).css("background-color","#FFCDCC");
					problem=1;
			  }
			});
		  	} else
	{$("#"+dest_obj).css("background-color","white");}

		}
		
	  );
}
 
 
 
 
 function Get_Cookie( check_name ) {
	// first we'll split this cookie up into name/value pairs
	// note: document.cookie only returns name=value, not the other components
	var a_all_cookies = document.cookie.split( ';' );
	var a_temp_cookie = '';
	var cookie_name = '';
	var cookie_value = '';
	var b_cookie_found = false; // set boolean t/f default f

	for ( i = 0; i < a_all_cookies.length; i++ )
	{
		// now we'll split apart each name=value pair
		a_temp_cookie = a_all_cookies[i].split( '=' );


		// and trim left/right whitespace while we're at it
		cookie_name = a_temp_cookie[0].replace(/^\s+|\s+$/g, '');

		// if the extracted name matches passed check_name
		if ( cookie_name == check_name )
		{
			b_cookie_found = true;
			// we need to handle case where cookie has no value but exists (no = sign, that is):
			if ( a_temp_cookie.length > 1 )
			{
				cookie_value = unescape( a_temp_cookie[1].replace(/^\s+|\s+$/g, '') );
			}
			// note that in cases where cookie is initialized but no value, null is returned
			return cookie_value;
			break;
		}
		a_temp_cookie = null;
		cookie_name = '';
	}
	if ( !b_cookie_found )
	{
		return null;
	}
}


function Delete_Cookie( name, path, domain ) {
if ( Get_Cookie( name ) ) document.cookie = name + "=" +
( ( path ) ? ";path=" + path : "") +
( ( domain ) ? ";domain=" + domain : "" ) +
";expires=Thu, 01-Jan-1970 00:00:01 GMT";
}
	
	
	
	
function exitfromsystem(){
window.location.href="py_user_manager.py?out=ok";
	//$.post("py_user_manager.py","out=ok",function (data){
		
	
		
//	});
	
	//location.reload(true);
	
	
}
	
	
	
	
function showModal(link) {
        var modal = new DayPilot.Modal();
        modal.top = 60; // position of the dialog top (y), relative to the visible area
        modal.width = 300; // width of the dialog
        modal.height = 250; // height of the dialog
        modal.opacity = 70; // opacity of the background
        modal.border = "10px solid #d0d0d0";  // dialog box border
        modal.closed = function() { // callback executed after the dialog is closed
            if(this.result == "OK") {  // if the
                dp.commandCallBack('refresh'); 
            }
        };
        modal.showUrl( link);
}




