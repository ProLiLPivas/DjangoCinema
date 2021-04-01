class Site{

    constructor(data=null){
        if (data){
            this.id = data.id;
            this.site_number = data.site_number;
            this.site_position = data.site_position;
            this.row = data.row;
            this.is_exist = data.is_exist;
        }

    }
    id = 0;
    site_number = 0;
    site_position = 0;
    row = 0;
    is_exist = true;
    is_selected = false;
}