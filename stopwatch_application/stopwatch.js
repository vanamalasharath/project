$(function(){
  
  var mode= false;
  var timecounter=0;
  var lapcounter=0;
  var action;
  var lapnumber=0;
  var timeminutes, timeseconds, timemseconds, lapminutes, lapseconds, lapmseconds;
  
  
  hideshowbutons("#startbutton","#lapbutton");
  
  $("#startbutton").click(function(){
    mode=1;
    hideshowbutons("#stopbutton","#lapbutton");
    startaction();

    
  });
  
  $("#stopbutton").click(function(){
    
    hideshowbutons("#resumebutton","#resetbutton");
    clearInterval(action);
    
  });
  
  $("#resumebutton").click(function(){
    
    hideshowbutons("#stopbutton","#lapbutton");
    startaction();
    
  });
  
  
  $("#resetbutton").click(function(){
    location.reload();
    //hideshowbutons("#stopbutton","#lapbutton");
    //startaction();
    
  });
  
  
  $("#lapbutton").click(function(){
    
    if(mode==1){
      clearInterval(action);
      lapcounter=0;
      addlap();
      startaction();
    }
    
  });
  
  
  
  
  
  
  function hideshowbutons(x,y){
    $(".button").hide();
    $(x).show();
    $(y).show();
  }
  
  
  function startaction(){
    action = setInterval(function(){
      timecounter++;
      if(timecounter == 100*60*100){
        timecounter=0;
      }
      lapcounter++;
      if(lapcounter == 100*60*100){
        lapcounter=0;
      }
      updatetime();
    },10);
  }
  
  function updatetime(){
    //1min=60*100centiseconds=6000 centiseconds
    timeminutes= Math.floor(timecounter/6000);
    //i sec=100centiseconds
    timeseconds = Math.floor((timecounter%6000)/100);
    timemseconds=(timecounter%6000)%100;
    
    
    $("#timeminute").text(format(timeminutes));
    $("#timesecond").text(format(timeseconds));
    $("#timemsecond").text(format(timemseconds));

    
    
    
    lapminutesminutes= Math.floor(timecounter/6000);
    //i sec=100centiseconds
    lapsecondsseconds = Math.floor((timecounter%6000)/100);
    lapmseconds=(timecounter%6000)%100;
    
    $("#lapminute").text(format(lapminutesminutes));
    $("#lapsecond").text(format(lapsecondsseconds));
    $("#lapmsecond").text(format(lapmseconds));

  }
  
  function format(number){
    if(number<10)
      {
        return '0'+number;
      }else{
        return number;
      }
  }
  
  function addlap(){
    lapnumber++;
    
    var lapdetails = '<div class="lapc">' + '<div class="laptitle">'+ 'lap' + lapnumber +
                            '</div>' +
                            '<div class="laptimetitle">'+
                                  '<span>'+ format(lapminutesminutes) + '</span>' +
                                          ':<span>'+ format(lapsecondsseconds) + '</span>'+
                                          ':<span>'+ format(lapmseconds) + '</span>'


        
                            '</div>'+
                            
    
    '</div>';
    $(lapdetails).prependTo("#laps");
    
    
  }
  
  
});