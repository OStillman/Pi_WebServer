let begin_all = {
    init: function(){
        console.log("Ready - All");
        all_display.init();
        all_bindings.init();
    }
}

let all_bindings = {
    init: function(){
        this.left_arrow();
        this.right_arrow();
    },
    left_arrow: function(){
        $("section.three div.bottom_nav .left").click(function(){
            let this_class = $("section.three ul").attr("class").split(" ");
            this_class[1]--;
            all_display.control(this_class);
        });
    },
    right_arrow: function(){
        $("section.three div.bottom_nav .right").click(function(){
            let this_class = $("section.three ul").attr("class").split(" ");
            this_class[1]++;
            all_display.control(this_class);
        });
    }
};

let all_display = {
    init: function(){
        this.displayShowTV(0);        
    },
    control: function(current_class){
        console.info(current_class);
        let current_show = current_class[1];
        if (current_class[0] == "tv"){
            this.displayShowTV(current_show);
        }
        else{
            this.displayShowOD(current_show);
        }
    },
    displayShowTV:function(count){
        try {
            let this_show = data_in.planner.shows[count];
            $("section.three div.all_shows ul").attr("class", `tv ${count}`)
            $("section.three div.all_shows li h1.show_name").text(this_show.name);
            $("section.three div.all_shows li.service").text(all_display.fixShowNames(this_show.service));            
        } catch (error) {
            if (count < 0){
                this.displayShowOD(data_in.planner.OD.length - 1)
            }
            else{
                this.displayShowOD(0);
            }
            
        }
    },
    displayShowOD: function(count){
        console.info("It needs to now be OD");
        try {
            let this_show = data_in.planner.OD[count];
            $("section.three div.all_shows ul").attr("class", `od ${count}`)
            $("section.three div.all_shows li h1.show_name").text(this_show.name);
            $("section.three div.all_shows li.service").text(all_display.fixShowNames(this_show.service));            
        } catch (error) {
            if (count < 0){
                this.displayShowTV(data_in.planner.shows.length - 1);
            }
            else{
                this.displayShowTV(0);
            }
            
            
        }
    },
    fixShowNames:function(show_name){
        if (show_name == "c4"){
            return "Channel 4";
        }
        else if (show_name == "e4"){
            return "E4"
        }
        else{
            return show_name.charAt(0).toUpperCase() + show_name.slice(1);
        }
    }
}