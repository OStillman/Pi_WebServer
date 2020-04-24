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
        let day = $("section.add .elements .airtime#day select option:selected").val();
        let time = $("section.add .elements .airtime#time input").val();
        if(this.submitCheck(length)){
            if (this.dayNeeded(day)){
                if (this.timeNeeded(time)){
                    console.info("Everything needed");
                }
                else{
                    console.info("Only need day");
                }
            }
            else{
                console.info("Day/Time not needed");
            }
        }
        
    },
    submitCheck: function(length){
        if (length){
            console.info("We are ready");
            return true;
        }
        else{
            console.info("Everything but length");
            return false;
        }
    },
    dayNeeded: function(day){
        if (day == "N/A"){
            console.info("Day is N/A");
            return false
        }
        else{
            return true;
        }
    },
    timeNeeded: function(time){
        if (time == "00:00"){
            console.info("Time is 00:00");
            return false;
        }
        else{
            return true;
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

let advanceStage = {
    init: function(stage){
        if (stage < 3){
            console.log("We have another stage");
            if (this.selectionChecker(stage)){
                this.advance(stage);
            }            
        }
        else{
            submitTasks.init();
        }
    },
    advance: function(stage){
        let new_stage = stage + 1;
        console.log(new_stage);
        $(".elements." + stage).hide();
        $(".elements." + new_stage).show();
    },
    selectionChecker: function(stage){
        let check_outcome = false;
        switch(stage){
            case 1:
                if (submitTasks.checkHasChanged("h2") && submitTasks.checkTagSelection()){
                    check_outcome = true;
                }
                break;
            case 2:
                if (submitTasks.checkServiceSelection()){
                    check_outcome = true;
                }
                break;
        }
        return check_outcome;
    }
}

let bindings = {
    init: function() {
        this.serviceSelection();
        this.showTitleBeginEntry();
        this.showLengthBeginEntry();
        this.tagSelection();
        this.daySelection();
        this.nextButton();
    },
    nextButton: function(){
        $("section.add").on('click', '.elements .next-button', function(){
            let this_stage = $(this).closest("div.elements").attr("class").split(" ")[1];
            console.log(this_stage);
            advanceStage.init(parseInt(this_stage));
        });
    },
    serviceSelection: function(){
        $("section.add .elements div#service_grid img").click(function(){
            $("section.add .elements div#service_grid img").removeClass("chosen").css("filter", "opacity(20%)");
            $(this).css("filter", "opacity(100%)").addClass("chosen")
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