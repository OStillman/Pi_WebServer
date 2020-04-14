let begin = {
    init: function () {
        $(document).ready(function () {
            console.info("Ready");
            bindings.init();
        });
    }
};

let bindings = {
    init: function () {
        this.addClick();
        this.uneditedFocus();
        this.submitClick();
    },
    addClick: function () {
        $(".actions #add").click(function(){
           console.log("Add Clicked");
           add.init();
        });
    },
    submitClick: function(){
        $(".actions #tick").click(function(){
           console.info("Submit Clicked");
           submit.init();
        });
    },
    uneditedFocus: function () {
        $(".unedited").click(function(){
           console.info("Unedited clicked");
            $(this).removeClass("unedited").text("");
        });
    }
};

let submit = {
    init: function () {
        $("section.item_add").hide();
        let title = (this.getTitle());
        let items = (this.getListItems());
        let data = this.sortJSON(title, items);
        this.submitData(data);
    },
    getTitle: function () {
        return $(".item h1").text();
    },
    getListItems: function () {
        let fetch_items = [];
        $("ul li").each(function() { fetch_items.push($(this).text()) });
        return fetch_items;
    },
    sortJSON: function (title, items) {
        return {
        "name": title,
        "items": items
      }
    },
    submitData: function (data) {
        console.log(data);
        $.when(ajaxCalls.ajaxCallData("POST", "./add", data))
            .then(function(result){
                console.info("Success");
                console.log(result);
                $("section#success").show();
            }, function(){
                console.info("Failed")
                $("section#error").show();
            })
    }
};

let add = {
    init: function () {
        this.addListItem();
    },
    addListItem: function () {
        $(".item ul").append("<li contenteditable='true'></li>");
        $(".item ul li:last").focus();
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