let begin = {
    init: function(){
        $(document).ready(function(){
            sort_parent_url.init();
        }); 
    },
};

let sort_parent_url = {
    init: function(){
        let current_url = window.location.pathname;
        let complete_url = this.format_url(current_url);
        console.info(complete_url);
        this.add_url(complete_url);
    },
    format_url: function(url){
        url_split = url.split("/")
        split_length = url_split.length - 1
        end_url = ""
        for (let i = 0; i < split_length; i++){
            end_url += url_split[i]
            if (i != split_length - 1){
                end_url += "/"
            }
        }
        return end_url;
    },
    add_url: function(url){
        $("section.directory_view section.directory_grid div.parent a").attr("href", url);
    }
};