$(document).on('click', '.like-btn', function(e) {
  e.preventDefault();
  var post_id = $(this).data('id');
  var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
  var like_btn = $(this);

  $.ajax({
    url: '/like/',
    data: { 'post_id': post_id },
    type: 'POST',
    beforeSend: function(xhr, settings) {
      xhr.setRequestHeader('X-CSRFToken', csrf_token);
    },
    success: function(response) {
      like_btn.next().text(response.likes);

      // Thêm hoặc xóa class 'liked' tùy thuộc vào trạng thái của nút thích
      if (like_btn.hasClass('liked')) {
        like_btn.removeClass('liked');
      } else {
        like_btn.addClass('liked');
      }
    },
    error: function(xhr, status, error) {
      console.log(error);
    }
  });
});
