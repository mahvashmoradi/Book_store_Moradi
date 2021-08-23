
    $(document).ready(function () {
    $("#coupon_button").click(function(){
    input_text = $('#coupon').val()
    console.log(input_text)
    // ajax
     $.post( "{% url 'payment:cart' %}",
     // $.post( "./")
    {
    csrfmiddlewaretoken: '{{ csrf_token }}',
    "inputText": input_text,  // دیتا در فرم وارد شده

    } ,function( data ) {
      iziToast.show({
           title: 'Hi',
          color : 'green',
           message: data.message
       });
  $('#discount_place').html(data.total_discount_value)
    }

    );
     task= document.getElementById('coupon');
    task.value=null;
    });

    });