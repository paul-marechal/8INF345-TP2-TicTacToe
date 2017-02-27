function gamelist(parentSelector) {
  var parent = $(parentSelector);

  $.getJSON('/game/list/', function(data) {
    //console.log(data);

    // For each game in data, check if it does not already exists
    $.each(data, function(id, v) {
      var match = parent.children('[data-game-id="' + id + '"]');
      if (match.length == 0) {
        var game = $('<div class="game"/>');
        game.attr('data-game-id', id);
        game.html(v);

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
