let begin_all = {
    init: function(){
        console.log("Ready - All");
        all_bindings.init();
    }
}

let all_bindings = {
    init: function(){
        this.doubleClick();
    },
    doubleClick: function(){
        $("section.three table tr").on('dblclick', function(){
            let this_show = $(this).attr("class");
            all_deleteActions.init(this_show);
            //let this_class = $(this).find("ul").attr("class").split(" ");
            //console.log(this_class);
            //all_deleteActions.init(this_class);
        })
    }
};

let all_deleteActions = {
    init: function(this_show){
        if (confirm("Are you sure you want to delete this?")){
            all_deleteActions.requestRemove(this_show);
        }
    },
    requestRemove: function(this_show){
        data = {"element": this_show};
        $.when(ajaxCalls.ajaxCallData("DELETE", "/shows", data)).then(function(result){
            console.info("Success");
            console.log(result);
            window.location.replace("../shows")
            //$("section#success").show();
        }, function(){
            console.info("Failed");
            //$("section#error").show();
        })
    }
};