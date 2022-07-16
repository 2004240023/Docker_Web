let flag  = true;
function change_table(){
    table_obj = document.getElementById('table_id');
    if ( flag ) {
        table_obj.style.backgroundColor = "red";    
        flag = false;
    }else{
        table_obj.style.backgroundColor = "";
        flag = true;
    }
    
    
}

function change_by_select(select) {
    table_obj = document.getElementById('table_id');
    if( select.value == "" ){
        table_obj.style.backgroundColor = "";
    }else if( select.value == "red") {
        table_obj.style.backgroundColor = "red";
    }else{
        table_obj.style.backgroundColor = "blue";
    }
}