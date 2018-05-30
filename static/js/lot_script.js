$(document).ready(function(){
 var count_item = $('#count_input');
 var cost_item=$('#cost_item');
 var cost = parseInt(cost_item.val());         
 
 var amount =$('#amount');
 
 var count_plus = $('#count_plus');
 var count_minus = $('#count_minus');

 var count_value = count_item.val();
     count_value = parseInt(count_value);

 var max_count_lot = $('#max_count_lot');
 var max_value = max_count_lot.val();
     max_value = parseInt(max_value);
     
 EnablePlusButton();
 EnableMinusButton();
 count_plus.on('click', function (e) {
     e.preventDefault();
     //var amount_value = amount.val();
     //console.log(amount_value)
     //amount.attr('value', amount.val() + 1)
     count_value = count_item.val();
     count_value = parseInt(count_value) + 1;
     count_item.attr('value', count_value);
     EnablePlusButton();
     EnableMinusButton();
     AmountCost();

 });
 count_minus.on('click', function (e) {
     e.preventDefault();
     count_value = count_item.val();
     count_value = parseInt(count_value) - 1;
     count_item.attr('value', count_value);
     EnablePlusButton();
     EnableMinusButton();
     AmountCost();
 })

 function EnablePlusButton() {
     if (count_value == max_value)
      {
        count_plus.hide();
      }
     else
      {
        count_plus.show();
      }

 }

 function EnableMinusButton() {
     if (count_value == 1)
      {
        count_minus.hide();
      }
     else
      {
        count_minus.show();
      }

 }
 
 function AmountCost() {
     amount.text("ИТОГОВАЯ ЦЕНА:" + " " + cost*count_value + " у.е.");
 }

});