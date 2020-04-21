$(document).ready(function () {
    $.ajax({
      url: "http://127.0.0.1:5000/cstoresales",
      method: "GET",
      success: function (newdata) {

        console.log(newdata);
    
      //var labels =[];
      //var data=[];

      //labels = newdata.jsonarray.map(function (e) {
       // return e.date});
       
      //data = newdata.jsonarray.map(function (e) {
       //return e.margin});

     //console.log(labels); 

      var datenew = [];
      var marginnew = [];
      
      for (var i in newdata) {
        datenew.push(newdata[i].date);
        marginnew.push(newdata[i].margin);
      };


      
      
      console.log(datenew);
      

      var chartdata = {
        //labels: ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],
        labels: datenew,
        datasets: [
        {
          label: 'C Store Margin Dollars',
          data: marginnew,
          backgroundColor: '#b3d9ff',
          borderColor: 'blue',
        }
      ]
      };

      var ctx = $("#storemargin");

      var barGraph = new Chart(ctx, 
        {
        type: 'bar',
        data: chartdata, 
           options: {
             scales: {
               xAxes: [{
                 
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
             }]
             }
           }
      });

    },
      error: function(data) {
        console.log(data);
      }
  });
});