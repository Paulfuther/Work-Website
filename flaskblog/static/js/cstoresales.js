$(document).ready(function () {
    $.ajax({
      url: "http://127.0.0.1:5000/cstoresales",
      method: "GET",
      success: function (newdata) {
      var datenew = [];
      var marginnew = [];  
        for (var i in newdata) {
          datenew.push(newdata[i].date);
          marginnew.push(newdata[i].sales);
          }; 
      var chartdata = {
        labels: datenew,
        datasets: [{
          label: 'C Store Sales',
          data: marginnew,
          backgroundColor: '#b3d9ff',
          }]
          };
      var ctx = $("#storemargin");
      var barGraph = new Chart(ctx, {
          type: 'line',
          data: chartdata, 
            options: {
              legend: {
                display: false
              },
              scales: {
                xAxes: [{
                  gridLines:{
                    display:false
                    },
                    ticks: {
                      beginAtZero: true
                    
                    },
                    type: 'time',
                    distribution: 'series',
                    time: {
                    unit: 'month',
                    
                    displayFormats: {
                     //   'day': 'MMM YY',
                     //   'week': 'MMM YY',
                       month: 'MMM',
                    //    'quarter': 'MMM YY',
                    //    'year': 'MMM YY',
                   //     }, //
                }
              }
             }],
             yAxes:[{
               gridLines:{
                 display:false
               },
               ticks: {
                 beginAtZero: false
               }
             }]
             }
           }
      })
    },
  });
});