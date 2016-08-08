$(document).ready(
  function(){
    var counter=0;
	  var imgurl,imgCounter;
  
    $('#container li').each(function(index){$('#container li:eq('+index+')').css('opacity', 0);});
    $("#slider").prepend('<div style="width:800px; height:300px;position:absolute; z-index:99" id="fmask"></div>');
    $('#container li:eq(0)').css('opacity', 1);
    imgurl = $('#container li:eq(1) img').attr('src');
    $('#fmask').css({'width': '0px','background-image': 'url("' + imgurl + '")'});
  function playAnim(){
      flag = true;
    
      $('#fmask').animate({width:($('#slider').width())}, 1000, function(){
          $('#slider ul li:eq('+counter+')').css('opacity', 0);	
          counter++;
          
          imgCounter = counter = (counter > ($('#slider ul li').length - 1))?0:counter;
					$('#slider ul li:eq('+counter+')').css('opacity', 1);
          
          imgCounter++;
					imgCounter = (imgCounter > ($('#slider ul li').length - 1))?0:imgCounter;
					imgurl = $('#slider ul li:eq('+imgCounter+') img').attr('src');
					$('#fmask').css({'width': '0px','background-image': 'url("' + imgurl + '")'});
      });
  }
    
  playAnim();
	setInterval(playAnim, 5000);
});