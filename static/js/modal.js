// 모달함수
var Btnclick = function (x, y) {
    x.onclick = function () {
        y.style.display = "block";
    }

}
var Spanclick = function (x, y) {
    x.onclick = function () {
        y.style.display = "none";
    }
}

function logout() {
    var back_head = confirm('정말 로그아웃 하시겠습니까?');
    if (back_head) {
        location.href = '/accounts/logout/';
    }
}