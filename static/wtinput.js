$(document).ready(function(){
			$("#livebox").keyup("input",function(e){

				$("#datalist").empty();


				$.ajax({
					method:"post",
					url:"/livesearch",
					data:{text:$("#livebox").val()},
					success:function(res){
						var data = "<ul>";

						$.each(res,function(index,value){
							data += "<li>"+value.WorkoutName+"</li>";
						});

						data += "</ul>";
//						data += "";
						$('#datalist').fadeIn();
						$("#datalist").html(data);
//						$('#datalist2').fadeIn();
//						$("#datalist2").html(data);
					}
				});
			});
			$('#datalist').on('click', 'li', function(){
               $('#livebox').val($(this).text());
               $('#datalist').fadeOut();

          });


		});

