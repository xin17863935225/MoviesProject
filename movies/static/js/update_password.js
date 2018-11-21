/**
 * Created by xin on 2018/11/19.
 */
var verify1 = false;
var verify2 = false;
var verify3 = false;
$(function () {
    // 验证用户名
    $oldpwd = $('#oldpwd');
    $newpwd = $('#password');
    $cpassword = $('#cpassword');
    $oldpwd.change(function () {
        $.getJSON("/movies/checkPassword", {"oldpwd": $oldpwd.val()}, function (data) {
            if (data["code"] == 200) {
                $('#s1').text('密码正确').css('color', 'green');
                verify1 = true;
            }
            else if (data["code"] == 901) {
                $('#s1').text("密码错误").css("color", "red");
            }
        })
    });
    // 验证密码
    $newpwd.change(function () {
        if ($newpwd.val().length < 6 || $newpwd.val().length > 15) {
            $('#s2').text('长度不能小于6或大于15').css('color', 'red');
        } else {
            if (/^[A-Za-z0-9]+$/.test($newpwd.val())) {
                $('#s2').text('密码可用').css('color', 'green');
                verify2 = true;
            } else {
                $('#s2').text('只能包含数字，字母').css('color', 'red');
            }
        }
    });
    // 验证密码
    $cpassword.change(function () {
        if ($cpassword.val() != $newpwd.val()) {
            $('#s3').text('两次输入的密码不同').css('color', 'red');
        } else {
            $('#s3').text('确认密码成功').css('color', 'green');
            verify3 = true;
        }
    });
});


function formsubmit() {
    if (!verify1) { //密码不合法
        alert("密码不正确,请重新输入");
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






