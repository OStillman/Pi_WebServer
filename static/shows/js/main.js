let begin = {
    init: function () {
        $(document).ready(function () {
            console.info("Ready");
            setScroll.init();
            //Splitting out the files - Callers below
            begin_tags.init();
            begin_all.init();
        });
    }
};

let setScroll = {
    init: function(){
        var elmnt = document.getElementById("start");
        elmnt.scrollIntoView();
    }
};

let ajaxCalls = {
    ajaxCallData: function (method, url, data) {
        return $.ajax({
            method: method,
            url: url,
            data: JSON.stringify(data),
            dataType: 'json',
        });
    }
};