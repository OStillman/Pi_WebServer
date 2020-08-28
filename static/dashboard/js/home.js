var presence_detection = new Vue({
    el: ".presence-detection",
    data: {
        owen_status: "out",
        kay_status: "out"
    }
});

var food_tonight = new Vue({
    el: ".info-pane.r",
    data: {
        today: "Spag Bowl",
        tomorrow: "Bangers and Mash"
    }
});

var on_tonight = new Vue({
    el: ".info-pane.l",
    data: {
        seven: "-",
        eight: "-",
        nine: "-",
        ten: "-"
    }
});

var bottom_bar = new Vue({
    el: "section.bottom-nav",
    template: `
        <BottomNav/>
    `,
    components: {BottomNav}
});

function currentTime(){
    const monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];
    var d = new Date();
    var s = d.getSeconds();
    var m = d.getMinutes();
    var h = d.getHours();
    var date = d.getDate();
    var month = monthNames[d.getMonth()];
    var y = d.getFullYear();
    if (m.toString().length == 1){
        m = `0${m}`;
    }
    return `${h}:${m} ${date} ${month} ${y}`;
}

function initialFetch(){
    axios
        .get('/dash/initial')
        .then((response) => {
            console.info("Initial Data Request Succeeded");
            header.notices = "No Notices";
        }, (error) => {
            console.log(error);
            header.isAlert = true;
            header.notices = "Initial Data Request Failed";
        });
}

//MQTT Home

function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("onConnect");
    header.notices = "Requesting Initial MQTT Data...";
    presence_owen.init();
    presence_kay.init();
    today_shows.init();
    initialFetch();
}

// called when a message arrives
function onMessageArrived(message) {
    //console.log("Message arrived: topic=" + message.destinationName + ", message=" + message.payloadString);
    if (message.destinationName ==  "presence/owen"){
        presence_owen.statusUpdate(message.payloadString);
    }
    else if (message.destinationName == "presence/kay"){
        presence_kay.statusUpdate(message.payloadString);
    }
    else if (message.destinationName == "today/shows"){
        today_shows.showsUpdated(message.payloadString)
    }
}

let presence_owen = {
    init: function(){
        console.info("Subscribing to Owen's status...");
        client.subscribe("presence/owen");
        console.info("Subscribed to Owen")
    },
    statusUpdate: function(status){
        console.info("Owen's status has been updated");
        console.log(`Owen is ${status}`);
        presence_detection.owen_status = status
    }
};

let presence_kay = {
    init: function(){
        console.info("Subscribing to Kayleigh's Status...");
        client.subscribe("presence/kay")
        console.info("Subscribed to Kayleigh")
    },
    statusUpdate: function(status){
        console.info("Kayleigh's status has been updated");
        console.log(`Kayleigh is ${status}`);
        presence_detection.kay_status = status
    }
};

let today_shows = {
    init: function(){
        console.info("Subscribing to Today's Shows...");
        client.subscribe("today/shows")
        console.info("Subscribed to Today's Shows")
    },
    showsUpdated: function(shows){
        console.info("Today's Shows have been updated");
        console.log(`On Today is ${shows}`);
        this.beginUpdate(shows);
    },
    beginUpdate: function(shows){
        shows = shows.replace(/'/g, '"');
        shows = JSON.parse(shows);

        on_tonight.seven = this.checkContent(shows["planner"]["19"]);
        on_tonight.eight = this.checkContent(shows["planner"]["20"]);
        on_tonight.nine = this.checkContent(shows["planner"]["21"]);
        on_tonight.ten = this.checkContent(shows["planner"]["22"]);
    },
    checkContent: function(hour){
        if (hour.length > 0){
            return this.formatContent(hour);
        }
        else{
            return "-";
        }
    },
    formatContent: function(hour){
        length = hour.length;
        //console.log(hour);
        final_content = "";
        for (let i = 0; i < length; i++){
            final_content += hour[i].name;
            if (i < length -1){
                final_content += " <br>";
            }
        }
        //console.log(final_content);
        return final_content
    },
}


setInterval(function(){
    header.getCurrentTime();
}, 1000)