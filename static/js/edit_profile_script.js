$(document).ready(function(){
 var errorloginalert = $('#EditErrorLoginAlert');
 var errorconfirmpasswordalert = $('#EditErrorConfirmPasswordAlert')
 var usernameenable = true;
 var passwordenable = true;
 var editsubmit = $('#edit-submit');
 var imagelink = $('#EditImageLink');
 var avatar = $('#EditAvatar')
 errorloginalert.hide();
 errorconfirmpasswordalert.hide();

 $('#inputEditUserName').change( function (e) {
     e.preventDefault();
     ValidateUsername();
 });

 $('#EditConfirm-Password').change(function (e) {
    e.preventDefault()
    ConfirmPassword();
 });

  $('#EditCloseLoginAlert').on('click', function (e) {
      e.preventDefault();
      errorloginalert.hide();
  });

  $('#EditCloseConfirmPasswordAlert').on('click', function (e) {
      e.preventDefault();
      errorconfirmpasswordalert.hide();
  });

  $('#EditImageLink').change( function (e) {
     e.preventDefault();
     avatar.attr('src', imagelink.val());
  });

 function ValidateUsername() {
      var username = $('#inputEditUserName').val();
      var loginform = $('#EditLoginForm');
      var loginspan = $('#EditLoginSpan');
      $.ajax({
          url:'/ajax/edit_validate_username',
          data: {
            'username': username
          },
          datatype: 'json',
          success: function (data) {
             if(data.is_username)
              {
                //alert("A user with this username already exists.");
                loginspan.removeClass('glyphicon glyphicon-ok form-control-feedback');
                loginform.removeClass('has-success has-feedback');

                loginform.addClass('has-error has-feedback');
                loginspan.addClass('glyphicon glyphicon-remove form-control-feedback');
                errorloginalert.show();
                usernameenable = false;
                EnableRegisterButton();
              }
             else
              {
                loginspan.removeClass('glyphicon glyphicon-remove form-control-feedback');
                loginform.removeClass('has-error has-feedback');

                loginform.addClass('has-success has-feedback');
                loginspan.addClass('glyphicon glyphicon-ok form-control-feedback');
                errorloginalert.hide();
                usernameenable = true;
                EnableRegisterButton();
              }
          }
      });
}

function ConfirmPassword() {
   var password = $('#EditPassword').val();
     var confirmpassword = $('#EditConfirm-Password').val();
     var passwordform = $('#EditPasswordForm');
     var passwordspan = $('#EditPasswordSpan');
     var passwordconfirmform = $('#EditConfirmPasswordForm');
     var passwordconfirmspan = $('#EditPasswordConfirmSpan');
     if (password.localeCompare(confirmpassword) == 0)
      {
        passwordform.removeClass('has-error has-feedback');
        passwordspan.removeClass('glyphicon glyphicon-remove form-control-feedback');
        passwordform.addClass('has-success has-feedback');
        passwordspan.addClass('glyphicon glyphicon-ok form-control-feedback');

        passwordconfirmform.removeClass('has-error has-feedback');
        passwordconfirmspan.removeClass('glyphicon glyphicon-remove form-control-feedback');
        passwordconfirmform.addClass('has-success has-feedback');
        passwordconfirmspan.addClass('glyphicon glyphicon-ok form-control-feedback');
        errorconfirmpasswordalert.hide();
        passwordenable = true;
        EnableRegisterButton();
      }
      else
      {
        passwordform.removeClass('has-success has-feedback');
        passwordspan.removeClass('glyphicon glyphicon-ok form-control-feedback');
        passwordform.addClass('has-error has-feedback');
        passwordspan.addClass('glyphicon glyphicon-remove form-control-feedback');

        passwordconfirmform.removeClass('has-success has-feedback');
        passwordconfirmspan.removeClass('glyphicon glyphicon-ok form-control-feedback');
        passwordconfirmform.addClass('has-error has-feedback');
        passwordconfirmspan.addClass('glyphicon glyphicon-remove form-control-feedback');
        errorconfirmpasswordalert.show();
        passwordenable = false;
        EnableRegisterButton();
      }
}

function EnableRegisterButton() {
    if (usernameenable && passwordenable)
     {
       editsubmit.prop('disabled', false);
     }
    else
     {
       editsubmit.prop('disabled', true);
     }
}
});