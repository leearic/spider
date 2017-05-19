

$(function(){
	$("img.lazyload").lazyload({effect: "fadeIn"});
  	$(function(){
		FocusChange(".focus01",".focus01 .foucs660",".focus01 .foucs660 li",".focus01 .focus_btn",".focus01 .focus_btn span","on");
	});
	function FocusChange(focMain,focUl,focLi,btnBox,btnIcon,btnNow){
		var focW = $(focLi).width();
		var len = $(focLi).length;
		var index = 0;
		var focTimer = null;
		var btn = "";
		//以下代码添加按钮
		for(var i=0; i < len; i++) {
			btn += "<span></span>";
		}
		$(btnBox).append(btn);		
		$(focUl).css("width",focW * len);		
		$(btnIcon).mouseenter(function() {
			index = $(btnIcon).index(this);
			cutImgInt();
		}).eq(0).trigger("mouseenter");		
		$(focMain).hover(function() {		
			clearInterval(focTimer);
		},function() {
			focTimer = setInterval(cutImgInt,3000);//此4000代表自动播放的间隔，单位：毫秒
		});		
		function showPic(num){
			var nowLeft = -num * focW;
			$(focUl).stop(true,false).animate({"left":nowLeft+"px"},300);
			$(btnIcon).removeClass(btnNow).eq(index).addClass(btnNow);			
		}		
		function cutImgInt() {
			showPic(index);
			index++;
			if(index >= len) {index = 0;}
		}		
		var focTimer = setInterval(cutImgInt,3000);
	}
})  

$(function () {
    var ie6 = document.all;
    var dv = $('#fixmenu'), st, topv;
	var rv = $('#fix_box');
	var cv = $('.clearline2');
    dv.attr('otop', dv.offset().top); //存储原来的距离顶部的距离
	rv.attr('otop', rv.offset().top);

    $(window).scroll(function () {
        st = Math.max(document.body.scrollTop || document.documentElement.scrollTop);
		if (pagetype == 'read'){
			cv.attr('otop', cv[0].offsetTop);
			topv = parseInt(cv.attr('otop'));
		}else{
			topv = parseInt(dv.attr('otop'));
		}


		if (st > topv) {
				if (dv.css('position') != 'fixed'){
					dv.css({'position': 'fixed', top: '10px' });
					$('.ilogo').css({'display': 'block'});
				}
		} else if (dv.css('position') != 'static') {
				dv.css({ 'position': 'static' });
				$('.ilogo').css({'display': 'none'});
		}

		if (st > parseInt(rv.attr('otop'))) {
            if (rv.css('position') != 'fixed'){
				rv.css({'position': 'fixed', top: '10px' });
			}
        } else if (rv.css('position') != 'static') {
			rv.css({ 'position': 'static' });
		}
    });
 });
