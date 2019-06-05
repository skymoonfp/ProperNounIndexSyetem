function CheckPost () {
      if (form_reg.password_2.value != form_reg.password_3.value) {
          var element=document.getElementById("error");
          element.innerHTML="密码不一致！"
          form_reg.password_2.focus();
          return false;
      }

     return true;
   }