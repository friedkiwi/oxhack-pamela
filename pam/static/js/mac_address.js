/**
 * Created by yj on 06/10/15.
 */


var MAC_RETRIEVAL_URL = "http://172.16.30.144:8080/mac"

$(document).ready(function () {
    $.get(MAC_RETRIEVAL_URL, function(data) {
        $("#id_mac_address").val(data.replace(":", ""))
    })
})