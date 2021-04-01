new Vue({
    el: '#hall',
    data: {
        halls: [],
        selected_hall: null,
        edit_mode: false,
        cashed_hall: null,
        selected_sites: [],
        show_create: false,
    },
    created(){
        makeAjaxRequest('get', '')
            .then(response => {
                this.halls = response.data.halls.map(hall => {return new Hall(hall)});
            });
        },

    methods: {
        choose_hall: function (hall_obj) {
            this.selected_hall = hall_obj;
            },
        set_edit_mode: function(){
            this.edit_mode = ! this.edit_mode;
            if(this.cashed_hall !== this.edit_mode){
                this.cashed_hall = this.edit_mode
            }
        },

        get_previous_number: function(row, site_obj){
            position = -1;
            for(site_num = site_obj.site_position - 1; site_num >= 0; site_num -= 1){
                if(row[site_num].is_exist && position <= site_num){
                    position = site_num;
                    console.log(site_num + '_________')
                }else {console.log(site_num)}
            }console.log('   ');
            if(position === -1){
                return 1;
            }else{
                return  row[position].site_number;
            }
        },

        remove_add_site: function(row, site_obj){
            if(site_obj.is_exist){
                for(site = site_obj.site_position; site < this.selected_hall.sites_amount; site += 1){
                    if(row[site].is_exist){
                        row[site].site_number -= 1;
                    }
                }site_obj.site_number = 0;
                site_obj.is_exist = false;
            }else{
                site_obj.site_number = this.get_previous_number(row, site_obj);
                site_obj.is_exist = true;
                for(site_num = site_obj.site_number; site_num  < this.selected_hall.sites_amount; site_num +=1){
                    if(row[site_num].is_exist){
                        row[site_num].site_number += 1
                    }
                }
            }
        },

        add_column: function(){
            sites_amount = this.selected_hall.sites_amount;
            for(row = 0; row <  this.selected_hall.rows.length; row += 1){
                console.log(this.selected_hall.rows[row][sites_amount - 1]);
                data = {
                    'id': 0,
                    'site_number': this.selected_hall.rows[row][sites_amount - 1].site_number + 1,
                    'site_position': sites_amount + 1,
                    'row': row + 1,
                    'is_exist': true,
                };
                this.selected_hall.rows[row].push(new Site(data));
            }
            this.selected_hall.sites_amount += 1
        },

        remove_column: function(col_num){
            for(row = 0; row <  this.selected_hall.rows.length; row += 1){
                delete this.selected_hall.rows[row].splice(col_num, 1)
            }
            this.selected_hall.sites_amount -= 1
        },

        add_row: function(){
            new_row = [];

            for(site = 1; site <= this.selected_hall.sites_amount; site += 1){
                data = {
                    'id': 0,
                    'site_number': site,
                    'site_position': site,
                    'row': this.selected_hall.rows.length,
                    'is_exist': true,
                };
                new_row.push(new Site(data));
            }
            this.selected_hall.rows.push(new_row);
        },

        remove_row: function(row_num){
            delete this.selected_hall.rows.splice(row_num, 1);
        },

        choose_site: function (site_obj) {
            index_of = this.selected_sites.indexOf(site_obj);
            if(index_of === -1){
                this.selected_sites.push(site_obj);
                site_obj.is_selected = true;
            }else {
                delete this.selected_sites.splice(index_of, 1);
                site_obj.is_selected = false;
            }
        }
    }
});