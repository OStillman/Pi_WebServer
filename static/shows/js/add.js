let begin = {
    init: function () {
        $(document).ready(function () {
            console.info("Ready");
            bindings.init();
        });
    }
};

let bindings = {
    init: function(){
        this.clickLiveTV();
    },
    clickLiveTV:function(){
        $("section.add div.1 #live_tv").click(function(){
            $("div.1").hide();
            $("div.2").show();
        });
    }
};
