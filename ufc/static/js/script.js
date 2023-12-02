document.addEventListener('DOMContentLoaded', function() {
  // Initialize Materialize sidenav
  let sidenavElements = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenavElements);

  // Initialize Materialize select dropdown
  let selectElements = document.querySelectorAll('select');
  M.FormSelect.init(selectElements);

  // Additional code for hiding label on select change
  var weightClassSelect = document.getElementById('weight_class');
  var weightClassLabel = document.querySelector('label[for="weight_class"]');

  weightClassSelect.addEventListener('change', function() {
      // Hide the label when an option is selected
      weightClassLabel.style.display = (weightClassSelect.value === "") ? "inline" : "none";
  });
});
