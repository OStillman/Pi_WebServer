let begin = {
    init: function () {
        $(document).ready(function () {
            console.info("Ready");
            calendar.init();
        });
    }
};

let calendar = {
    init: function(){
        let d = new Date();
        let month = this.getMonth(d);
        let first_day = this.getFirstDay(d);
        let month_length = this.getMonthLength(d);
        let today = this.getToday(d);
        let dayNum = this.getDayNum(d);
        this.displayTitle(dayNum, today, month);
        this.displayCalendar(first_day, month_length, today);
    },
    getMonth: function(date){
        let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        return months[date.getMonth()];
    },
    getFirstDay: function(date){
        return new Date(date.getFullYear(), date.getMonth(), 1).getDay();
    },
    getMonthLength: function(date){
        return new Date(date.getFullYear(), date.getMonth()+1, 0).getDate();
    },
    getToday: function(date){
        return date.getDate();
    },
    getDayNum: function(date){
        return date.getDay()
    },
    displayTitle: function(dayNum, today, month){
        let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        $("#calendar h2").text(`${days[dayNum]} ${today} ${month}`);
    },
    displayCalendar: function(first_day, month_length, today){
        let date_num = 1;
        $( "#calendar ul.days li" ).each(function( index ) {
            if (index >= first_day && date_num <= month_length){
                if (date_num === today){
                    $(this).html(`<span class='active'>${date_num}</span>`);
                }
                else{
                    $(this).text(date_num);
                }                
                date_num++;
            }
            else if (index < first_day){
                $(this).text("");
            }
            else if (date_num > month_length){
                $(this).text("");
            }
          });
    }
};