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
    initOD: function(){
        console.info("Checking");
        if (this.checkODShowTitle() && this.checkODServiceSelection() && this.checkTagSelection()){
            console.info("We can begin");
            $("div.2").hide();
            return true
        }
    },
    checkODShowTitle(){
        if($("section.add .elements.od_tv h2#title").hasClass("unedited")){
            return false;
        }
        else{
            return true
        }
    },
    checkShowTitle(){
        if($("section.add .elements.live_tv h2#title").hasClass("unedited")){
            return false;
        }
        else{
            return true
        }
    },
    checkODServiceSelection: function(){
        if ($("section.add .elements.od_tv div#service_grid img.chosen").length > 0){
            return true
        }
        else{
            return false;
        }
    },
    checkServiceSelection: function(){
        if ($("section.add .elements.live_tv div#service_grid img.chosen").length > 0){
            return true
        }
        else{
            return false;
        }
    },
    checkTagSelection: function(){
        if ($("section.add .elements div.tags .selected").length > 0){
            console.info("We have tags");
            let tags = [];
            let new_tags = [];
            $( "section.add .elements div.tags .selected" ).each(function( index ) {
                tags.push($( this ).text());
                if ($(this).hasClass("new_submitted")){
                    console.info("Tag has new submitted class");
                    new_tags.push($( this ).text());
                }
              });
            return {"selections": tags, "new": new_tags};
        }
        else{
            console.info("No Tags");
            return null;
        }
    }
};

let submit_to_search = {
    init: function(){
        if (submitChecks.init()){
            submit_to_search.proceed();
        }
    },
    proceed: function(){
        let service = $("section.add .elements div#service_grid img.chosen").attr("alt");
        let title = $("section.add .elements.live_tv h2#title").text();
        console.info(`Service: ${service} / Title: ${title}`);
        this.saveService(service);
        this.saveOffset(0)
        this.saveTitle(title);
        data = {"service": service, "title": title, "offset": 0}
        this.request(data)
    },
    saveService: function(service){
        sessionStorage.setItem("service", service)
    },
    saveOffset:function(offset){
        sessionStorage.setItem("offset", offset)
    },
    saveTitle:function(title){
        sessionStorage.setItem("title", title)
    },
    retrieveData(){
        let service = sessionStorage.getItem("service");
        let offset = parseInt(sessionStorage.getItem("offset")) + 1;
        this.saveOffset(offset);
        let title = sessionStorage.getItem("title");
        data = {"service": service, "title": title, "offset": offset};
        return data;
    },
    request: function(data){
        $.when(ajaxCalls.ajaxCallData("POST", "/shows/live/search", data))
            .then(function(result){
                console.info("Success");
                console.log(result);
                if (result[0][0] == "Error, show not found"){
                    data.offset = data.offset + 1;
                    submit_to_search.saveOffset(data.offset)
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
        if (show[0] == "Error, further than 7 days"){
            $("div.live_tv.3 table tbody").append(`<tr>`+
                    `<td colspan="2">No More Results</td>`+
                "</tr>");
            $("div.live_tv.3 button.next").hide();
        }
        else{
            $("div.live_tv.3 table tbody").append(`<tr>`+
                    `<td>${show[0]}</td>`+
                    `<td><input type="radio" name="show" value=${show[1]}></td>` +
                "</tr>");
        }
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
        $.when(ajaxCalls.ajaxCallData("POST", "/shows/live", data))
            .then(function(result){
                console.info("Success");
                console.log(result);
                location.replace("/shows");
            }, function(){
                console.info("Failed");
                $(".error").show();
            });
    }
};

let addOD = {
    init: function(){
        if(submitChecks.initOD()){
            addOD.beginSubmit();
        }
    },
    beginSubmit: function(){
        let service = $("section.add .elements div#service_grid img.chosen").attr("alt");
        let title = $("section.add .elements.od_tv h2#title").text();
        let tags = submitChecks.checkTagSelection();
        let data = {"name": title, "service": service, "tags": tags.selections, "new_tags": tags.new};
        $.when(ajaxCalls.ajaxCallData("POST", "/shows/od", data))
            .then(function(result){
                console.info("Success");
                console.log(result);
                window.location.replace("../shows")
                //$("section#success").show();
            }, function(){
                console.info("Failed");
                //$("section#error").show();
            });
    },
};

let newTagDisplay = {
    init: function(content){
        console.info(content);
        this.addNewTag(content);
        this.resetEditedTag();
    },
    addNewTag: function(content){
        $(".elements.od_tv .tags").append(`<span contenteditable="true" class="new_submitted">${content}</span>`);
    },
    resetEditedTag: function(){
        $(".elements.od_tv .tags .new").text("New Tag").addClass("unedited");
    }
};

let bindings = {
    init: function(){
        this.clickLiveTV();
        this.clickOD();
        this.clickSubmit();
        this.showTitleBeginEntry();
        this.serviceSelection();
        this.confirmLiveShow();
        this.nextDaySearch();
        this.newTagEntry();
        this.tagSelection();
    },
    clickLiveTV:function(){
        $("section.add div.1 #live_tv").click(function(){
            $("div.1").hide();
            $("div.live_tv.2").show();
        });
    },
    clickOD: function(){
        $("section.add div.1 #on_demand").click(function(){
            $("div.1").hide();
            $("div.od_tv.2").show();
        });
    },
    clickSubmit: function(){
        $("section.add div.2 button#submit_to_search").click(function(){
            submit_to_search.init();
        });
        $("section.add div.2 button#od_submit").click(function(){
            addOD.init();
        });
    },
    showTitleBeginEntry: function(){
        $("section.add .elements.live_tv h2#title").click(function(){
            if ($(this).hasClass("unedited")){
                $(this).text("").removeClass("unedited");
            }
        });
        $("section.add .elements.od_tv h2#title").click(function(){
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
        $("div.live_tv.3 button.confirm").click(function(){
            $("div.live_tv.3 button").hide();
            let evtid = $("div.live_tv.3 table tbody input:checked").val();
            addShow.init(evtid);
        });        
    },
    nextDaySearch: function(){
        $("div.live_tv.3 button.next").click(function(){
            console.info("Searching")
            let data = submit_to_search.retrieveData();
            submit_to_search.request(data);
        });        
    },
    tagSelection: function(){
        $("section.add .elements.od_tv .tags").on('click', 'span', function(){
            if(!$(this).hasClass("new")){
                if ($(this).hasClass("selected")){
                    $(this).removeClass("selected");
                }
                else{
                    $(this).addClass("selected");
                }
            }            
        });
    },
    newTagEntry: function(){
        $(".elements.od_tv .tags .new").keyup(function(e){
            if (e.which === 13 && e.keyCode == 13){
                if (!$(this).hasClass("unedited")){
                    newTagDisplay.init($(this).text());
                }                
            }
            else{
                $(this).removeClass("unedited");
            }
        });

        $(".elements.od_tv .tags .new").click(function(){
            if ($(this).hasClass("unedited")){
                $(this).text("");
            }
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
