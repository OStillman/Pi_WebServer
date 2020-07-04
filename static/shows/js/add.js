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
        this.saveService(service);
        data = {"service": service, "title": title, "offset": 0}
        this.request(data)
    },
    saveService: function(service){
        sessionStorage.setItem("service", service)
    },
    request: function(data){
        $.when(ajaxCalls.ajaxCallData("POST", "/shows/live/search", data))
            .then(function(result){
                console.info("Success");
                console.log(result);
                if (result[0][0] == "Error, show not found"){
                    data.offset = data.offset + 1;
                    submit_to_search.request(data);
                }
                else{
                    submit_to_search.displayResults(result)
                }
            }, function(){
                console.info("Failed");
            })
    },
    displayResults: function(responses){
        responses.forEach(response => {
            console.info(response);
            this.output(response);  
        });
        $("div.3").show();  
    },
    output: function(show){
        $("div.live_tv.3 table tbody").append(`<tr>`+
                    `<td>${show[0]}</td>`+
                    `<td><input type="radio" name="show" value=${show[1]}></td>` +
                "</tr>");
    }
};

let addShow = {
    init: function(evtid){
        let service = sessionStorage.getItem("service");
        console.info(`Service = ${service} with evtid of ${evtid}`);
        this.send(service, evtid);
    },
    send: function(service, evtid){
        let data = {"service": service, "evtid": evtid};
        $.when(ajaxCalls.ajaxCallData("POST", "/shows/live/add", data))
            .then(function(result){
                console.info("Success");
                console.log(result);
            }, function(){
                console.info("Failed");
            });
    }
};

let bindings = {
    init: function(){
        this.clickLiveTV();
        this.clickSubmit();
        this.showTitleBeginEntry();
        this.serviceSelection();
        this.confirmLiveShow();
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
    confirmLiveShow: function(){
        $("div.live_tv.3 button").click(function(){
            let evtid = $("div.live_tv.3 table tbody input:checked").val();
            addShow.init(evtid);
        });        
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
    },
    ajaxCall: function (method, url) {
        return $.ajax({
            method: method,
            url: url,
        });
    }
};
