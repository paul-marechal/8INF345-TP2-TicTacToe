function isNumeric(string) {
  return !isNaN(string);
}

// List available games
function gamelist(parentSelector, callback) {
  var parent = $(parentSelector);

  $.getJSON('/game/list/', function(data) {
    //console.log(data);

    // For each game in data, check if it does not already exists
    $.each(data, function(id, opponent) {
      var match = parent.children('[data-game-id="' + id + '"]');
      if (match.length == 0) {
        var game = $('<div class="game" />');
        game.attr('data-game-id', id);

        var text = $('<span>');
        text.text(opponent);

        var joinButton = $('<button class="joingame" />')
        joinButton.text('Join');
        joinButton.click(function(e) {
          callback({id: id, opponent: opponent});
        });

        game.append(joinButton);
        game.append(text);
        parent.append(game);
      }
    });

    // For each game listed, remove the ones that are not available
    parent.children('.game').each(function(k, game) {
      if (!($(game).attr('data-game-id') in data)) {
        game.remove();
      }
    });
  })
}

// Creates new game
function creategame(username, callback) {
  $.get('/game/create/' + username + '/', function(gameid) {
    if (isNumeric(gameid)) {
      callback(gameid);
    }
  });
}

function gameexists(id, callbacks) {
  $.get('/game/exists/' + id + '/', function(bool) {
    if (bool == "True" && callbacks.onTrue)
      callbacks.onTrue();
    else if (bool == "False" && callbacks.onFalse)
      callbacks.onFalse();
  });
}

// Ask to join a game
function joingame(id, username) {
  gameexists(id, {
    onTrue: function() {
      $.get('/game/join/' + id + '/' + username + '/', function(bool) {
        if (bool == "True") {
          window.location.replace('/play/');
        } else {
          alert('Could not join the game...');
        }
      });
    },
    onFalse: function() {
      alert('This game does not exists anymore...')
    }
  });
}

// creates some grid under root tree
function creategrid(parentSelector, callback) {
  var root = $(parentSelector);
  for(var i = 0; i < 3; i++) {
    var row = $('<tr class="gridrow" />');
    for(var j = 0; j < 3; j++) {
      var cell = $('<td class="gridcell" />');
      cell.attr('data-x', i);
      cell.attr('data-y', j);

      var callhell = function(x, y) {
        return function() {
          callback(x, y);
        }
      };

      cell.click(callhell(i, j));

      row.append(cell);
    } root.append(row);
  } // END
}

function isEmpty(object) {
  return Object.keys(object).length === 0 && object.constructor === Object;
}
