$(document).ready(function() {
    $('#like_btn').click(function() {
        var categoryIdVar;
        categoryIdVar = $(this).attr('data-categoryid');

        $.get('/concertconnect_app/like_category/',
            {'category_id': categoryIdVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
    });

    $('#search-input').keyup(function() {
        var query;
        query = $(this).val();

        $.get('/concertconnect_app/suggest',
              {'suggestion': query},
              function(data) {
                  $('#categories-listing').html(data);
              })
    });

    $('.concertconnect_app-page-add').click(function() {
        var categoryid = $(this).attr('data-categoryid');
        var title = $(this).attr('data-title');
        var url = $(this).attr('data-url');
        var clickedButton = $(this);

        $.get('/concertconnect_app/search_add_page/',
              {'category_id': categoryid, 'title': title, 'url': url},
              function(data) {
                  $('#page-listing').html(data);
                  clickedButton.hide();
              })
    });
});