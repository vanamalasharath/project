var playing= false;
var score;
var trails;
var fruits=['apple','banana','orange'];
var step;
var action;

$(function(){
  // clicl on the start or reset buttopn
  $("#startreset").click(function(){
    // we are playing
    if(playing == true){
       //reload the page
      location.reload();
       }else{
         
         playing=true;// game initiated
         
         score=0;// set the score to zero
         
         $("#scorevalue").html(score);
         // show the trail box
         $("#trails").show();
         trails=3;
         addhearts();
         
         // hide th hameover box
         $("#gameover").hide();
         
         // change the button to reset
         $("#startreset").html("reset");
         
         // start sending the fruits
         
         startaction();
         
       }
    
  });
  
$("#fruit1").mouseover(function(){
  score++;
  $("#scorevalue").html(score);//updating the score
  document.getElementById("sound").play();
  
  // stop the fruit going down
  clearInterval(action);
  // hide the fruit
  $("#fruit1").hide("explode",500);
  // send an new fruit
  setTimeout(startaction,500);
  //startaction();
});


// no
// show the trils left
// change he button to reset game
//creae a random fruit
// move the fruit down
// is the fruit is too low
// no-> repeat nuber 2
// if the fruit is too low
// yes-> do we have ay trails left
// if trails is yes -> we will create a new random fruit by removinf one heart


function addhearts(){
  
  $("#trails").empty();
  for(i=0;i<trails;i++){
           $("#trails").append('<img src="images/heart.png" class="life">');
         }
}


function startaction(){
  
  $("#fruit1").show();
  choosefruit();
  $("#fruit1").css({'left':  Math.round(550*Math.random()) , 'top': -20});
  
  step= 1+ Math.round(5*Math.random());// change the step
  action= setInterval(function(){
    $("#fruit1").css('top',$("#fruit1").position().top +step);
    
    if($("#fruit1").position().top > $("#fruitcontainer").height()){
      // check if any trails left
      if(trails > 1){
         $("#fruit1").show();
            choosefruit();
          $("#fruit1").css({'left':  Math.round(550*Math.random()) , 'top': -20});
  
           step= 1+ Math.round(5*Math.random());// change the step
        
        trails= trails-1;
        
        addhearts();
        
         
         }else{// game over
           playing=false;
           $("#startreset").html("start game");
           $("#gameover").show();
           $("#gameover").html('<p>game over</p><p>your score is ' + score +'</p>');
           $("#trails").hide();
           stopaction();
         }
    }
  },10);
  
  
  
}
// selecting a random fruit
function choosefruit(){
  $("#fruit1").attr('src','images/' + fruits[Math.floor(2*Math.random())]+ '.png');
}
// stop dropping fruits
function stopaction(){
  clearInterval(action);
  $("#fruit1").hide();
  
}
  
  });