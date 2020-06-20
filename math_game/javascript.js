
var playing= false;
var score;
var action;
var timeremaining;
var correct;
// if we cick on the start/reset
document.getElementById("startreset").onclick=function(){
  // if we are playing
    if(playing == true){
      location.reload();// reload the page

      
    }else{// if we are not playing
      playing=true;

      score=0;// set scire to zero

      document.getElementById("scorevalue").innerHTML=score;
      document.getElementById("time").style.display="block";//show the countdoun box
      timeremaining=60;
      document.getElementById("timevalue").innerHTML=timeremaining;
      hide("gameover");
      document.getElementById("startreset").innerHTML="reset";

      //start countdown
      startcountdown();
      
      //generate question ans answes
      generate();
    }
}
// clicking on the answe box
for(i=1;i<5;i++){
  document.getElementById("box"+i).onclick=function(){
  if(playing == true){
     if(this.innerHTML == correct){
       //correct answer
       score++;
       document.getElementById("scorevalue").innerHTML=score;
       // hide the wrong box
       hide("wrong");
       show("correct");
       setTimeout(function(){
         hide("correct");
       },1000);
       
       //generate a new qustion
       
       generate();
       
     }else{//wrong answer
       hide("correct");
       show("wrong");
       setTimeout(function(){
         hide("wrong");
       },1000);
       
     }
     }
}
}


// if w click on the answer box
// if we arepalying or not
// if the answer is coorct
// if yes
// increase th score by 1
// show the corrct box for 1 s
// generate new q box
//no
// show try agsin box

//functions
//start counter
function startcountdown(){
  action = setInterval(function(){
    timeremaining -= 1;
          document.getElementById("timevalue").innerHTML=timeremaining;
    if(timeremaining==0){
      stopcountdown();
      document.getElementById("gameover").style.display="block";
      document.getElementById("gameover").innerHTML="<p>game over</p><p>your score is " + score + "</p>";
      hide("time");
      hide("correct");
      hide("wrong");
      playing=false;
      document.getElementById("startreset").innerHTML="start game";
      
    }
    
  

  },1000)
}
// stop the counter
function stopcountdown(){
        clearInterval(action);
  

}

// hide the elements
function hide(Id){
  document.getElementById(Id).style.display="none";
}

// show the elements
function show(Id){
  document.getElementById(Id).style.display="block";
}

//generate quation and nswes
function generate(){
  var x= 1 + Math.round(9*Math.random());
    var y= 1 + Math.round(9*Math.random());
  correct= x*y;
  document.getElementById("question").innerHTML= x+ "x" + y;
  var corrctposition = 1+ Math.round(3*Math.random());
  document.getElementById("box"+corrctposition).innerHTML= correct;// fill one box witht th correct answer;
  // fill other boxes with wrong answer
  for(i=1;i<5;i++){
    if(i!= corrctposition){
      var wronganswer ;
      do{
        wronganswer= (1 + Math.round(9*Math.random()))*(1 + Math.round(9*Math.random()));
      document.getElementById("box"+i).innerHTML=wronganswer;
      }while(wronganswer == correct)
    }
    
  }

}