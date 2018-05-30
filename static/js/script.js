$(document).ready(function(){
   var btn = $('#show_item');
   var h_item_name = $('#item_name');
   var h_item_type = $('#item_type');
   var h_item_description = $('#item_description');
   var h_item_price = $('#item_price');
   var price_input = $('#price_input');
   var h_item_quantity = $('#item_quantity')
   var quantity_input = $('#quantity_input')
    btn.on('click', function (e) {
     e.preventDefault();
     var item_name = btn.data("item_name");
     var item_description = btn.data("item_description");
     var item_type = btn.data("item_type");
     var item_starting_price = btn.data("item_starting_price")
     var item_quantity = btn.data("item_quantity")
     console.log(item_starting_price)
     h_item_name.text(h_item_name.data("h") + item_name);
     h_item_type.text(h_item_type.data("h") + item_type);
     h_item_description.text(h_item_description.data("h") + item_description);
     h_item_price.text(h_item_price.data("h") + item_starting_price)
     h_item_quantity.text(h_item_quantity.data("h") + item_quantity + " шт.")
     price_input.attr({"min" : item_starting_price})
     quantity_input.attr({ "max" : item_quantity })
    })
});