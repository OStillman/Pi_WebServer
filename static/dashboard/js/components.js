const BottomNav = {
    template: `
    <section class="bottom-nav">
        <a href="./">
            <img src="/static/dashboard/img/home.svg">
        </a>
        <a href="./tv">
            <img src="/static/dashboard/img/tv.svg">
        </a>
        <img src="/static/dashboard/img/menu.svg">
        <img src="/static/dashboard/img/light.svg">
    </section>
    `
}

var header = new Vue({
    el: ".header",
    template: `
    <section class="header">
        <p class="datetime">{{datetime}}</p>
        <span class="message">
            <p class="message"><img v-if="isAlert" height="20" src="/static/dashboard/img/error.svg"> {{notices}} </p>
        </span>
    </section>
    `,
    data: {
        datetime: "",
        notices: "Connecting to MQTT...",
        isAlert: false,
    },
    methods: {
        getCurrentTime: function(){
            this.datetime = currentTime();
        }
    }
});