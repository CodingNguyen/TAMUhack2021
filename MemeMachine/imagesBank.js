// randomize Meme displayed on webpage

window.onload = choosePic;

var myPic = new Array();

function choosePic() {
     var randomNum = Math.floor(Math.random() * myPic.length);
     document.getElementById("chosenPic").src = myPic[randomNum]
}
