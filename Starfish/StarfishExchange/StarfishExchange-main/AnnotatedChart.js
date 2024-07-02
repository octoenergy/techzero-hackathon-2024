// var series = {
//   value: [
//   ],
//   datetime: [
//   ]
// };
var series = {
    value: [
      8107.85,
      8128.0,
      8122.9,
      8165.5,
      8340.7,
      8423.7,
      8423.5,
      8514.3,
      8481.35,
      8487.7,
      8885.1,
      9340.85,
      9340.85,
      9467.3
    ],
    datetime: [
      "13 Nov 2017",
      "14 Nov 2017",
      "15 Nov 2017",
      "16 Nov 2017",
      "17 Nov 2017",
      "20 Nov 2017",
      "21 Nov 2017",
      "22 Nov 2017",
      "23 Nov 2017",
      "24 Nov 2017",
      "27 Nov 2017",
      "28 Nov 2017",
      "29 Nov 2017",
      "30 Nov 2017"
    ]
};

var options = {
  series: [{
  data: series.value
}],
  chart: {
  height: 350,
  type: 'line',
  id: 'areachart-2',
  reversed: false
},
annotations: {
  yaxis: [{
    y: 8200,
    borderColor: '#00E396',
    label: {
      borderColor: '#00E396',
      style: {
        color: '#fff',
        background: '#00E396',
      },
      text: 'Support',
    }
  }, {
    y: 8600,
    y2: 9000,
    borderColor: '#000',
    fillColor: '#FEB019',
    opacity: 0.2,
    label: {
      borderColor: '#333',
      style: {
        fontSize: '10px',
        color: '#333',
        background: '#FEB019',
      },
      text: 'Y-axis range',
    }
  }],
  xaxis: [{
    x: new Date('23 Nov 2017').getTime(),
    strokeDashArray: 0,
    borderColor: '#775DD0',
    label: {
      borderColor: '#775DD0',
      style: {
        color: '#fff',
        background: '#775DD0',
      },
      text: 'Anno Test',
    }
  }, {
    x: new Date('3 Nov 2017').getTime(),
    x2: new Date('28 Nov 2017').getTime(),
    fillColor: '#B3F7CA',
    opacity: 0.4,
    label: {
      borderColor: '#B3F7CA',
      style: {
        fontSize: '10px',
        color: '#fff',
        background: '#00E396',
      },
      offsetY: -10,
      text: 'X-axis range',
    }
  }],
  points: [{
    x: new Date('01 Dec 2017').getTime(),
    y: 8607.55,
    marker: {
      size: 8,
      fillColor: '#fff',
      strokeColor: 'red',
      radius: 2,
      cssClass: 'apexcharts-custom-class'
    },
    label: {
      borderColor: '#FF4560',
      offsetY: 0,
      style: {
        color: '#fff',
        background: '#FF4560',
      },

      text: 'Point Annotation',
    }
  }, {
    x: new Date('08 Dec 2017').getTime(),
    y: 9340.85,
    marker: {
      size: 0
    },
    image: {
      path: '../../assets/images/ico-instagram.png'
    }
  }]
},
dataLabels: {
  enabled: false
},
stroke: {
  curve: 'straight'
},
grid: {
  padding: {
    right: 30,
    left: 20
  }
},
title: {
  text: 'UK Energy Prices from Octopus Energy Agile Tariff API',
  align: 'left'
},
labels: series.datetime,
yaxis: {
  labels: {
    formatter: function (value) {
      return value + "p / kWh";
    }
  },
},
xaxis: {
  type: 'datetime',
  labels: {
    // formatter: function (value) {
    //   return value;
    // }
    datetimeFormatter: {
      year: 'yyyy',
      month: 'MMM \'yy',
      day: 'dd MMM',
      hour: 'HH:mm'
    }
  }
},
};

document.addEventListener('DOMContentLoaded', function() {
  var chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();

  var url = 'https://zuzanakovacsova--starfish-get-tariff.modal.run/';

  let series;

  fetch(url)
    .then(response => response.json())
    .then(series => {
      console.log('Data stored in series:', series);
      chart.updateSeries([{
        data: series
      }])
    })
    .catch(error => console.error('Error:', error));

});

