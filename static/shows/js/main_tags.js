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
            let this_class = "tall";
            if (shows[i].channel == "BBC1" || shows[i].channel == "BBC2"){
                this_class = "long";
            }
            else if (shows[i].channel == "ITV1" || shows[i].channel == "ITV2"){
                this_class = "long";
                shows[i].channel == "itv"
            }
            $("section.one div.show_output table tbody").append(
                `<tr><td>${shows[i].name}</td><td><img src='/static/shows/img/${shows[i].channel.toLowerCase()}.png' class=${this_class}></tr>`);
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
            $("section.one div.tags .selection").css("width", "auto")
            $("section.one div.tags span").removeClass("reset").removeClass("selection").show();
            $("section.one div.show_output table tbody").empty().hide();
            //display_tags.init();
        });
    }
}

let tag_bindings = {
    init: function(){
        this.tagClick();
        this.tagElementSwipe();
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
    tagElementSwipe: function(){
        /*
        document.addEventListener('swiped-left', function(e){
            console.log(e.target);
        })
        */
       $("section.one div.show_output table").on('swiped-left', 'tr', function(){
           console.log("They've swiped a event");
           alert("swipe")
       });
    }
};