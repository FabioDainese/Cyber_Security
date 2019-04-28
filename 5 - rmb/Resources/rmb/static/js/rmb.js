$(function() {
  $('#show').bind('click', function() {
    $('#releases').empty();
    var $orderby = $('#orderby').val();
    var $page = $('#page').val();
    $.ajax({
      url: '/_get_releases/' + $orderby + '/' + $page,
      dataType: 'json',
      success: function(data, textStatus, jqXHR) {
        var $thead = $('<thead>')
        $thead.append($('<tr>').append(
          $('<th>').text('label'),
          $('<th>').text('cat'),
          $('<th>').text('artist'),
          $('<th>').text('title'),
          $('<th>').text('format'),
          $('<th>').text('year')
        ));
        $thead.appendTo('#releases');
        $('<tbody>').appendTo('#releases');
        $.each(data.records, function(i, item) {
          $tr = $('<tr>').append(
            $('<td>').text(item.label),
            $('<td>').text(item.cat),
            $('<td>').text(item.artist),
            $('<td>').text(item.title),
            $('<td>').text(item.format),
            $('<td>').text(item.year)
          ).appendTo('#releases');
        });
      }
    });
    return false;
  });

  $('#show-djset').bind('click', function() {
    $('#djset-content').empty();
    var $djset = $('#djset').val();
    $.ajax({
      url: '/_get_djset/' + $djset,
      dataType: 'json',
      success: function(data, textStatus, jqXHR) {
        $('<h3>').text(data.title).appendTo('#djset-content');
        $('<p>').text(data.size + ' | ' + data.year).appendTo('#djset-content');
        $('<pre>').text(data.tracklist).appendTo('#djset-content');
      }
    });
    return false;
  });

});