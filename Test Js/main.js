$("input[name='address']").submit(function () {
var fname = $.trim($('#form-reg-fullname').val());
$("input[name='return']").val("http://localhost:9000/app/fname");
});
