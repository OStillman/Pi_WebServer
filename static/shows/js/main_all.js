let begin_all = {
    init: function(){
        console.log("Ready - All");
        all_bindings.init();
    }
}

let all_bindings = {
    init: function(){
        this.doubleClickLive();
        this.doubleClickOD();
        this.tabsClick();
    },
    doubleClickOD: function(){
        $("section.three div#OD table tr").on('dblclick', function(){
            let this_show = $(this).attr("class");
            all_deleteActions.init(this_show, false);
            //let this_class = $(this).find("ul").attr("class").split(" ");
            //console.log(this_class);
            //all_deleteActions.init(this_class);
        })
    },
    doubleClickLive: function(){
        $("section.three div#Live table tr").on('dblclick', function(){
            let this_show = $(this).attr("class");
            all_deleteActions.init(this_show, true);
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
    init: function(this_show, isLive){
        if (confirm("Are you sure you want to delete this?")){
                all_deleteActions.requestRemove(this_show, isLive);
        }
    },
    requestRemove: function(this_show, isLive){
        data = {"element": this_show};
        if (isLive){
            url = "/shows/live";
        }
        else{
            url = "/shows/od";
        }
        $.when(ajaxCalls.ajaxCallData("DELETE", url, data)).then(function(result){
            console.info("Success");
            console.log(result);
            window.location.replace("../shows")
            //$("section#success").show();
        }, function(){
            console.info("Failed");
            //$("section#error").show();
        })
    },
};