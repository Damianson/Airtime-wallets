(function ($) {
  $(function () {

    $('.sidenav').sidenav();

  }); // end of document ready
})(jQuery); // end of jQuery name space

$(document).ready(function () {
  $('select').formSelect();
});

$('#submit').on('click', function (e) {
  e.preventDefault();
  $.ajax({
    url: "https://api.wallets.africa/bills/airtime/purchase",
    type: 'POST',
    data: {
      Code: $('#airtime').val(),
      Amount: $('#amount').val(),
      PhoneNumber: $('#number').val(),
      SecretKey: $('#secretKey').val()
    },
    contentType: 'application/json',
    headers: {
      "Authorization": "Bearer " + $('#publicKey').val()
    },
    success: function (response) {
      console.log(response);
      $('.form-control').val(response);
    }
  });
  return false;
});