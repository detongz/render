$(document).ready(function(){
    $('#submiting').click(function(){
        $('aside').css('display','none');
        var flag=0;
        var id=$('#name').val();
        var pwd=$('#password').val();
        var email=$('#email').val();
        var cpwd=$('#cpassword').val();
        var description=$('#description').val();
        if(id==""){
            flag+=1;
            $('#name').after('<aside><p>要输入用户名哦( ◔ ڼ ◔ )</p></aside>');
            $('aside').css('width',$('#name').width()-15);
        }
        else if(id.length>10){
            flag+=1;
            $('#name').after('<aside><p>输入的用户名在十个字之内哦(^・ω・^)</p></aside>');
            $('aside').css('width',$('#name').width()-15);
        }
        if(pwd==""){
            flag+=1;
            $('#password').after('<aside><p>要输入密码哦(●\'◡\'●)ﾉ♥</p></aside>');
            $('aside').css('width',$('#password').width()-15);
        }
        else if(cpwd==""){
            flag+=1;
            $('#cpassword').after('<aside><p>要再输入一边上面一样的密码哦(๑￫ܫ￩)</p></aside>');
            $('aside').css('width',$('#cpassword').width()-15);
        }
        else if(pwd!=cpwd){
            flag+=1;
            $('#cpassword').after('<aside><p>两次输入的密码要第一模一样哦｡◕‿◕｡</p></aside>');
            $('aside').css('width',$('#cpassword').width()-15);
        }
        if(email==""){
            flag+=1;
            $('#email').after('<aside><p>这里要写上自己常用的邮箱哦(=・ω・=)</p></aside>');
            $('aside').css('width',$('#email').width()-15);
        }
        if(!flag){
            $.ajax({
                url:window.location.href,
                type:'post',
                dataType:'json',
                data:{
                    'id':id,
                    'pwd':pwd,
                    'email':email,
                    'description':description,
                },
                success:function(data){
                    if(data.result=='success'){
                        $('.form-signin').html('<div style="height:50px;color:#ADFF2F;"><p>(●\'◡\'●)ﾉ♥&nbsp;&nbsp;注册成功啦,请登录吧!&nbsp;&nbsp;(●\'◡\'●)ﾉ♥</p></div>');
                    }
                    else{
                        window.location.href='/error/'+data.result+'/login';
                    }
                }
            })
        }
    });
});