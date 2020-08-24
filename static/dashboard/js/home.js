var presence_detection = new Vue({
    el: ".presence-detection",
    data: {
        owen_status: "in",
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
        eight: "Gogglebox",
        nine: "-",
        ten: "Celebrity Masterchef"
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

setInterval(function(){
    header.getCurrentTime();
}, 1000)