// 모달 창 끄기 + 다시 보지 않음 쿠키 설정
var modal = document.getElementById('myModal');
var span = document.getElementsByClassName("close")[0];
var expiredays = 7;

$( document ).ready(function() {
    cookiedata = document.cookie;
    if ( cookiedata.indexOf("ncookie=done") < 0 ){
        modal.style.display = "block";    //  팝업창 아이디
    } else {
        modal.style.display = "none";    // 팝업창 아이디
    }
});

function setCookie(name, value) {
    var todayDate = new Date();
    todayDate.setDate( todayDate.getDate() + expiredays);
    document.cookie = name + "=" + escape( value ) + "; path=/; expires=" + todayDate.toGMTString() + ";"
}

var Spanclick_set_cookie = function (x, y) {
    x.onclick = function () {
        y.style.display = "none";
        var chk = document.getElementById('unlook');
        // 체크하고 누르면 쿠키 생성
        if (chk.checked) {
            setCookie("ncookie", "done");
        }
    }
}

// 검사대상표 모달
var target_btn = document.getElementById("target_btn");
var target_modal = document.getElementById('target_modal');
var target_close = document.getElementById("target_close");
Btnclick(target_btn, target_modal);
Spanclick(target_close, target_modal);
Spanclick_set_cookie(span, modal);
window.onclick = function (event) {
    if (event.target == target_modal) {
        target_modal.style.display = "none";
    }
}
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
