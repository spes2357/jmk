



let myChart = document.getElementById('myChart').getContext('2d');
let myChart2 = document.getElementById('myChart2').getContext('2d');
let myChart3 = document.getElementById('myChart3').getContext('2d');
let myChart4 = document.getElementById('myChart4').getContext('2d');
let myChart5 = document.getElementById('myChart5').getContext('2d');


// Global Options
Chart.defaults.global.defaultFontFamily = 'Lato';
Chart.defaults.global.defaultFontSize = 18;
Chart.defaults.global.defaultFontColor = '#777';

let massPopChart = new Chart(myChart, {
  type:'line', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
  data:{
//    labels:['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge', 'New Bedford'],
    labels: dates1,
    datasets:[{
      label:'sleep hours',
      data: sleephours,
      backgroundColor:[
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)'
      ],
      borderWidth:1,
      borderColor:'#777',
      hoverBorderWidth:3,
      hoverBorderColor:'#000'
    }, {
      label:'Workout Hours',
      data: sumOfworkouthours,
      //backgroundColor:'green',
      backgroundColor:[
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 99, 132, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)'
      ],
      borderWidth:1,
      borderColor:'#777',
      hoverBorderWidth:3,
      hoverBorderColor:'#000'
    }]
  },
  options:{
    responsive: true,
    scales: {
        yAxes: [{
            display: true,
            ticks: {
                beginAtZero: true,
                max: 24,
                min: 0
            }
        }]
    },
    title:{
      display:true,
      text:'Sleep Hours and Workout Hours',
      fontSize:25
    },
    legend:{
      display:true,
      position:'right',
      labels:{
        fontColor:'#000'
      }
    },
    layout:{
      padding:{
        left:50,
        right:0,
        bottom:50,
        top:0
      }
    },
    tooltips:{
      enabled:true
    }
  }
});
let massPopChart2 = new Chart(myChart2, {
  type:'line', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
  data:{
//    labels:['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge', 'New Bedford'],
    labels: dates3,
    datasets:[{
      label:'Sum of Sets',
      data: sumOfworkoutset,
      //backgroundColor:'green',
      backgroundColor:[
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 99, 132, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)'
      ],
      borderWidth:1,
      borderColor:'#777',
      hoverBorderWidth:3,
      hoverBorderColor:'#000'
    },
    {
      label:'Sum of Reps',
      data: sumOfworkoutsetNrep,
      //backgroundColor:'green',
      backgroundColor:[
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)'
      ],
      borderWidth:1,
      borderColor:'#777',
      hoverBorderWidth:3,
      hoverBorderColor:'#000'
    },
    {
      label:'Sum of (Sets * Reps * Weight)',
      data: sumOfworkoutsetNrepNweight,
      //backgroundColor:'green',
      backgroundColor:[
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)'
      ],
      borderWidth:1,
      borderColor:'#777',
      hoverBorderWidth:3,
      hoverBorderColor:'#000'
    }]
  },
  options:{
    responsive: true,
    scales: {
        yAxes: [{
            display: true,
            ticks: {
                beginAtZero: true,
//                max: 1000,
                min: 0
            }
        }]
    },
    title:{
      display:true,
      text:'Volume',
      fontSize:25
    },
    legend:{
      display:true,
      position:'right',
      labels:{
        fontColor:'#000'
      }
    },
    layout:{
      padding:{
        left:50,
        right:0,
        bottom:50,
        top:0
      }
    },
    tooltips:{
      enabled:true
    }
  }
});

let massPopChart3 = new Chart(myChart3, {
  type:'line', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
  data:{
//    labels:['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge', 'New Bedford'],
    labels: dates3,
    datasets:[{
      label:'Intensity',
      data: intensity,
      //backgroundColor:'green',
      backgroundColor:[
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)'
      ],
      borderWidth:1,
      borderColor:'#777',
      hoverBorderWidth:3,
      hoverBorderColor:'#000'
    }]
  },
  options:{
    responsive: true,
    scales: {
        yAxes: [{
            display: true,
            ticks: {
                beginAtZero: true,
//                max: 24
                min: 0
            }
        }]
    },
    title:{
      display:true,
      text:'Intensity (= Sum(Sets * Reps * Weight)/Sum(Workout Hours)) ',
      fontSize:25
    },
    legend:{
      display:true,

      position:'right',
      labels:{
        fontColor:'#000'
      }
    },
    layout:{
      padding:{
        left:50,
        right:0,
        bottom:50,
        top:0
      }
    },
    tooltips:{
      enabled:true
    }
  }
});


let massPopChart4 = new Chart(myChart4, {
    type: 'pie',
    data: {
      labels: ["avgCarb", "avgProtein", "avgFat"],
      datasets: [{
        label: "nutrition",
        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f"],
        data: [nutrition.avgCarb, nutrition.avgProtein, nutrition.avgFat]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Predicted world population (millions) in 2050'
      },
      layout:{
          padding:{
            left:50,
            right:0,
            bottom:50,
            top:0
          }
        }
    }
});

let massPopChart5 =new Chart(myChart5, {
    type: 'bar',
    data: {
      labels: dates4,
      datasets: [
        {
          label: "carb",
          backgroundColor: "#3e95cd",
//          data: [2478,5267,734,784,433]
          data: carb
        },
        {
          label: "protein",
          backgroundColor: "#8e5ea2",
//          data: [2478,5267,734,784,433]
          data: protein
        },
        {
          label: "fat",
          backgroundColor: "#3cba9f",
//          data: [2478,5267,734,784,433]
          data: fat
        }
      ]
    },
    options: {
        responsive: true,
        scales: {
            yAxes: [{
                display: true,
                ticks: {
                    beginAtZero: true,
    //                max: 24
                    min: 0
                }
            }]
        },
      legend: { display: true },
      title: {
        display: true,
        text: 'Nutrition'
      }
    }
});



