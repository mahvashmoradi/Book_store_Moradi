   $(document).ready(function () {
    console.log('input_text')

    //   $("#delete_button").click(function () {#}
    console.log('input_text222')

    $.ajax({
    url: "{% url 'accounts:complete-api-info' %}",
    type: 'GET',
    dataType: 'json', // added data type
    success: function (data) {
    console.log(data);
    iziToast.show({
    title: 'Hey',
    color: 'green',
    message: data
    });
    //          $('#discount_place').html(data.total_discount_value)
    $($(this).closest('div')).append('data')
    $.each(data.inf_address, function (index, value) {
    console.log('index', index)
    console.log('value', value)

    $('#address_table').append('<tr><td> '+value.province+'</td><td> '+value.city+'</td><td> '+value.address+'</td><td> '+value.postal_code+'</td><td> '+value.phone_number+'</td><td> '+value.id+'</td><td> '+value.id+'</td></tr>')
    })

    }
    });
    });