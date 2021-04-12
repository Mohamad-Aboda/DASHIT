function createHalfCard(title, content) {
  var halfcards = document.getElementById("halfcards");
  var halfcard = document.createElement("div");
  halfcard.innerHTML =
    '<div class="averageSales"><div class="halfcardcontent" style = "padding-top: 25px;"><div class="count_content"><h6>' +
    title +
    '</h6><span class="counter" id="' +
    title +
    '"><h2>' +
    content +
    "</h2></span></div></div></div>";
  halfcard.setAttribute("class", "halfcard");
  halfcard.style.backgroundImage = "url('../static/img/green.svg')";
  halfcards.appendChild(halfcard);
}
function createCard(title) {
  var cards = document.getElementById("cards");
  var card = document.createElement("div");
  card.setAttribute("class", "card");
  card.setAttribute("id", title);
  cards.appendChild(card);
}
function createDoubleCard(title) {
  var cards = document.getElementById("cards");
  var card = document.createElement("div");
  card.setAttribute("class", "doubleCard");
  card.setAttribute("id", title);
  cards.appendChild(card);
}

function createCHART(title, x, y, chartType) {
  var chartDom = document.getElementById(title);
  var myChart = echarts.init(chartDom, null, { renderer: "svg" });
  var option;

  option = {
    toolbox: {
      show: true,
      feature: {
        saveAsImage: {
          title: "save",
          type: "svg",
        },
      },
    },
    title: {
      text: title,
    },
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "shadow",
      },
    },
    grid: {
      left: "3%",
      right: "4%",
      bottom: "3%",
      containLabel: true,
    },
    xAxis: [
      {
        type: "category",
        data: x,
        axisTick: {
          alignWithLabel: true,
        },
      },
    ],
    yAxis: [
      {
        type: "value",
      },
    ],
    series: [
      {
        type: chartType,
        barWidth: "60%",
        data: y,
      },
    ],
  };
  option && myChart.setOption(option);
  window.addEventListener("resize", function () {
    myChart.resize();
  });
}

function createPICHART(title, x, y){
  var count = x.length;
  var values = [["value", "name"]];
  for (let i = 1; i <= count; i++) {
    values.push([
      y[i-1],
      x[i-1],
    ]);
  }
  console.log(values);
  var chartDom = document.getElementById(title);
  var myChart = echarts.init(chartDom, null, { renderer: "svg" });
  var option;
  option = {
    toolbox: {
      show: true,
      feature: {
        saveAsImage: {
          title: "save",
          type: "svg",
        },
      },
    },
    title: {
      text: "Sales Percentage For Brand",
      left: "center",
    },
    tooltip: {
      trigger: "item",
    },
    legend: {
      orient: "vertical",
      left: "left",
    },
    series: [
      {
        type: "pie",
        radius: "70%",
        data: arrToObject(values),
        emphasis: {
          itemStyle: {
            shadowBlur: 5,
            shadowOffsetX: 0,
            shadowColor: "rgba(0, 0, 0, 0.5)",
          },
        },
      },
    ],
  };
  option && myChart.setOption(option);
  window.addEventListener("resize", function () {
    myChart.resize();
  });
}

function arrToObject(arr) {
  //assuming header
  var keys = arr[0];
  //vacate keys from main array
  var newArr = arr.slice(1, arr.length);

  var formatted = [],
    data = newArr,
    cols = keys,
    l = cols.length;
  for (var i = 0; i < data.length; i++) {
    var d = data[i],
      o = {};
    for (var j = 0; j < l; j++) o[cols[j]] = d[j];
    formatted.push(o);
  }
  return formatted;
}

function createGraph(title, type, x, y) {
  if (type == "BARCHART") createCHART(title, x, y, 'bar');
  if (type == "LINECHART") createCHART(title, x, y, 'line');
  if (type == "PIECHART") createPICHART(title, x, y);
  console.log(title);
}

function getData() {
  var getData = $.get("/data/general/" + document.title);
  getData.done(function (results) {
    for (const key in results.kpi) {
      console.log(`${key} : ${results.kpi[key]}`);
      createHalfCard(key, results.kpi[key]);
    }
    for (const key in results.chart) {
      if(results.chart[key].type == 'PIECHART')
        createDoubleCard(key)
      else
        createCard(key);
      
    }
    for (const key in results.chart) {
      createGraph(
        key,
        results.chart[key].type,
        results.chart[key].index,
        results.chart[key].data
      );
    }
  });
}
