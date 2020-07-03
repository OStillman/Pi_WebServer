let begin = {
    init: function () {
        $(document).ready(function () {
            console.info("Ready");
            bindings.init();
        });
    }
};

let submitChecks = {
    init: function(){
        if (this.checkShowTitle() && this.checkServiceSelection()){
            console.info("We can begin");
            $("div.2").hide();
            return true
        }
    },
    checkShowTitle(){
        if($("section.add .elements h2#title").hasClass("unedited")){
            return false;
        }
        else{
            return true
        }
    },
    checkServiceSelection: function(){
        if ($("section.add .elements div#service_grid img.chosen").length > 0){
            return true
        }
        else{
            return false;
        }
    },
};

let submit_to_search = {
    init: function(){
        if (submitChecks.init()){
            submit_to_search.proceed();
        }
    },
    proceed: function(){
        let service = $("section.add .elements div#service_grid img.chosen").attr("alt");
        let title = $("section.add .elements h2#title").text();
        console.info(`Service: ${service} / Title: ${title}`);
    },
};

let bindings = {
    init: function(){
        this.clickLiveTV();
        this.clickSubmit();
        this.showTitleBeginEntry();
        this.serviceSelection();
    },
    clickLiveTV:function(){
        $("section.add div.1 #live_tv").click(function(){
            $("div.1").hide();
            $("div.2").show();
        });
    },
    clickSubmit: function(){
        $("section.add div.2 button").click(function(){
            submit_to_search.init();
        });
    },
    showTitleBeginEntry: function(){
        $("section.add .elements h2#title").click(function(){
            if ($(this).hasClass("unedited")){
                $(this).text("").removeClass("unedited");
            }
        });
    },
    serviceSelection: function(){
        $("section.add .elements div#service_grid img").click(function(){
            $("section.add .elements div#service_grid img").removeClass("chosen").css("filter", "opacity(20%)");
            $(this).css("filter", "opacity(100%)").addClass("chosen")
        });
    },
};

let ajaxCalls = {
    ajaxCallData: function (method, url, data) {
        return $.ajax({
            method: method,
            url: url,
            data: JSON.stringify(data),
            dataType: 'json',
        });
    },
    ajaxCall: function (method, url) {
        return $.ajax({
            method: method,
            url: url,
        });
    }
};
