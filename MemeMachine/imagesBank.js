// randomize Meme displayed on webpage


function getRandomImage(){
    var randomNumber = Math.floor(Math.random() * 10) + 5;
    var imageName = "_Img" + randomNumber;
    document.getElementById("imageid").src= "ImagePath" + "/" + imageName
}
