let begin = {
    init: function () {
        $(document).ready(function () {
            console.info("Ready");
            display.init();
            bindings.init();
        });
    }
};

let bindings = {
    init: function () {
        this.nextClick();
    },
    nextClick: function () {
        $(".next img").click(function () {
            console.info("Next Clicked");
            display.init(true);
        });
    },
};

let display = {
    init: function (number = false) {
        let this_item = this.menuItem(number);
        this.itemsNeeded(this_item);
    },
    menuItem: function (number = false) {
        let this_item = 0;
        if (!number) {
            $(".item h1").text(data_in.menu.options[0].name).attr("id", this_item);
        } else {
            this_item = parseInt($(".item h1").attr("id"));
            this_item++;
            if (data_in.menu.options.length <= this_item) {
                this_item = 0;
            }
            $(".item h1").text(data_in.menu.options[this_item].name).attr("id", this_item);
        }
        return this_item
    },
    itemsNeeded: function (this_item) {
        let items = [];
        items = data_in.menu.options[this_item].items;
        this.displayItems(items);
    },
    displayItems: function (items) {
        $(".item ul").empty();
        for (let i = 0; i < items.length; i++) {
            $(".item ul").append("<li>" + items[i] + "</li>");
        }
    },
};