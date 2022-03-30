function draw(){
    var canvas = document.getElementById('canvas');
    if (canvas.getContext){
        var ctx = canvas.getContext('2d');
        // 绘制第一个正方形
        //ctx.fillStyle = 'rgb(200,0,0)'
        //ctx.fillRect(0,0,50,50)
        // 绘制第二个
        //ctx.fillStyle = 'rgb(0, 0, 200, 0.5)'
        //ctx.fillRect(25,25,50,50)

        //ctx.beginPath()
        //ctx.arc(175, 175, 50, 0, Math.PI * 2, true)
        //ctx.stroke()

        // ctx.font = '20px Microsoft YaHei';          //字体、大小
        // ctx.fillStyle = '#000000';                  //字体颜色
        // ctx.fillText('canvas 绘制文字', 100, 50);
        // ctx.font = '20px Microsoft YaHei';          //字体、大小
        // ctx.fillStyle = '#FF0000';                  //字体颜色
        //
        // let textw = ctx.measureText('canvas 绘制文字').width
        // ctx.fillText('canvas 绘制文字', 100+textw, 50);
        // let texth = ctx.measureText('canvas 绘制文字').height
        // ctx.clearRect(100,33,textw,20)

        // setTimeout(a.add_barrageList('隔10秒的弹幕能发出来吗',10000))

    }
}

class Barrage{
    constructor(canvas) {
        this.canvas = document.getElementById(canvas);
        let rect = this.canvas.getBoundingClientRect()
        this.w = rect.right - rect.left;
        this.h = rect.bottom - rect.top;
        this.ctx = this.canvas.getContext('2d');
        this.ctx.font = '20px Microsoft YaHei';
        }

    add_barrage(danmu){
        // 自动添加弹幕
        let current_top = this.get_top()
        this.barrage={value:danmu,w:this.w,h:current_top}
        console.log('弹幕初始化成功!'+this.barrage.value+this.barrage.w+this.barrage.h)
    }

    move(){
        // var max_leng = 0
        // if(this.barrage.w+this.ctx.measureText(this.barrage.value).width+20>this.w){
        //     console.log(1)
        // }

        console.log('清除宽度w:'+this.ctx.measureText(this.barrage.value).width)
        console.log('清除坐标x:'+this.barrage.w+2)
        console.log('清除坐标y:'+this.barrage.h)

        this.ctx.clearRect(this.barrage.w+2,this.barrage.h-40,this.ctx.measureText(this.barrage.value.width),50)
        this.draw_text(this.barrage)
        this.barrage.w -= this.speed()


        // console.log(max_floor,barrage_num)
        if(this.barrage.w + this.ctx.measureText(this.barrage.value).width>=0){
                requestAnimationFrame(this.move.bind(this));
        }
    }

    draw_text(content){
        // 用户名字和他发送弹幕的颜色分开
        const user_danmu=content.value.split(':')
        // 用户名宽度
        const user_width = this.ctx.measureText(user_danmu[0]).width
        // 弹幕宽度
        // const danmu_width = this.ctx.measureText(user_danmu[1]).width
        // 冒号宽度
        // const maohao_width = this.ctx.measureText(':').width
        // 获取颜色配置
        const color_style = this.get_color()
        //先设置用户名颜色
        this.ctx.fillStyle = color_style.user_color
        // 绘制用户名
        console.log('绘制用户:'+user_danmu[0]+'坐标x:'+content.w+'坐标y:'+content.h)
        this.ctx.fillText(user_danmu[0],content.w,content.h)
        // 设置弹幕颜色
        this.ctx.fillStyle = color_style.danmu_color
        //绘制弹幕
        this.ctx.fillText(':'+user_danmu[1],content.w+user_width,content.h)


    }

    speed(){
        return 1
    }

    get_color(){
        // 用户名颜色
        return {
            'user_color':'#FFD700',
            'danmu_color':'#000000'
        }
    }

    get_top(){
        return Math.floor(Math.random() * 5+1)*50
    }
}


function danmu_move(name) {
    const a = new Barrage('canvas');
    a.add_barrage(name)
    a.move()
}

function send() {
    // 获取发送的弹幕值
    var danmu_word = $('#danmu_word').val()
    $('#danmu_word').val('')
    // 获取发送弹幕时间
    // console.log(danmu_time)
    // ajax 请求将弹幕数据上传数据库
    $.ajax({
            url:'/danmu_send',
            type:'get',
            datatype:'json',
            data:{
                'danmu_value':danmu_word,
                'danmu_time':'danmu_time',
            },
            headers:{
                'X-CSRFtoken':$.cookie('csrftoken')
            },
            success:function(data){
                if(data.res_success==true){
                    console.log('发送弹幕成功')
                }
                else{
                    console.log('弹幕发送失败，请刷新页面')
                }
            },
            error:function () {
                console.log('有错误！！')
            }
        })
}

function get_danmu() {
    const myDate = new Date;
    const year = myDate.getFullYear(); //获取当前年
    const mon = myDate.getMonth() + 1; //获取当前月
    const date = myDate.getDate(); //获取当前日
    const h = myDate.getHours();//获取当前小时数(0-23)
    const m = myDate.getMinutes();//获取当前分钟数(0-59)
    const s = myDate.getSeconds();//获取当前秒
    const now_time = year + "-" + mon + "-" + date + " " + h + ":" + m + ":" + s;
    // console.log('开始获取'+now_time+'的弹幕')
    $.ajax({
         url:'/get_danmu',
        type:'get',
        datatype:'json',
        data:{
            'get_time':now_time,
        },
        success:function (data) {
             if(data.message==false){
                 location.href('/login')
             }
             else{
                 for(let j=0;j<data.content.length;j++){
                     // console.log('弹幕第'+j+'条'+data.content[j]['danmu_name'])
                     danmu_move(data.content[j]['user_id__user_name']+':'+data.content[j]['danmu_name'])
                 }
             }
        }
    })
}

setInterval(get_danmu,1000)





//还有两个问题：第一个：调整窗体后canvas的尺寸要随之调整，弹幕出现的位置也要调整
//            第二个：怎么直接通过页面上的发送来移动弹幕  直接点击发送后新增到字典即可
//新问题：一批弹幕运行完了，move函数也停了，怎么在启动呢   解决：把每一条弹幕作为一个对象在canvas上跑


// {0:{h:50,value:"弹幕",w:}}