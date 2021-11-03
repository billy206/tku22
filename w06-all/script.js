var slideIndex = 1;
showSlides(slideIndex);

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    console.log(slides.length)
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";

  for (i = 0; i < dots.length; i++) {
      console.log(dots.length)
      dots[i].className = dots[i].className.replace(" active", "");
  }


  dots[slideIndex-1].className += " active";
}