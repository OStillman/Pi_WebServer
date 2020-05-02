let today_begin = {
    init: function () {
        today_data.planner[20].sort((a, b) => a.time.localeCompare(b.time))
        console.log(today_data);
        today_display.init();
    },
};

let today_display = {
    init: function(){
        this.getRowData();
    },
    getRowData: function(){
        this.addRow("7", today_data.planner[19]);
        this.addRow("8", today_data.planner[20]);
        this.addRow("9", today_data.planner[21]);
        this.addRow("10", today_data.planner[22]);
    },
    addRow: function(time, data){
        for (let i = 0; i < data.length; i++){
            $(`.content.${time} .output.name`).append(`${data[i].name} <br>`);
            $(`.content.${time} .output.duration`).append(` ${data[i].duration} <br>`);
            
        }        
    }
};