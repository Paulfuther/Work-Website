$(document).ready(function () {
    $.ajax({
      url: "http://127.0.0.1:5000/cstoresales",
      method: "GET",
      success: function (newdata) {
      var datenew = [];
      var marginnew = [];  
        for (var i in newdata) {
          datenew.push(newdata[i].date);
          marginnew.push(newdata[i].margin);
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
          type: 'bar',
          data: chartdata, 
            options: {
              scales: {
                xAxes: [{
                  gridLines:{
                    display:false
                    },
                    type: 'category',
                    time: {
                    unit: 'month',
                    displayFormats: {
                        'day': 'MMM YY',
                        'week': 'MMM YY',
                        'month': 'MMM YY',
                        'quarter': 'MMM YY',
                        'year': 'MMM YY',
                        },
                }
             }],
             yAxes:[{
               gridLines:{
                 display:false
               },
               ticks: {
                 beginAtZero: true
               }
             }]
             }
           }
      })
    },
  });
});