let begin_all = {
    init: function(){
        console.log("Ready - All");
        all_bindings.init();
    }
}

let all_bindings = {
    init: function(){
        this.doubleClick();
        this.tabsClick();
    },
    doubleClick: function(){
        $("section.three table tr").on('dblclick', function(){
            let this_show = $(this).attr("class");
            all_deleteActions.init(this_show);
            //let this_class = $(this).find("ul").attr("class").split(" ");
            //console.log(this_class);
            //all_deleteActions.init(this_class);
        })
    },
    tabsClick: function(){
        $("section.three button").click(function(){
            let this_tab = $(this).attr("id");
            console.info(this_tab);
            tabSwitch.init(this_tab);
        });
    }
};

let tabSwitch = {
    init: function(this_tab){
        if (this.check_Active(this_tab)){
            console.log("Tab visible");
            this.hideAll();
        }
        else{
            console.log("Tab not visibile");
            this.hideAll();
            this.makeVisible(this_tab);
        }
    },
    check_Active(this_tab){
        return $(`section.three div#${this_tab}`).hasClass("active");
    },
    makeVisible(this_tab){
        $(`section.three div#${this_tab}`).show().addClass("active");        
    },
    hideAll:function(this_tab){
        $(`section.three div#OD`).hide().removeClass("active"); 
        $(`section.three div#Live`).hide().removeClass("active"); 
    }
}

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