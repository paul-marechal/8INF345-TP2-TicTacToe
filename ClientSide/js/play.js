var REFRESH_RATE = 1000;

var STARTED = false;

function updategrid(id) {
  var loading = $('#loading');
  var playarea = $('#playarea');

  $.getJSON('/game/grid/' + id + '/', function(grid) {
    if (isEmpty(grid)) {
      loading.show();
      playarea.hide();
    } else {
      for(i in grid) {
        for(j in grid[i]) {
          var mark = grid[i][j];

          var cell = $('.gridcell[data-x="' + i + '"][data-y="' + j + '"]');
          cell.addClass(({
            '0': '',
            'O': 'circle',
            'X': 'cross',
          })[mark]);
        }
      }

      loading.hide();
      playarea.show();
    }
  })
}



function refresh(id) {
  gameexists(id, {
    onTrue: function() {
      updategrid(id);
    },
    onFalse: function() {
      alert('The game no longer exists...');
      window.location.replace('/');
    },
  });
}

$(document).ready(function() {

  var username = Cookies.get('username');
  var game = Cookies.getJSON('game');

  if (!username || isEmpty(game)) {
    alert('you should not be here...');
    window.location.replace('/');
    return;
  }

  $.get('/game/exists/' + game.id + '/', function(exists) {
    if (exists == 'False') {
      alert('The game was cancelled...');
      window.location.replace('/');
    }
  });

  var quitButton = $('#quit');
  quitButton.click(function(e) {
    $.get('/game/quit/' + game.id + '/' + username + '/', function() {
      window.location.replace('/');
    });
  });

  creategrid('#grid', function(x, y) {
    $.get('/game/play/' + game.id + '/' + username + '/' + x + '/' + y + '/', function(result) {
      if (result == "True") {
        console.log('played');
        refresh(game.id);
      }
    });
  });

  refresh(game.id);
  setInterval(function() { refresh(game.id); }, REFRESH_RATE);
});
