
/*
 * -------------------------------------------------------
 * Project: Pins Grid
 * Version: 0.1.0
 *
 * Author:  Yury Egorenkov
 * Site:     http://ru.linkedin.com/in/yuryegorenkov
 * Contact: yury.egorenkov@gmail.com
 *
 *
 * Copyright (c) 2015 Yury Egorenkov
 * -------------------------------------------------------
 */

var ready=function(){};$(document).ready(ready),$(document).on("page:load",ready);var ready=function(){function removeClassByWildcard(el,wildcard){$(el).removeClass(function(index,css){var regex=new RegExp("(^|\\s)"+wildcard+"\\S+","g");return(css.match(regex)||[]).join(" ")})}function setColumns(columns){pinColumns=columns+zoom,pinColumns=1>pinColumns?1:pinColumns,classSwitch&&(removeClassByWildcard(".pins-grid","pins-grid-"),$(".pins-grid").addClass("pins-grid-"+pinColumns))}function setPinChanger(media,columns){media.addListener(function(changed){changed.matches&&(setColumns(columns),rearrangePins())})}function addMediaQueryAction(query,columns){var media=window.matchMedia(query);media.matches&&setColumns(columns),setPinChanger(media,columns)}function addMaxWidthMedia(max,columns){var query="(max-width: "+max+")";addMediaQueryAction(query,columns)}function addMinWidthMedia(min,columns){var query="(min-width: "+min+")";addMediaQueryAction(query,columns)}function addMinMaxWidthMedia(min,max,columns){var query="(min-width: "+min+") and (max-width: "+max+")";addMediaQueryAction(query,columns)}function initSettings(settings){var s=settings;for(var i in s){var columns=s[i].columns;0!=i?i!=s.length-1?addMinMaxWidthMedia(s[i-1].width,s[i].width,columns):addMinWidthMedia(s[i-1].width,columns):addMaxWidthMedia(s[i].width,columns)}}function previousN(el,n){var prev=$(el).prev();if(prev.length>0){for(var i=1;n>i;i++)prev=prev.prev();return prev}return[]}function translatePin(el,height){$(el).css({transform:"translate(0, "+height+"px)"})}function rearrangePin(el){var gridTop=$(".pins-grid").offset().top,gridPadding=$(".pins-grid").css("padding-top").replace(/[^-\d\.]/g,""),prev=previousN(el,pinColumns),height=0;prev.length>0&&(height=prev.offset().top+prev.height()+marginTop-gridTop-gridPadding);var height=1===pinColumns?0:height;translatePin(el,height);var globalOffset=$(".pins-grid").offset().top,last=$(".pins-grid .pin").last();$(".pins-grid").css("height",last.offset().top+last.height()-globalOffset)}function rearrangePins(){$(".pins-grid .pin:visible").each(function(i,el){rearrangePin(el)})}function removePin(img){var pin=$(img).closest(".pin");pin.remove(),loadPinImage()}function loadPinImage(){clearTimeout(killImageTimeout),$(".pins-grid img[data-src]").slice(0,1).each(function(i,d){$(d).error(function(){removePin(d)}),$(d).attr("src",$(d).attr("data-src")),$(d).removeAttr("data-src"),killImageTimeout=setTimeout(function(){removePin(d)},5e3)})}var inited=!1,marginTop=15,classSwitch=!0,zoom=0,defaultSettings={classSwitch:!0,zoomable:!0,resolutions:[{width:"768px",columns:1},{width:"992px",columns:3},{width:"1200px",columns:4},{width:"",columns:5}]},pinColumns=1;window.getSameItems=function(array,column,index){for(var result=[],i=index-column;i>=0;i-=column)result.push(array[i]);return result};var killImageTimeout=null;$(".pins-grid img").on("load",function(){var image,img,pin,ratio;return img=$(this),image=new Image,image.src=img.attr("src"),pin=img.closest(".pin"),image.naturalWidth<300?void removePin(img):(ratio=1*image.naturalHeight/image.naturalWidth*100,img.closest(".image").css("padding-bottom",ratio+"%"),rearrangePin(pin),pin.css("z-index","0"),img.css("opacity","1"),pin.css("opacity","1"),void loadPinImage())}),$(window).resize(function(){rearrangePins()}),window.pinGrid=function pinGrid(settings){inited=!0,classSwitch=settings.classSwitch,initSettings(settings.resolutions),settings.zoomable&&($(".pins-grid-controls").css("display","block"),$(".zoom-in").on("click",function(){pinGrid.zoom(-1)}),$(".zoom-out").on("click",function(){pinGrid.zoom(1)})),loadPinImage()},window.pinGrid.zoom=function(newZoom){zoom=newZoom,setColumns(pinColumns),rearrangePins()},setTimeout(function(){inited||pinGrid(defaultSettings)},300)};$(document).ready(ready),$(document).on("page:load",ready);