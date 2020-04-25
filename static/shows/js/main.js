let begin = {
    init: function () {
        $(document).ready(function () {
            console.info("Ready");
            bindings.init();
            display.init();
        });
    }
};

let display = {
    init: function(){
        console.log(data_in);
        let updated_data = this.replaceImg(data_in);
        this.output(updated_data);
    },
    replaceImg: function (our_data) {
        let shows_length = our_data.planner.shows.length;
        for (let i = 0; i < shows_length; i++){
            let this_show = our_data.planner.shows[i];
            our_data.planner.shows[i] = display.decideImg(this_show);
        }
        return our_data;
    },
    decideImg: function(this_show){
        this_show.service = this_show.service.toLowerCase();
        if (this_show.service == "bbc"){
            this_show.service = '/static/shows/img/bbc.png';
            this_show.class="long";
            return this_show
        }
        else if (this_show.service == "itv"){
            this_show.service = '/static/shows/img/itv.png';
            this_show.class="long";
            return this_show
        }
        else if (this_show.service == "c4"){
            this_show.service = '/static/shows/img/c4.png';
            this_show.class="c4";
            return this_show
        }
        else if (this_show.service == "e4"){
            this_show.service = '/static/shows/img/e4.png';
            this_show.class="c4";
            return this_show
        }
        else if (this_show.service == "netflix"){
            this_show.service = '/static/shows/img/netflix.png';
            this_show.class="long";
            return this_show
        }
        else if (this_show.service == "disney"){
            this_show.service = '/static/shows/img/disney.png';
            this_show.class="long";
            return this_show
        }
        else if (this_show.service == "sky"){
            this_show.service = '/static/shows/img/sky.png';
            this_show.class="long";
            return this_show
        }
        else if (this_show.service == "amazon"){
            this_show.service = '/static/shows/img/amazon.png';
            this_show.class="c4";
            return this_show
        }
        else if (this_show.service == "5"){
            this_show.service = '/static/shows/img/5.png';
            this_show.class="c4";
            return this_show
        }
    },
    output: function (our_data) {
        console.info(our_data);
        let shows_length = our_data.planner.shows.length;
        for (let i = 0; i < shows_length; i++){
            let this_show = our_data.planner.shows[i];
            $("table tbody").append("" +
                "<tr>" +
                "<td>" + this_show.name + "</td>" +
                "<td>" + this_show.duration + "</td>" +
                "<td> <img src='" + this_show.service + "' class='" + this_show.class + "'></td>" +
                "<td>" + this_show.time + "<br>" + this_show.day +"</td>" +
                "</tr>");
        }
    }
};

let bindings = {
    init: function () {
        //this.nextClick();
    },
};