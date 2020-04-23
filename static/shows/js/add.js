let begin = {
    init: function () {
        $(document).ready(function () {
            console.info("Ready");
            bindings.init();
        });
    }
};

let submitTasks = {
    init: function(){
        //TODO: Conditional Choices? Collect
        let title = this.checkHasChanged("h2");
        let length = this.checkHasChanged("p#length span");
        let service = this.checkServiceSelection();
        let tags = this.checkTagSelection();
        if (service == "netlix" || service == "disney" || service == "amazon"){
            this.ODServiceCheck(title, length, service, tags);
        }
        else{
            this.complexServiceCheck(title, length, service, tags);
        }
        
    },
    ODServiceCheck: function(title, length, service, tags){
        if (tags && service && length && title){
            console.info("READY");
        }
        else{
            console.info("NOT READY");
        }
    },
    complexServiceCheck: function(title, length, service, tags){
        let day = $("section.add .elements .airtime#day select option:selected").val();
        let time = $("section.add .elements .airtime#time input").val();
        //console.info(time);
        if (day != "N/A"){
            console.info("they've specified a day");
        }
        else{
            console.info("Day is N/A");
        }
        
    },
    checkHasChanged: function (element) {
        if ($("section.add .elements " + element).hasClass("unedited")) {
            return null;
        }
        else {
            return $("section.add .elements " + element).text();
        }
    },
    checkServiceSelection: function(){
        if ($("section.add .elements div#service_grid img.chosen").length > 0){
            console.info("We have one");
            return $("section.add .elements div#service_grid img.chosen").attr("alt");
        }
        else{
            console.info("No Service");
            return null;
        }
    },
    checkTagSelection: function(){
        if ($("section.add .elements div.tags .selected").length > 0){
            console.info("We have tags");
            let tags = []
            $( "section.add .elements div.tags .selected" ).each(function( index ) {
                tags.push($( this ).text());
              });
            //console.log(tags);
            return tags;
        }
        else{
            console.info("No Tags");
            return null;
        }
    }
};

let bindings = {
    init: function() {
        this.submitClick();
        this.serviceSelection();
        this.showTitleBeginEntry();
        this.showLengthBeginEntry();
        this.tagSelection();
        this.daySelection();
    },
    submitClick: function(){
        $("section.add #submit").click(function(){
            console.info("Submit chosen");
            submitTasks.init();
        });
    },
    serviceSelection: function(){
        $("section.add .elements div#service_grid img").click(function(){
            $("section.add .elements div#service_grid img").removeClass("chosen").css("filter", "opacity(20%)");
            $(this).css("filter", "opacity(100%)").addClass("chosen")
            if ($(this).hasClass("tv")){
                $(".airtime").show();
            }
            else{
                $(".airtime").hide();
            }
        });
    },
    showTitleBeginEntry: function(){
        $("section.add .elements h2#title").click(function(){
            if ($(this).hasClass("unedited")){
                $(this).text("").removeClass("unedited");
            }
        });
    },
    showLengthBeginEntry: function(){
        $("section.add .elements p#length span").click(function(){
            if ($(this).hasClass("unedited")){
                $(this).text("").removeClass("unedited");
            }
        });
    },
    tagSelection: function(){
        $("section.add .elements .tags span").click(function(){
            if ($(this).hasClass("selected")){
                $(this).removeClass("selected");
            }
            else{
                $(this).addClass("selected");
            }
        });
    },
    daySelection: function(){
        $("section.add .elements .airtime#day select").change(function(){
            let thisday = $(this).children("option:selected").val();
            //console.log(thisday);
            if (thisday == "N/A"){
                //console.log("Yup it's N/A");
                $("section.add .elements .airtime#time").hide().children("input").val("00:00");
            }
            else{
                $("section.add .elements .airtime#time").show();
            }
        });
    }
};