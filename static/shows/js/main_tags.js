let begin_tags = {
    init: function(){
        console.log("Ready - Tags");
        display_tags.init();
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