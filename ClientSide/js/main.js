var REFRESH_RATE = 1000;

var mainloop = [
  function() { gamelist('#gamelist'); },
];

$(document).ready(function() {
  for (i in mainloop) {
    setInterval(mainloop[i], REFRESH_RATE);
  }
})
