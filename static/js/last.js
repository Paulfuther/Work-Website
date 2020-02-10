$(document).ready(function(){
    $.ajax({
      url: "http://127.0.0.1:5000/data",
      method: "GET",
      success: function(newdata2) {
    
      

      var date2 = [];
      var volume2 = [];
      //var date3=[];
      //var volume3 =[];
  
      for(var i in newdata2) {
      //if (i < 8){
          date2.push(newdata2[i].date);
          volume2.push(newdata2[i].volume);
      }
      //else
      //  {
         // date3.push(newdata2[i].date)
        //  volume3.push(newdata2[i].volume)    
       // }
        //console.log(date2)
        //console.log(volume2)
        //console.log(date3)
        //console.log(volume3)
      

        var chartdata = {
          labels: ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],
          //labels: date3,
          datasets : [
           // {
            //  label: 'last year',
            //  data: volume2,
            //  backgroundColor: '#b3d9ff',
              
          // },
            {
              label: 'this year',
              backgroundColor: 'red',
              data: volume2,
            }
          ]
        };
  
       var ctx = $("#mycanvas");

        var barGraph = new Chart(ctx, {
          type: 'bar',
          data: chartdata,
          options: {
            responsive:true,
            scales: {
              xAxes: [{
               // type: 'time',
               // distribution: 'series',
                time: {
                  unit: 'month',
                  
                  //min: date3[0],
              
                  displayFormats: {
                   
                    'day': 'MMM YY',
                    'month': 'MMM YY',
                    'quarter': 'MMM YY',
                    'year': 'MMM YY',
                  }
                },
                ticks: {
                  source: 'data',
                  beginAtZero: true
                }
               }],
                  yAxes: [{
                    ticks: {
                      beginAtZero: true
                    }
                }]
            }
            }
        });
      },
     
    });
  });