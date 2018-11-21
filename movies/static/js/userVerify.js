/**
 * Created by xin on 2018/11/19.
 */
var verify1 = false;
var verify2 = false;
var verify3 = false;
$(function () {
    // 验证用户名
    $username = $('#username');
    $password = $('#password');
    $pwd = $('#cpassword');
    $username.change(function () {
        $.getJSON("/movies/checkUser", {"username": $username.val()}, function (data) {
            if (data["code"] == 200) {
                if ($username.val().length < 6 || $username.val().length > 15) {
                    $('#s1').text('长度不能小于6或大于15').css('color', 'red');
                } else {
                    if (/^[a-zA-Z]/.test($username.val())) {
                        if (/^[A-Za-z0-9]+$/.test($username.val())) {
                            $('#s1').text('用户名可用').css('color', 'green');
                            verify1 = true;
                        } else {
                            $('#s1').text('只能包含数字，字母').css('color', 'red');
                        }
                    } else {
                        $('#s1').text('必须以字母开头').css('color', 'red');
                    }
                }
            }
            else if (data["code"] == 901) {
                $('#s1').text("用户名已经存在!").css("color", "red");
            }
        })
    });
    // 验证密码
    $password.change(function () {
        if ($password.val().length < 6 || $password.val().length > 15) {
            $('#s2').text('长度不能小于6或大于15').css('color', 'red');
        } else {
            if (/^[A-Za-z0-9]+$/.test($password.val())) {
                $('#s2').text('密码可用').css('color', 'green');
                verify2 = true;
            } else {
                $('#s2').text('只能包含数字，字母').css('color', 'red');
            }
        }
    });
    // 验证密码
    $pwd.change(function () {
        if ($password.val() != $pwd.val()) {
            $('#s3').text('两次输入的密码不同').css('color', 'red');
        } else {
            $('#s3').text('确认密码成功').css('color', 'green');
            verify3 = true;
        }
    });
});


function formsubmit() {
    if (!verify1) { //密码不合法
        // alert("用户名不合法,不能提交");
        return false
    }
    if (!verify2) { //密码不合法
        alert("密码不合法,不能提交");
        return false
    }
    if (!verify3) {
        alert("密码不合法,不能提交");
        return false
    }
    return true;
}






