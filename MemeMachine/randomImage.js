// set array
var images = ['0_Img.jpg', '1_Img.jpg', '2_Img.jpg', '3_Img.jpg', '4_Img.jpg', '5_Img.jpg', '6_Img.jpg', '7_Img.jpg', '8_Img.jpg', '9_Img.jpg', '10_Img.jpg', '11_Img.jpg', '12_Img.jpg', '13_Img.jpg', '14_Img.jpg', '15_Img.jpg', '16_Img.jpg', 
'17_Img.jpg', '18_Img.jpg', '19_Img.jpg', '20_Img.jpg', '21_Img.jpg', '22_Img.jpg', '23_Img.jpg', '24_Img.jpg', '25_Img.jpg', '26_Img.jpg', '27_Img.jpg', '28_Img.jpg', '29_Img.jpg', '30_Img.jpg', '31_Img.png', '32_Img.png', '33_Img.png', '34_Img.png', '35_Img.png', '36_Img.png', '37_Img.png', '38_Img.png', '39_Img.png', '40_Img.png']



function random_image(image){
  
return image[Math.floor(Math.random()*image.length)];
     
}

function main(){
    var ChosenImg = random_image(images)
    document.getElementById("imageID").src = "Images2/" + ChosenImg;
    
    // checking output
    // console.log(src);
    console.log(random_image(images));
    console.log(ChosenImg);
}
window.onload = main
