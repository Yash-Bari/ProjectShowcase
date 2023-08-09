document.addEventListener("DOMContentLoaded", function() {
    const searchButton = document.getElementById("search-button");
    const searchInput = document.getElementById("search-input");
    const projectCards = document.querySelectorAll(".project-card");
  
    searchButton.addEventListener("click", function() {
      const searchTerm = searchInput.value.toLowerCase().trim();
      projectCards.forEach(function(card) {
        const projectTitle = card.querySelector(".project-title").textContent.toLowerCase();
        const projectAuthor = card.querySelector(".project-author").textContent.toLowerCase();
        if (projectTitle.includes(searchTerm) || projectAuthor.includes(searchTerm)) {
          card.style.display = "block";
        } else {
          card.style.display = "none";
        }
      });
    });
  });
  