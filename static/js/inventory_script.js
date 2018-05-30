$(document).ready(function(){
    var min_price = parseInt($('#price_input').val());
    var max_quantity = parseInt($('#item_quantity').data("h"));
    var lot_button = $('#create_lot_button');
    var lot_name = $('#lot_name_input').val();
    var name_enable = false;
    var price_enable = true;
    var quantity_enable = true;
    LotButtonEnable();
$('#price_input').change(function (e) {
    e.preventDefault();
    var price = parseInt($('#price_input').val())
    if (price <= min_price)
     {
       price_enable = false;
       LotButtonEnable();
     }
    else
     {
       price_enable = true;
       LotButtonEnable();
     }
});

$('#quantity_input').change(function (e) {
    e.preventDefault();
    var quantity = parseInt($('#quantity_input').val());
    if (quantity <= 0 || quantity > max_quantity)
     {
       quantity_enable = false;
       LotButtonEnable();
     }
    else
     {
       quantity_enable = true;
       LotButtonEnable();
     }
});

$('#lot_name_input').change(function (e) {
   e.preventDefault();
   lot_name = $('#lot_name_input').val();
   if(lot_name == "")
     {
       name_enable = false;
       LotButtonEnable();
     }
    else
     {
       name_enable = true;
       LotButtonEnable();
     }
});

function LotButtonEnable() {
    if(name_enable & quantity_enable & price_enable)
     {
        lot_button.prop('disabled', false);
     }
    else
     {
        lot_button.prop('disabled', true);
     }
}

});