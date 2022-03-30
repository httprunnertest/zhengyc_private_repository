$(function () {
    $('#ten_touch').click(
     function () {
         var money = $('.money_num').text()
         if(money>=1000){
             $.ajax({
                 url:'/touch_prize',
                 type:'post',
                 datatype:'json',
                 data:{
                     count:10
                 },
                 headers:{
                     'X-CSRFtoken':$.cookie('csrftoken')
                 },
                 success:function (data) {
                    if(data.success==true){
                        var i = 1
                        $('.money_num').text(data.user_money)
                        var prize = data.prize
                        $('.prize_').text(data.prize[1])
                        img_url="/static/image/"+data.prize[1]+'.png'
                        $('.prize_picture').attr('src',img_url)
                        $('html').click(
                            function () {
                                if(i<10){
                                     i++
                                     $('.prize_').text(data.prize[i])
                                     img_url="/static/image/"+data.prize[i]+'.png'
                                     $('.prize_picture').attr('src',img_url)
                                }
                            }
                        )
                    }
                },
                 error:function () {
                    console.log('有错误！！')
                }
            })
         }
         else{
             alert('点券不够')
         }

        }
    )
    $('#one_touch').click(
     function () {
         var money = $('.money_num').text()
         if(money>=100){
             $.ajax({
                 url:'/touch_prize',
                 type:'post',
                 datatype:'json',
                 data:{
                     count:1
                 },
                 headers:{
                    'X-CSRFtoken':$.cookie('csrftoken')
                 },
                 success:function (data) {
                    if(data.success==true){
                        $('.money_num').text(data.user_money)
                        $('.prize_').text(data.prize[1])
                        img_url="/static/image/"+data.prize[1]+'.png'
                        $('.prize_picture').attr('src',img_url)
                        // $('.tip_').css('display', 'block')
                    }
                    // else if(data.success==false){
                    //     warning()
                    // }
                    // else{
                    //     date_is_null()
                    // }
                },
                 error:function () {
                    console.log('有错误！！')
                }
            })
         }
         else{
             alert('点券不够')
         }

        }
    )
    }
)