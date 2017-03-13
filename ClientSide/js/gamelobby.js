var REFRESH_RATE = 1000;

// WATCH OUT ! SPAGHETTI CODE !!

/*
var mainloop = [
  function() { gamelist('#gamelist'); },
]; //*/

$(document).ready(function() {

  // Username set/get
  var usernameInput = $('#username');
  usernameInput.val(Cookies.get('username'));
  usernameInput.on('input', function(e) {
    Cookies.set('username', usernameInput.val());
  });

  var createButton = $('#creategame');
  createButton.click(function(e) {
    var username = Cookies.get('username');
    if (username) creategame(username, function(gameid) {
      Cookies.set('game', {id: gameid});
      window.location.replace('/play/');
    });
    else alert('Please enter your username...');
  });

  var gamelisting = function() {
    gamelist('#gamelist', function(game) {
      Cookies.set('game', game);
      joingame(game.id, Cookies.get('username'));
    });
  }

  gamelisting();
  setInterval(gamelisting, REFRESH_RATE);

  /*
  // Mainloop
  for (i in mainloop) {
    setInterval(mainloop[i], REFRESH_RATE);
  } //*/
})
