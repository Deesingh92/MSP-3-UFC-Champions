document.addEventListener('DOMContentLoaded', function () {
    // Initialize Materialize CSS side navigation
    let sidenavElements = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenavElements);
  
    function resetFilters() {
      var championsContainer = document.getElementById('champions-container');
      var championItems = championsContainer.querySelectorAll('.col');
  
      championItems.forEach(function (item) {
        item.style.display = 'block';
      });
    }
  
    function filterChampions(weightClass) {
      var championsContainer = document.getElementById('champions-container');
      var championItems = championsContainer.querySelectorAll('.col');
  
      championItems.forEach(function (item) {
        var championWeightClass = item.querySelector('.weight-class').textContent.toLowerCase();
  
        if (weightClass === 'all' || championWeightClass === weightClass.toLowerCase()) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }
  
    function filterChampionsByName(name) {
      var championsContainer = document.getElementById('champions-container');
      var championItems = championsContainer.querySelectorAll('.col');
  
      championItems.forEach(function (item) {
        var championName = item.querySelector('.card-title').textContent.toLowerCase();
  
        if (championName.includes(name.toLowerCase())) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }
  
    function confirmDelete(championId) {
      if (confirm("Are you sure you want to delete this champion?")) {
        // Continue with the deletion
        window.location.href = `/delete_champion/${championId}`;
      } else {
        // Cancel the deletion
      }
    }
  

  
    document.getElementById('btn-flyweight').addEventListener('click', function () {
      filterChampions('Flyweight');
    });
  
    document.getElementById('btn-bantamweight').addEventListener('click', function () {
      filterChampions('Bantamweight');
    });
  
    document.getElementById('btn-featherweight').addEventListener('click', function () {
      filterChampions('Featherweight');
    });
  
    document.getElementById('btn-lightweight').addEventListener('click', function () {
      filterChampions('Lightweight');
    });
  
    document.getElementById('btn-welterweight').addEventListener('click', function () {
      filterChampions('Welterweight');
    });
  
    document.getElementById('btn-middleweight').addEventListener('click', function () {
      filterChampions('Middleweight');
    });
  
    document.getElementById('btn-light-heavyweight').addEventListener('click', function () {
      filterChampions('Light Heavyweight');
    });
  
    document.getElementById('btn-heavyweight').addEventListener('click', function () {
      filterChampions('Heavyweight');
    });
  
    document.getElementById('reset-filters-btn').addEventListener('click', function () {
      resetFilters();
    });
  
    document.getElementById('searchForm').addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent the default form submission behavior
  
      var searchName = document.getElementById('searchName').value;
      filterChampionsByName(searchName);
    });
  
    // Add event listeners for the delete buttons
    var deleteButtons = document.querySelectorAll('.delete-champion-btn');
    deleteButtons.forEach(function (button) {
      button.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default link behavior
        var championId = button.getAttribute('data-champion-id');
        confirmDelete(championId);
      });
    });
  });
  