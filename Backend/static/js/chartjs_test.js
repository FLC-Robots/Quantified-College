var intervalID = setInterval(updateChart, 1000);
var c = 0;
var temp;
var $SCRIPT_ROOT = "{{ request.script_root|tojson|safe }}";

function updateChart() {
  $.getJSON(
    $SCRIPT_ROOT + "/data",

    function (data) {
      console.log(data);
      temp = data.num;
    }
  );

  c = c + 1;
  myChart.data.labels.push(c);
  myChart.data.datasets.forEach((dataset) => {
    dataset.data.push(temp);
  });
  myChart.update();
}

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: [c],
    datasets: [
      {
        label: "Temperature",
        data: [temp],
        backgroundColor: ["rgba(255, 99, 132, 0.2)"],
        borderColor: ["rgba(255,99,132,1)"],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
  },
});
