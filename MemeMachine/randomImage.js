


var images = ['0_Img', '1_Img', '2_Img', '3_Img', '4_Img', '5_Img', '6_Img', '7_Img', '8_Img', '9_Img', '10_Img', '11_Img', '12_Img', '13_Img', '14_Img', '15_Img', '16_Img', '17_Img', '18_Img', '19_Img', '20_Img', '21_Img', '22_Img', '23_Img', '24_Img', '25_Img', '26_Img', '27_Img', '28_Img'];
function random_image(image)
{
  
return image[Math.floor(Math.random()*image.length)];
     
}

console.log(random_image(images));