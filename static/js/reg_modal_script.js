$(document).ready(function(){
  var errorloginalert = $('#ErrorLoginAlert');
  var erroremailalert = $('#ErrorEmailAlert');
  var errorconfirmpasswordalert = $('#ErrorConfirmPasswordAlert');
  var registersubmit = $('#register-submit');
  registersubmit.prop('disabled', true);
  var usernameenable;
  var passwordenable;
  var emailenable;
  errorloginalert.hide();
  erroremailalert.hide();
  errorconfirmpasswordalert.hide();

  $('#RegUserName').change(function (e) {
      e.preventDefault();
      ValidateUsername();
  });

  $('#CloseLoginAlert').on('click', function (e) {
      e.preventDefault();
      errorloginalert.hide();
  });

  $('#Email').change(function (e) {
    e.preventDefault();
    ValidateEmail();
  });

 $('#CloseEmailAlert').on('click', function (e) {
      e.preventDefault();
      erroremailalert.hide();
  });

 $('#Confirm-Password').change(function (e) {
     e.preventDefault();
     ConfirmPassword();
     });

 $('#CloseConfirmPasswordAlert').on('click', function (e) {
      e.preventDefault();
      errorconfirmpasswordalert.hide();
  });


function ValidateUsername() {
      var username = $('#RegUserName').val();
      var loginform = $('#LoginForm');
      var loginspan = $('#LoginSpan');
      $.ajax({
          url:'/ajax/validate_username',
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

function ValidateEmail() {
    var email = $('#Email').val();
    var emailform = $('#EmailForm');
    var emailspan = $('#EmailSpan');
    $.ajax({
          url:'/ajax/validate_email',
          data: {
            'email': email
          },
          datatype: 'json',
          success: function (data) {
             if(data.is_email)
              {
                emailspan.removeClass('glyphicon glyphicon-ok form-control-feedback');
                emailform.removeClass('has-success has-feedback');

                emailform.addClass('has-error has-feedback');
                emailspan.addClass('glyphicon glyphicon-remove form-control-feedback');
                erroremailalert.show();
                emailenable = false;
                EnableRegisterButton();
              }
            else
             {
                emailspan.removeClass('glyphicon glyphicon-remove form-control-feedback');
                emailform.removeClass('has-error has-feedback');

                emailform.addClass('has-success has-feedback');
                emailspan.addClass('glyphicon glyphicon-ok form-control-feedback');
                erroremailalert.hide();
                emailenable = true;
                EnableRegisterButton();
             }
          }
      });

}


function ConfirmPassword() {
   var password = $('#RegPassword').val();
     var confirmpassword = $('#Confirm-Password').val();
     var passwordform = $('#PasswordForm');
     var passwordspan = $('#PasswordSpan');
     var passwordconfirmform = $('#ConfirmPasswordForm');
     var passwordconfirmspan = $('#PasswordConfirmSpan');
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
    if (usernameenable && emailenable && passwordenable)
     {
       registersubmit.prop('disabled', false);
     }
    else
     {
       registersubmit.prop('disabled', true);
     }
}
    
});
