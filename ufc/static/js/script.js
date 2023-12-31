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

  function filterChampionsByWeight(weightClass) {
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
      window.location.href = `/delete_champion/${championId}`;
  }

  // Add event listeners for all weight class buttons
  var weightClassButtons = document.querySelectorAll('.weight-class-btn');
  weightClassButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      var weightClass = button.getAttribute('data-weight-class');
      filterChampionsByWeight(weightClass);
    });
  });

  // Add event listener for reset-filters-btn if it exists
  var resetFiltersButton = document.getElementById('reset-filters-btn');
  if (resetFiltersButton) {
    resetFiltersButton.addEventListener('click', function () {
      resetFilters();
    });
  }

  // Add event listener for searchForm if it exists
  var searchForm = document.getElementById('searchForm');
  if (searchForm) {
    searchForm.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent the default form submission behavior

      var searchNameElement = document.getElementById('searchName');
      if (searchNameElement) {
        var searchName = searchNameElement.value;
        filterChampionsByName(searchName);
      } else {
        console.error("Element with ID 'searchName' not found.");
      }
    });
  }

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
