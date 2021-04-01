import {
    onCreated,
    align_calendar_list,
    changeMonth,
    days_in_month,
    get_calendar_list,
    get_day_url,
    get_month_list,
    is_equals_date
} from "./calendarScripts.js";


var app = new Vue({
    el: '#calendar',
    data: {
        settings:{
            zero_day: new Date(2021, 0),
            sunday_is_first_day: false,
        },
        today: null,
        selected_mouth: null,
        calendar_list: [],
        mouths_name: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        days_of_week_names: ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'],
    },
    created(){
        onCreated(this);
    },

    methods: {
        days_in_month: days_in_month(year, month),
        get_month_list: get_month_list(year, month),
        align_calendar_list: align_calendar_list(month_list, this.settings.sunday_is_first_day),
        get_calendar_list: get_calendar_list(year, month),
        changeMonth: changeMonth(adding, this),
        is_equals_date: is_equals_date(date1, date2),
        get_day_url: get_day_url(day, this.settings.zero_day),
    }
});