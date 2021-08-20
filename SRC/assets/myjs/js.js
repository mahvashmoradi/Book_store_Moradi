
    $(document).ready(function () {
        console.log('inputText')

    $("#search_button").click(function(){
    inputText = $('#search').val()
    console.log(inputText)
    // ajax
    $.post( "{% url 'ajax-sample' %}",
    {
    csrfmiddlewaretoken: '{{ csrf_token }}',
    "inputText": inputText,  // دیتا در فرم وارد شده

    } ,function( data ) {
    //   console.log('data : ',data)
    //  iziToast.show({
    //       title: 'Hey',
    //      color : 'green',
    //       message: data.message
    //   });
    $('#books li').remove()
    $.each(data.books,function(index,value){
    console.log('index',index)
    console.log('value',value)

    $('#books').append(' <li>'+value.question+'</li>')
    })
    }

    );
    });
    });
