/**
 * Created by xin on 2018/11/20.
 */

$(function () {
    // 买票
        $("#buybtn").click(function () {
            // 判断是否登录
            if ($("#buybtn").attr('userid')) {
                $('.buy-seats').css('display', 'block');
                $('body').css('background', '#C1C1C1');
            }else{
                alert('请先登录');
                window.location.href = '/movies/login/';
            }
        });


    // 取消按钮
    $("#cancel").click(function () {
        // 初始化
        arr = [];
        $('.selectable').css("background-image", "url('/static/img/seat/227714.png')");
        $('#choose_seats').text('');
        $('.buy-seats').css('display', 'none');
        $('body').css('background', 'white');
        $('#QRcode').css('display', 'none');
        $('#price').text(0);
        $('.buy-seats').css('background', 'white');
        window.clearInterval(t1);
    });

    // 选座位
    var arr = [];
    $('.selectable').click(function () {
        // 最多只能选4张票
        if (arr.length < 4) {
            arr.push($(this));
            console.log(arr);
            console.log(arr.length);
            $(this).css("background-image", "url('/static/img/seat/227774.png')");
            // 已经选了的座位
            var arr1 = [];
            for (x in arr) {
                var seat_row = arr[x].attr('data-row-id');
                var seat_col = arr[x].attr('data-column-id');
                arr1.push(seat_row + '排' + seat_col + '座');
            }
            $('#choose_seats').text(arr1);
            // 总票价
            $('#price').text(arr.length * 26);
        } else {
            alert('一次性最多可买4张票！');
        }
    });

    // 付款按钮
    $("#paybtn").click(function () {
        if ($('#price').text() > 0) {
            $('#QRcode').css('display', 'block');
            $('.buy-seats').css('background', '#38f');
            $.getJSON("/movies/QRcode/", {"paystatus": 0}, function (data) {
                t1 = window.setInterval(refreshCount, 2000);
                function refreshCount() {
                    console.log("ready");
                    $.getJSON("/movies/QRcode/", {"paystatus": 1}, function (data) {
                    if (data["code"] == 200) {
                        alert('支付成功！');
                        //去掉定时器的方法
                        window.clearInterval(t1);
                        var userid = $("#paybtn").attr('userid');
                        var movieid = $("#paybtn").attr('movieid');
                        var price = $('#price').text();
                        var quantity = arr.length;
                        var seats = $('#choose_seats').text();
                        $.get("/movies/buy/",{'userid':userid,'movieid':movieid,'price':price,'quantity':quantity,'seats':seats},function () {
                            window.location.href = '/movies/userInfo/';
                        })
                    } else if (data["code"] == 901) {
                    }
                })
                }
            })
        } else {
            alert('你还没有选座，请先选座。')
        }
    });
});










