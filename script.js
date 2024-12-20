const cardArtis = document.querySelectorAll(".card-artis, .card-artis2");

cardArtis.forEach(function (card) {
  const playIcon = card.querySelector(".play");

  card.addEventListener("mouseover", function () {
    playIcon.style.display = "flex";
    playIcon.style.opacity = "1";
    playIcon.style.transform = "translateY(0)"; 
  });

  card.addEventListener("mouseout", function () {
    playIcon.style.opacity = "0"; 
    playIcon.style.transform = "translateY(20px)";
  });
});
