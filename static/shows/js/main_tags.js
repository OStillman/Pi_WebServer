let begin_tags = {
    init: function(){
        console.log("Ready - Tags");
        display_tags.init();
        tag_bindings.init();
    }
}

let display_tags = {
    init: function(){
        let these_tags = this.getTags();
        this.displayTags(these_tags);
    },
    getTags: function(){
        let these_tags = data_in.planner.tags;
        return these_tags;
    },
    displayTags: function(tags){
        for (let i = 0; i < tags.length; i++){
            $("section.one div.tags").append(`<span>${tags[i]}</span>`);
        }
    },
};

let GetShowsWithTag = {
    init: function(tag){
        let odData = data_in.planner.OD;
        let these_shows = this.sortThroughData(odData, tag);
        this.tagAnimate();
        this.displayShows(these_shows);
    },
    sortThroughData: function(data, tag){
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
            let this_class = "tall";
            if (shows[i].service == "bbc"){
                this_class = "long"
            }
            $("section.one div.show_output table tbody").append(
                `<tr><td>${shows[i].name}</td><td><img src='/static/shows/img/${shows[i].service}.png' class=${this_class}></tr>`);
        }
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
            $("section.one div.tags").empty();
            $("section.one div.show_output table tbody").empty().hide();
            display_tags.init();
        });
    }
}

let tag_bindings = {
    init: function(){
        this.tagClick();
    },
    tagClick: function(){
        $("section.one div.tags").on("click", "span", function(){
            if ($(this).hasClass("reset")){
                //$(this).remove();
                GetShowsWithTag.tagUnanimate();
            }
            else{
                $("section.one div.tags span").addClass("hide");
                let this_tag = $(this).removeClass("hide").addClass("selection").text();
                console.info(this_tag);
                GetShowsWithTag.init(this_tag);
            }
        });
    },
};