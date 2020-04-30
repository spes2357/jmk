document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    plugins: [ 'interaction', 'dayGrid', 'timeGrid' ],
    defaultView: 'dayGridMonth',
    defaultDate: '2020-04-07',
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay, addEventButton'
    },
    events: '/calendarsetting',
    customButtons: {
        addEventButton: {
              text: 'Delete Day Record',
              click: function () {
                  var dateStr = prompt('Enter date in YYYY-MM-DD format');
                  var date = moment(dateStr);
                  if (date.isValid()) {
                      alert("You wrote "+dateStr);
                      var xhr = new XMLHttpRequest();
                      xhr.open("POST", "/deletedate", true);
                      xhr.setRequestHeader('Content-Type', "application/x-www-form-urlencoded");
                      var  postVars = 'dateStr='+dateStr;
                      xhr.send(postVars);
                      calendar.render();
                  }
                  else{alert('Invalid Date');}
//                  if (dateStr != null) {
//                    alert("You wrote "+dateStr);
//
//                  }
            }
        }
    }
  });

  calendar.render();
});


//$(document).ready(function() {
//   var calendar = $('#calendar').fullCalendar({
//    editable:true,
//    header:{
//     left:'prev,next today',
//     center:'title',
//     right:'month,agendaWeek,agendaDay'
//    },
//    events:'/calendarsetting'
//    alert("Added Successfully")
//   });
//  });