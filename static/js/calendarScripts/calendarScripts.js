

function onCreated(instance){
        var time_now = new Date();
        instance.today = new Date(
            time_now.getFullYear(), time_now.getMonth(), time_now.getDate());
        instance.selected_mouth = new Date(
            time_now.getFullYear(), time_now.getMonth());
        instance.calendar_list = instance.get_calendar_list(
            time_now.getFullYear(), time_now.getMonth());
}

function days_in_month(year, month){
    let days_in_month;
    if(month === 1){
        if ((year % 4 === 0 && year % 100 !== 0)|| year % 400 === 0 ){
            days_in_month = 29}
        else{
            days_in_month = 28
        }
    }else if( [0, 2, 4, 6, 7, 9, 11].indexOf(month) !== -1){
        days_in_month = 31
    }else {
        days_in_month = 30
    }
    return days_in_month
}

function get_month_list(year, month){
    var days = [];
    for(let day = 0; day < days_in_month(year, month); day++){
        days.push(new Date(year, month, day + 1))
    }
    return days
}

function align_calendar_list(month_list, sunday_is_first_day){
    if (sunday_is_first_day){

        var first_day = 0;  var last_day = 6;
    }else{
        first_day = 1;  last_day = 0;
    }
    while (month_list[0].getDay() !== first_day) {
        var previous_day = new Date(month_list[0]);
        previous_day.setDate(previous_day.getDate() - 1);
        month_list.unshift(previous_day);
    }
    while (month_list[month_list.length - 1].getDay() !== last_day) {
        var next_day = new Date(month_list[month_list.length - 1]);
        next_day.setDate(next_day.getDate() + 1);
        month_list.push(next_day);
    }
    return month_list
}

function get_calendar_list(year, month){
    var days = align_calendar_list(get_month_list(year, month));
    var calendar_list = [];
    var weeks_amount = days.length/7;
    for(var week = 0; week < weeks_amount; week++ ){
        var days_in_week = [];
        for(var week_day = 0; week_day < 7; week_day++){
            days_in_week.push(days.shift())
        }
        calendar_list.push(days_in_week)
    }
    return calendar_list
}

function changeMonth(adding, app_instance){
    var new_selected_mouth = new Date(app_instance.selected_mouth);
    new_selected_mouth.setMonth(new_selected_mouth.getMonth() + adding);
    app_instance.selected_mouth = new_selected_mouth;
    app_instance.calendar_list = app_instance.get_calendar_list(
        app_instance.selected_mouth.getFullYear(),
        app_instance.selected_mouth.getMonth()
    );
}

function is_equals_date(date1, date2){
    return date1.getDate() === date2.getDate()
        && date1.getMonth() === date2.getMonth()
        && date1.getFullYear() === date2.getFullYear();
}

function get_day_url(day, zero_day){
    var slug = (day - zero_day)/(24*60*60*1000);
    return '/schedule/day=' + slug + '/'
}

export {
    onCreated,
    align_calendar_list,
    changeMonth,
    days_in_month,
    get_calendar_list,
    get_day_url,
    get_month_list,
    is_equals_date
}