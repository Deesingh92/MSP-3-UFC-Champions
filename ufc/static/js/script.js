document.addEventListener('DOMContentLoaded', function () {
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

  document.getElementById('btn-all').addEventListener('click', function () {
    filterChampions('all');
  });

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
});
