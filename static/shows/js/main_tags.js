let begin_tags = {
    init: function(){
        console.log("Ready - Tags");
        tag_bindings.init();
    }
}


let GetShowsWithTag = {
    init: function(tag){
        let these_shows = this.sortThroughData(od_data.Planner.Shows, tag);
        this.tagAnimate();
        this.displayShows(these_shows);
    },
    sortThroughData: function(data, tag){
        console.log(data);
        let these_shows = [];
        for (let i = 0; i < data.length; i++){
            let this_show = data[i];
            if (GetShowsWithTag.checkShow(this_show, tag)){
                //console.info("This show matches the tag");
                these_shows.push(this_show);
            }
        }
        //console.log(these_shows);
        return these_shows
    },
    checkShow: function(show, tag){
        let these_tags = show.tags;
        for (let i = 0; i < these_tags.length; i++){
            if (these_tags[i] == tag){
                return true;
            }
        }
        return false;
    },
    displayShows: function(shows){
        for (let i = 0; i < shows.length; i++){
            $("section.one div.show_output table tbody").append(
                `<tr style="opacity: ${this.displayOpacity(shows[i].watching)};" class="${shows[i].id}"><td>${shows[i].name}</td><td>${this.displaySeasonEpisode(shows[i].series, shows[i].episode)}</td><td><img src='/static/shows/img/${shows[i].channel.toLowerCase()}.png' class=${this.getDisplayClass(shows[i])}></tr>`);
        }
    },
    getDisplayClass: function(show){
        let this_class = "tall";
        if (show.channel == "BBC1" || show.channel == "BBC2"){
            this_class = "long";
        }
        else if (show.channel == "ITV1" || show.channel == "ITV2"){
            this_class = "long";
            //shows[i].channel == "itv"
        }
        return this_class
    },
    sortDisplayChannel: function(channel){
        if (channel == "ITV1" || channel == "ITV2"){
            return "ITV"
        }
        else{
            return channel;
        } 
    },
    displayOpacity: function(status){
        let opacity = 1;
        if (status == "N" || !status){
            opacity = 0.7;
        }
        return opacity
    },
    displaySeasonEpisode: function(season, episode){
        let output = ""
        if (season){
            output = `S${season}`;
        }
        if (episode){
            if (output.length > 0){
                output += " ";
            }
            output += `E${episode}`
        }
        return output;
    },
    tagAnimate: function(tag){
        $.when($("section.one div.tags .hide").fadeOut()).done(function(){
            $.when($("section.one div.tags .selection").animate({width: "300px"}).css("text-align", "center").addClass("reset")).done(function(){
                $("section.one div.show_output table tbody").fadeIn();
            });
        });              
    },
    tagUnanimate: function(){
        $.when($(".section.one div.tags .reset").fadeOut()).done(function(){
            $("section.one div.tags .selection").css("width", "auto")
            $("section.one div.tags span").removeClass("reset").removeClass("selection").show();
            $("section.one div.show_output table tbody").empty().hide();
            $("section.one div.edit").hide();
            //display_tags.init();
        });
    }
}

let tag_progress = {
    init: function(show_id){
        //console.info(`This ID: ${show_id}`)
        show_id = parseInt(show_id);
        this_show = this.getShow(show_id);
        this.displayShow(this_show);
    },
    getShow: function(id){
        for (let i = 0; i < od_data.Planner.Shows.length; i++){
            //console.info(od_data.Planner.Shows[i]);
            let this_show = od_data.Planner.Shows[i];
            if (this_show.id == id){
                return od_data.Planner.Shows[i];
            }
        }        
    },
    displayShow: function(show){
        $("section.one div.edit p").text(show.name).attr("class", show.id);
        if (show.watching == "Y"){
            $("#watching input").attr("checked", true);
        }
        else{
            $("#watching input").attr("checked", false);
        }
        $("#season input").val(show.series);
        $("#episode input").val(show.episode);
    },
    onClose: function(){
        if ($("section.one div.edit").is(":visible")){
            console.info("We gotta update");
            let new_details = this.onCloseFetchDetails();
            console.info(new_details);
            this.onCloseUpdateIt(new_details);
            GetShowsWithTag.tagUnanimate();
        }
        else{
            GetShowsWithTag.tagUnanimate();
        }
    },
    onCloseFetchDetails: function(){
        let this_show = $("section.one div.edit p").attr("class");
        let watching = this.onCloseSortWatching();
        let season = $("#season input").val();
        let episode = $("#episode input").val();
        return {"id": this_show, "watching": watching, "season": season, "episode": episode};
    },
    onCloseSortWatching: function(){
        //console.log(status);
        if ($("#watching input").is(":checked")){
            return "Y"
        }
        else{
            return "N"
        }
    },
    onCloseUpdateIt: function(new_details){
        for (let i = 0; i < od_data.Planner.Shows.length; i++){
            //console.info(od_data.Planner.Shows[i]);
            let this_show = od_data.Planner.Shows[i];
            if (this_show.id == new_details.id){
                od_data.Planner.Shows[i].watching = new_details.watching;
                od_data.Planner.Shows[i].series = new_details.season;
                od_data.Planner.Shows[i].episode = new_details.episode;
                this.onCloseUpdateDB(od_data.Planner.Shows[i])
                break;
            }
        }    
    },
    onCloseUpdateDB: function(show){
        console.info(show);
        $.when(ajaxCalls.ajaxCallData("PUT", "/shows/od", show))
            .then(function(result){
                console.info("Success");
                console.log(result);
            }, function(){
                console.info("Failed");
            })
    }
};

let tag_bindings = {
    init: function(){
        this.tagClick();
        this.tagElementClick();
    },
    tagClick: function(){
        $("section.one div.tags").on("click", "span", function(){
            if ($(this).hasClass("reset")){
                //$(this).remove();
                tag_progress.onClose();
                //GetShowsWithTag.tagUnanimate();
            }
            else{
                $("section.one div.tags span").addClass("hide");
                let this_tag = $(this).removeClass("hide").addClass("selection").text();
                console.info(this_tag);
                GetShowsWithTag.init(this_tag);
            }
        });
    },
    tagElementClick: function(){
        $("section.one table tbody").on("dblclick", "tr", function(e){
            $("section.one div.show_output table tbody").hide();
            let this_id = $(this).attr("class");
            tag_progress.init(this_id)
            $("section.one div.edit").show();
        });
    }
};