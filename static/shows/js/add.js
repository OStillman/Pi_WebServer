let begin = {
    init: function () {
        $(document).ready(function () {
            console.info("Ready");
            bindings.init();
        });
    }
};

let bindings = {
    init: function() {
        this.serviceSelection();
        this.showTitleBeginEntry();
        this.tagSelection();
        this.daySelection();
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
                console.log("Yup it's N/A");
                $("section.add .elements .airtime#time").hide().children("span").text("00:00");
            }
            else{
                $("section.add .elements .airtime#time").show();
            }
        });
    }
};