 $(function () {
     function warning() {
         // $('#password').css()
         $('input').removeClass('change')
         $('input').css('border', '#ccc 1px solid')
         $('.date_wrong').css('display', 'inline-block')
     }

     function date_is_null() {
         // $("input:not([type='button'])").css('border', 'red 1px solid')
         $('input').addClass('change')
         if($('#username').val()==''){
             $('#username').attr('placeholder','账号必填')
             $('#username').addClass('change')
             $("#username").css('border', 'red 1px solid')
         }
         else{
             $('#username').removeClass('change')
             $("#username").css('border', '#ccc 1px solid')
         }
         if($('#password').val()==''){
             $('#password').attr('placeholder','密码必填')
             $('#password').addClass('change')
             $("#password").css('border', 'red 1px solid')
         }
         else{
             $('#password').removeClass('change')
             $("#password").css('border', '#ccc 1px solid')
         }
     }

     $('#submit').click(
            function () {
                var username = $('#username').val()
                var password = $('#password').val()
                var remember = $('#remember').is(':checked')
                $.ajax({
                    url:'/login_check',
                    type:'post',
                    datatype:'json',
                    data:{
                        'username':username,
                        'password':password,
                        'remember':remember
                    },
                    headers:{
                        'X-CSRFtoken':$.cookie('csrftoken')
                    },
                    success:function (data) {
                        if(data.res_success==true){
                            $('.date_wrong').css('display', 'none')
                            location.href='/index'
                        }
                        else if(data.res_success==false){
                            warning()
                        }
                        else{
                            date_is_null()
                        }
                    },
                    error:function () {
                        console.log('有错误！！')
                    }
                })
            }
        )

        $('#register').click(function () {
        location.href='/register'
        })
    })
