class Hall{
    /* class of cinema hall */

    constructor(data){
        this.id = data.id;
        this.name = data.number;
        this.is_vip = data.is_vip;
        this.sites_amount = data.sites_amount;
        var list = [];
        data.sites.forEach(el =>{
            if(list.length +1 < this.sites_amount) {
                list.push(new Site(el));
            }else{
                list.push(new Site(el));
                this.rows.push(list);
                list = [];
            }
        });
    }

    id = 0;
    name = '';
    sites_amount = 0;
    is_vip = false;
    rows = [];
}