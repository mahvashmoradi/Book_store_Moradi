function send() {
    var person = {
        name: $("#id-name").val(),
        address: $("#id-address").val(),
        phone: $("#id-phone").val()
    }

    $('#target').html('sending..');

    $.ajax({
        url: '/test/PersonSubmit',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        success: function (data) {
            $('#target').html(data.msg);
        },
        data: JSON.stringify(person)
    });
}


$.ajax({
    url: url,
    type: "POST",
    data: JSON.stringify(data),
    processData: false,
    contentType: "application/json; charset=UTF-8",
    complete: callback
});

////////////////////////////////////////////////////////
const $tableID = $('#table');
const $BTN = $('#export-btn');
const $EXPORT = $('#export');
const newTr = `
<tr class="hide">
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half">
    <span class="table-up"
      ><a href="#!" class="indigo-text"
        ><i class="fas fa-long-arrow-alt-up" aria-hidden="true"></i></a
    ></span>
    <span class="table-down"
      ><a href="#!" class="indigo-text"
        ><i class="fas fa-long-arrow-alt-down" aria-hidden="true"></i></a
    ></span>
  </td>
  <td>
    <span class="table-remove"
      ><button
        type="button"
        class="btn btn-danger btn-rounded btn-sm my-0 waves-effect waves-light"
      >
        Remove
      </button></span
    >
  </td>
</tr>
`;
$('.table-add').on('click', 'i', () => {
    const $clone = $tableID.find('tbody tr').last().clone(true).removeClass('hidetable - line');
    if ($tableID.find('tbody tr').length === 0) {
        $('tbody').append(newTr);
    }
    $tableID.find('table').append($clone);
});
$tableID.on('click', '.table-remove', function () {
    $(this).parents('tr').detach();
});
$tableID.on('click', '.table-up', function () {
    const $row = $(this).parents('tr');
    if
    ($row.index() === 0) {
        return;
    }
    $row.prev().before($row.get(0));
});
$tableID.on('click', '.table-down', function () {
    const $row = $(this).parents('tr');
    $row.next().after($row.get(0));
}); // A few jQuery helpers for exporting only
jQuery.fn.pop = [].pop;
jQuery.fn.shift = [].shift;
$BTN.on('click', () => {
    const $rows =
        $tableID.find('tr:not(:hidden)');
    const headers = [];
    const data = []; // Get the headers(add special header logic here )
    $($rows.shift()).find('th:not(:empty)').each(function () {
        headers.push($(this).text().toLowerCase());
    }); // Turn all existing rows into a loopable array
    $rows.each(function () {
        const $td = $(this).find('td');
        const h = {}; // Use the headers from earlier to name our hash keys
        headers.forEach((header, i) => {
            h[header] =
                $td.eq(i).text();
        });
        data.push(h);
    }); // Output the result
    $EXPORT.text(JSON.stringify(data));
});
/////////////////////////////////////////////////////////////////////
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

                $('#address_table').append('<tr><td>' + (index + 1) + '</td><td> ' + value.province + '</td><td> ' + value.city + '</td><td> ' + value.address + '</td><td> ' + value.postal_code + '</td><td> ' + value.phone_number + '</td><td> ' + value.id + '</td><td> ' + value.id + '</td></tr>')
            })

        }
    });
});
/////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////

/////////////////////////////////////

////////////////////////////////////////
$(document).ready(function () {
    console.log('input_text')

    const tableID = $('#table');
    var count = tableID.find('tbody tr').length + 1
    const newTr = `
    <tr class="hide">
            <td class="pt-3-half"> {{ count }}</td>
        <td class="pt-3-half"><input type="text" id="province{{ count }}"></td>
        <td class="pt-3-half"><input type="text" id="city{{ count }}"></td>
        <td class="pt-3-half"><input type="text" id="address{{ count }}"></td>
        <td class="pt-3-half"><input type="text" id="postal{{ count }}"></td>
        <td class="pt-3-half"><input type="text" id="phone{{ count }}"></td>

        <td>
    <span class="table-remove"
    ><button
            type="button"
            class="btn btn-danger btn-rounded btn-sm my-0 waves-effect waves-light"
    >
        پاک کردن
      </button></span
    >
        </td>
        <td class="pt-3-half"></td>

    </tr>
    `;

    console.log(count)
    $('.table-add').on('click', 'i', () => {
        $('tbody').append(newTr);
    });
    tableID.on('click', '.table-remove', function () {
        $(this).parents('tr').detach();
    });
    // $EXPORT.text(JSON.stringify(data));
    //     name: $("#name").val(),
    const data = [];


    $("#edit_button").click(function () {
        for (let i = 1; i < count; i++) {

            info_address = {
                province: $("#province" + i).val(),
                city: $("#city" + i).val(),
                address: $("#address" + i).val(),
                postal: $("#postal" + i).val(),
                phone: $("#phone" + i).val()
            }
            //  text += cars[i] + "<br>";
            console.log(info_address)
            data.push(info_address)
        }

        console.log(data)
        send_data = {
            first_name: $("#first_name").val(),
            last_name: $("#last_name").val(),
            gender: $("#gender").val(),
            inf_address: data
        }
        console.log(send_data)

        $.ajax({
            url: "{% url 'accounts:complete-api-info' %}",
            type: "POST",
            data: JSON.stringify(send_data),
            processData: false,
            contentType: "application/json; charset=UTF-8",
            complete: callback
        });

    });
});
/////////////////////////////////////
$.ajax({
    url: url,
    type: "POST",
    data: JSON.stringify(data),
    processData: false,
    contentType: "application/json; charset=UTF-8",
    complete: callback
});
////////////////////////////////////////


    $(document).ready(function () {
    console.log('input_text')

    const tableID = $('#table');
    var count = tableID.find('tbody tr').length + 1
    const newTr = `
    <tr class="hide">
        <td class="pt-3-half"> {{ count }}</td>
        <td class="pt-3-half"><input type="text" id="province{{ count }}"></td>
        <td class="pt-3-half"><input type="text" id="city{{ count }}"></td>
        <td class="pt-3-half"><input type="text" id="address{{ count }}"></td>
        <td class="pt-3-half"><input type="text" id="postal{{ count }}"></td>
        <td class="pt-3-half"><input type="text" id="phone{{ count }}"></td>

        <td>
    <span class="table-remove"
    ><button
            type="button"
            class="btn btn-danger btn-rounded btn-sm my-0 waves-effect waves-light"
    >
        پاک کردن
      </button></span
    >
        </td>
        <td class="pt-3-half"></td>

    </tr>
    `;

    console.log(count)
    $('.table-add').on('click', 'i', () => {
    $('tbody').append(newTr);
    });
    tableID.on('click', '.table-remove', function () {
    $(this).parents('tr').detach();
    });
    // $EXPORT.text(JSON.stringify(data));
    //     name: $("#name").val(),
    const data = [];


    $("#edit_button").click(function () {
    for (let i = 1; i < count; i++) {

    info_address = {
    province: $("#province" + i).val(),
    city: $("#city" + i).val(),
    address: $("#address" + i).val(),
    postal: $("#postal" + i).val(),
    phone: $("#phone" + i).val()
    }
    //  text += cars[i] + "<br>";
    console.log(info_address)
    data.push(info_address)
    }

    console.log(data)
    send_data = {
    first_name: $("#first_name").val(),
    last_name: $("#last_name").val(),
    gender: $("#gender").val(),
    inf_address: data
    }
    console.log(send_data)

       $.post( "./",
    {
    csrfmiddlewaretoken: '{{ csrf_token }}',
    "inputText": send_data,  // دیتا در فرم وارد شده

    } ,function( data ) {
    //   console.log('data : ',data)
    //  iziToast.show({
    //       title: 'Hey',
    //      color : 'green',
    //       message: data.message
    //   });
    $('#books_ul li').remove()
   if (data.books.length > 0){
    $.each(data.books,function(index,value){
    console.log('index',index)
    console.log('value',value)

  $('#books_ul').append(' <li class="list-group"><a href="/product/'+value.id+'">'+value.name+'</a></li>')
        })}
        else{
        $('#books_ul').append('<li class="list-group">محصولی یافت نشد</li>')
   };


    }

    );
     task= document.getElementById('search');
    task.value=null;
    });


    });
///////////////////////////////////////////////////////




    $(document).ready(function () {
    const newTr = `
    <div class="row">
        <div class="col-2">
            <input class="form-check-input" type="radio" name="flexRadioDefault" value="" id="flexRadioDefault2"
                   checked>
        </div>
        <div class="col-10">
            <label class="form-check-label" for="flexRadioDefault2" id="label_select">
            </label></div></div>
        `;
        $("#new_address").click(function(){

        // ajax
        $.post( "{% url 'payment:select-address' %}",
        {
        csrfmiddlewaretoken: '{{ csrf_token }}',
        province: $("#province").val(),
        city: $("#city").val(),
        address: $("#address").val(),
        postal: $("#postal").val(),
        phone: $("#phone").val()
        } ,function( data ) {
        // console.log('data : ',data)
        // iziToast.show({
        // title: 'Hey',
        // color : 'green',
        // message: data.message
        // });

        console.log(data.message)

        $("#add_item").append(newTr)
        $("#label_select").append(''+postal.value+', '+address.value+',,'+city.value+','+province.value+'')
        $("#flexRadioDefault2").value =data.message

        // $("#add_item").append('<input class="form-check-input" type="radio" name="flexRadioDefault"
        //                                 value="data.message" id="flexRadioDefault2" checked>')

        // $("#add_item").append('<label class="form-check-label" for="flexRadioDefault2">
       // '+province.value+','+city.value+','+postal.value+', '+address.value+','+phone.value+',</label>')
        // })}
        // else{
        // $('#books_ul').append('
       // <li class="list-group">محصولی یافت نشد</li>
       // ')
        }

        );
        // task= document.getElementById('search');
        // task.value=null;
        });


        });
//////////////////////////////////////////////////////

    $(document).ready(function () {
    console.log('input_text')

    const tableID = $('#table');
    var count = tableID.find('tbody tr').length + 1
    const newTr = `
    <tr class="hide">
        <td class="pt-3-half"> {{ count }}</td>
        <td class="pt-3-half"><input type="text" id="province{{ count }}"></td>
        <td class="pt-3-half"><input type="text" id="city{{ count }}"></td>
        <td class="pt-3-half"><input type="text" id="address{{ count }}"></td>
        <td class="pt-3-half"><input type="text" id="postal{{ count }}"></td>
        <td class="pt-3-half"><input type="text" id="phone{{ count }}"></td>

        <td>
    <span class="table-remove"
    ><button
            type="button"
            class="btn btn-danger btn-rounded btn-sm my-0 waves-effect waves-light"
    >
        پاک کردن
      </button></span
    >
        </td>
        <td class="pt-3-half"></td>

    </tr>
    `;

    console.log(count)
        function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
    console.log('ok')
    $('.table-add').on('click', 'i', () => {
    $('tbody').append(newTr);
    });
    tableID.on('click', '.table-remove', function () {
    $(this).parents('tr').detach();
    });
    // $EXPORT.text(JSON.stringify(data));
    //     name: $("#name").val(),
    const data = [];


    $("#edit_button").click(function () {
    for (let i = 1; i < count; i++) {

    info_address = {
    province: $("#province" + i).val(),
    city: $("#city" + i).val(),
    address: $("#address" + i).val(),
    postal: $("#postal" + i).val(),
    phone: $("#phone" + i).val()
    }
    //  text += cars[i] + "<br>";
    console.log(info_address)
    data.push(info_address)
    }

    console.log(data)
    send_data = {
    first_name: $("#first_name").val(),
    last_name: $("#last_name").val(),
    gender: $("#gender").val(),
    inf_address: data
    }
    console.log(send_data)

    console.log(csrftoken)
    console.log('csrftoken')
    $.ajax({
    url: "{% url 'accounts:complete-api-info' %}",
    type: "PUT",
    headers: {'X-CSRFToken': csrftoken},
    data: JSON.stringify(send_data),
    //  data: { "data":JSON.stringify(send_data)},

    processData: false,
    contentType: "application/json; charset=UTF-8",
    });

    });
    });
