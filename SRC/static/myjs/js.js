$(document).ready(function () {
    $("#search_button").click(function () {
        input_text = $('#search').val()
        console.log(input_text)
        // ajax
        // $.post( "{% url 'pages:home' %}",
        $.post("./",
            {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                "inputText": input_text,  // دیتا در فرم وارد شده

            }, function (data) {
                //   console.log('data : ',data)
                //  iziToast.show({
                //       title: 'Hey',
                //      color : 'green',
                //       message: data.message
                //   });
                $('#books_ul li').remove()
               // var inf_book=data.books
              //  if (inf_book != null) {
                    console.log('chek')
                    $.each(data.books, function (index, value) {
                        console.log('index', index)
                        console.log('value', value)

                        $('#books_ul').append(' <li class="list-group"><a href="/product/' + value.id + '">' + value.name + '</a></li>')
                    })
             //   } else {
              //      $('#books_ul').append('<li>محصولی یافت نشد</li>')
             //   }
            }
        );
    });


});
