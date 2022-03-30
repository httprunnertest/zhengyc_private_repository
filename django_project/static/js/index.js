 $(function () {
    $('#logout').click(
        function () {
            $.ajax({
                url:'/logout',
                type:'post',
                datatype:'json',
                headers:{
                    'X-CSRFtoken':$.cookie('csrftoken')
                },
                success:function (data) {
                if(data.session_delete==true){
                    location.href='/login'
                }},
                error:function () {
                    console.log('有错误！！')
                }
            })
        }
    )

    $('[id=delete]').click(
        function () {
            let current_delete_id = this.getAttribute('delete_index')
            $('#delete_confirm').css('display','block')
            test(current_delete_id)
        }
    )

    function test(id) {
        $('#cancel').click(function () {
            $('#delete_confirm').css('display', 'none')
        })
        $('#confirm').click(function () {
            $('#delete_confirm').css('display', 'none')
            $.ajax({
                url:'/delete_date',
                type:'post',
                datatype:'json',
                data:{
                    'delete_id': id
                },
                headers:{
                    'X-CSRFtoken':$.cookie('csrftoken')
                },
                success:function (data) {
                if(data.isdelete==true){
                    location.reload()
                }},
                error:function () {
                    console.log('有错误！！')
                }
            })
        })
    }

    // 根据身份来显示不同画面



 })
