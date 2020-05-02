let begin = {
    init: function () {
        $(document).ready(function () {
            console.info("Ready");
            setScroll.init();
            bindings.init();
            //display.init();
            //Splitting out the files - Callers below
            begin_tags.init();
            today_begin.init();
        });
    }
};

let setScroll = {
    init: function(){
        var elmnt = document.getElementById("start");
        elmnt.scrollIntoView();
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
        let shows_length = our_data.planner.shows.length;
        for (let i = 0; i < shows_length; i++){
            let this_show = our_data.planner.shows[i];
            let these_tags = "";
            for (let j = 0; j < this_show.tags.length; j++){
                these_tags += `${this_show.tags[j]} `;
            }
            $(`table tbody`).append(`` +
                `<tr id='s${i}' class="${these_tags}">` +
                `<td>${this_show.name}</td>` +
                `<td>${this_show.duration}</td>` +
                `<td> <img src='${this_show.service}' class='${this_show.class}'></td>` +
                `<td>${this_show.time}<br>${this_show.day}</td>` +
                `</tr>`);
        }
    }
};

let removeShow = {
    init: function(element_num){
        $("section.shows table").hide();
        $("section.loading").show();
        console.info(element_num);
        data = {"element": element_num};
        this.runDelete(data);
    },
    runDelete: function(data){
        $.when(ajaxCalls.ajaxCallData("DELETE", "/shows", data))
            .then(function(result){
                console.info("Success");
                window.location.reload();
                //$("section#success").show();
            }, function(){
                console.info("Failed");
                //$("section#error").show();
            })
    }
};

let bindings = {
    init: function () {
        this.doubleClickTable();
    },
    doubleClickTable: function(){
        $("table tbody").on('dblclick', 'tr', function(){
            console.log("Double clicked");
            let this_name = $(this).closest('tr').children('td:first').text();
            console.info(this_name);
            if(window.confirm(`Delete ${this_name}?`)){
                let this_number = $(this).attr("id").charAt(1);
                removeShow.init(this_number);
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
    }
};