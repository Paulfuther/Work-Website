$(document).ready(function () {
    $.ajax({
      url: "http://127.0.0.1:5000/cstoresales",
      method: "GET",
      success: function (newdata) {
      var datenew = [];
       
        for (let i=0; i < newdata.length; i++)  //var i in newdata)// 
        {
          datenew.push(newdata[i].date);
        };
      var marginnew = [];
        for (let k = 0; k < newdata.length; k++)
        {
          marginnew.push(newdata[k].sales);
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
                    //distribution: 'series',//
                    time: {
                      parser: "DD-MMM-YYYY HH:mm:ss",
                      unit: 'month',
                    
                      displayFormats: {
                      
                      day: 'MMM YY',
                  
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