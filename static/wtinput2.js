
$(document).ready(function(){
			$("#livebox2").keyup("input",function(e){

				$("#datalist2").empty();

				$.ajax({
					method:"post",
					url:"/livesearch2",
					data:{text:$("#livebox").val()},
					success: function(response){
                        if (response == "FALSE") {
                            var message = "ERROR: something went wrong on the MYSQL side";
                            alert(message);
                        } else {
                            $("#livebox2").val(response.MajorMuscle);
                        }
                     }
//					success:function(res){
//						var data = "<ul>";
//						$.each(res,function(index,value){
//							data += "<li>"+value.MajorMuscle+"</li>";
//						});
//
//						data += "</ul>";
////						data += "";
//						$('#datalist2').fadeIn();
//						$("#datalist2").val(data);
//					}
				});
			});
//			$(document).on('click', 'li', function(){
////               $('#livebox2').val($('#datalist2').text());
//               $('#datalist2').fadeOut();
//
//          });
		});