// console.log('working')
// const MonthNames=["jan","feb","march","april","may","jun","july","August","Sep","October","November","December"]
// $('#commentForm').submit(function(e){
// e.preventDefault();
// let dt=new Date();
// let time=dt.getDay()+''+MonthNames[dt.getUTCMonth()]+''+dt.getFullYear()
// $.ajax({
//     data:$(this).serialize(),
//     method:$(this).attr('method'),
//     url:$(this).attr('action'),
//     dataType:'json',
//     success:function(response){
//         console.log('comment saved to db')
//         if(response.bool==true){
//             $('#review_res').html('reviewed successfully')
//             $('.comment_form_hide').hide()
//             $('.add_review').hide()

//             let _html = '<div class="single-comment justify-content-between d-flex mb-30">'
//             _html  +=     ' <div class="user justify-content-between d-flex">'
//             _html  +=   '<div class="thumb text-center">'
//             _html  +=   '<img src="https://isobarscience-1bfd8.kxcdn.com/wp-content/uploads/2020/09/default-profile-picture1.jpg" alt="" />'
//             _html  +=   '<a href="#" class="font-heading text-brand">'+ response.context.user +'</a>'
//             _html  +=   '</div>'
//             _html  +=   '<div class="desc">'
//             _html  +=   '<div class="d-flex justify-content-between mb-10">'
//             _html  +=   '<div class="d-flex align-items-center">'
//             _html  +=   '<span class="font-xs text-muted">'+ time +'</span>'
//             _html  +=   ' </div>'
//             for(var i=1; i<=response.context.rating; i++){
//                 _html += '<i class="fas fa-star text-warning"></i>';
//             }
//             _html  +=   '</div>'
//             _html  +=    '<p class="mb-10">'+response.context.review +'</p>'
//             _html  +=  '</div>'
//             _html  +=   '</div>'
//             _html  +=  ' </div>'
//             $('.comment-list').prepend(_html)
//         }
//     }
// })
// })
console.log('working');
const MonthNames=["jan","feb","march","april","may","jun","july","August","Sep","October","November","December"]
$('#commentForm').submit(function(e){
    e.preventDefault()
    let dt=new Date()
    let time=dt.getDay()+''+MonthNames[dt.getUTCMonth()]+''+dt.getFullYear()
    $.ajax({
        data:$(this).serialize(),
        method:$(this).attr('method'),
        url:$(this).attr('action'),
        dataType:'json',
        sucess:function(response){
            console.log('saved to db')
            if(response.bool==true){
                $('#comment_form_hide').hide()
                $('.review_res').hide()
              let _html=  '<div class="single-comment justify-content-between d-flex mb-30">'
              _html +=  '<div class="user justify-content-between d-flex">'
                   _html +=  '<div class="thumb text-center">'
                   _html +=      '<img src="https://isobarscience-1bfd8.kxcdn.com/wp-content/uploads/2020/09/default-profile-picture1.jpg" alt="" />'
                   _html +=      '<a href="#" class="font-heading text-brand">'+ response.context.user +'</a>'
                    _html += '</div>'
                    _html += '<div class="desc">'
                    _html +=     '<div class="d-flex justify-content-between mb-10">'
                    _html +=         '<div class="d-flex align-items-center">'
                    _html +=             '<span class="font-xs text-muted">'+time + '</span>'
                    _html +=         '</div>'
                           for (var i=1; i<=response.context.rating;i++){
                            _html +='<i class="fas fa-star text-warning"></i>'
                           }
                      _html +=  ' </div>'
                      _html +=   '<p class="mb-10">'+response.context.review+ '</p>'
                  _html +=   '</div>'
               _html +=  '</div>'
           _html +=  '</div>'
           $('#comment-list').prepend(_html)
            }
        }
    })
})


