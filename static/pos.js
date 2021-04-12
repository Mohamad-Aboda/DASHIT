function totalSales(results) {
  var total = parseInt(results.totalSales[0]);
  var now = parseInt(results.totalSales[1]);
  var last = parseInt(results.totalSales[2]);

  var element = document.getElementById("totalSales");
  element.innerHTML = "";
  var tag = document.createElement("h2");
  var text = document.createTextNode(total);
  tag.appendChild(text);
  element.appendChild(tag);
  var subelement = element.parentElement.parentElement.parentElement.parentElement.parentElement
  var subtag = document.createElement("h5");
  if(now>=last){
    var subtext = document.createTextNode("↑ " + (((now-last)/now)*100).toFixed(2) + '%');
    subtag.appendChild(subtext);
    subelement.appendChild(subtag);
    subelement.style.color='#0DA65F';
    subelement.style.backgroundImage = "url('../static/img/green.svg')";
    subelement.style.backgroundSize = "cover";
  }
  else{
    var subtext = document.createTextNode("↓ " + (((last-now)/last)*100).toFixed(2) +'%');
    subtag.appendChild(subtext);
    subelement.appendChild(subtag);
    subelement.style.color='#BF1140';
    subelement.style.backgroundImage = "url('../static/img/red.svg')";
    subelement.style.backgroundSize = "cover";
  }
  
}

function averageInventoryAmount(results) {
  var total = parseInt(results.averageInventoryAmount[0]);
  var last = parseInt(results.averageInventoryAmount[1]);
  var element = document.getElementById("averageInventoryAmount");
  element.innerHTML = "";
  var tag = document.createElement("h2");
  var text = document.createTextNode(total);
  tag.appendChild(text);
  element.appendChild(tag);
  var subelement = element.parentElement.parentElement.parentElement.parentElement.parentElement
  var subtag = document.createElement("h5");
  if(total>=last){
    var subtext = document.createTextNode("↑ "+ (((total-last)/total)*100).toFixed(2) + '%');
    subtag.appendChild(subtext);
    subelement.appendChild(subtag);
    subelement.style.color='#0DA65F';
    subelement.style.backgroundImage = "url('../static/img/green.svg')";
    subelement.style.backgroundSize = "cover";
  }
  else{
    var subtext = document.createTextNode("↓ "+ (((last-total)/last)*100).toFixed(2) + '%');
    subtag.appendChild(subtext);
    subelement.appendChild(subtag);
    subelement.style.color='#BF1140';
    subelement.style.backgroundImage = "url('../static/img/red.svg')";
    subelement.style.backgroundSize = "cover";
  }
}

function totalOnhandAmount(results) {
  var total = parseInt(results.totalOnhandAmount[0]);
  var last = parseInt(results.totalOnhandAmount[1]);
  var element = document.getElementById("totalOnhandAmount");
  element.innerHTML = "";
  var tag = document.createElement("h2");
  var text = document.createTextNode(total);
  tag.appendChild(text);
  element.appendChild(tag);
  var subelement = element.parentElement.parentElement.parentElement.parentElement.parentElement
  var subtag = document.createElement("h5");
  if(total>=last){
    var subtext = document.createTextNode("↑ "+ (((total-last)/total)*100).toFixed(2) + '%');
    subtag.appendChild(subtext);
    subelement.appendChild(subtag);
    subelement.style.color='#0DA65F';
    subelement.style.backgroundImage = "url('../static/img/green.svg')";
    subelement.style.backgroundSize = "cover";
  }
  else{
    var subtext = document.createTextNode("↓ "+ (((last-total)/last)*100).toFixed(2) + '%');
    subtag.appendChild(subtext);
    subelement.appendChild(subtag);
    subelement.style.color='#BF1140';
    subelement.style.backgroundImage = "url('../static/img/red.svg')";
    subelement.style.backgroundSize = "cover";
  }
}

function salesPerStore(results) {
  var total = parseInt(results.salesPerStore[0]);
  var last = parseInt(results.salesPerStore[1]);
  var element = document.getElementById("salesPerStore");
  element.innerHTML = "";
  var tag = document.createElement("h2");
  var text = document.createTextNode(total);
  tag.appendChild(text);
  element.appendChild(tag);
  var subelement = element.parentElement.parentElement.parentElement.parentElement.parentElement
  var subtag = document.createElement("h5");
  if(total>last){
    var subtext = document.createTextNode("↑ "+ (((total-last)/total)*100).toFixed(2) + '%');
    subtag.appendChild(subtext);
    subelement.appendChild(subtag);
    subelement.style.color='#0DA65F';
    subelement.style.backgroundImage = "url('../static/img/green.svg')";
    subelement.style.backgroundSize = "cover";
  }
  else{
    var subtext = document.createTextNode("↓ "+ (((last-total)/last)*100).toFixed(2) + '%');
    subtag.appendChild(subtext);
    subelement.appendChild(subtag);
    subelement.style.color='#BF1140';
    subelement.style.backgroundImage = "url('../static/img/red.svg')";
    subelement.style.backgroundSize = "cover";
  }
}

function distinctProductsSold(results) {
  var total = parseInt(results.distinctProductsSold[0]);
  var last = parseInt(results.distinctProductsSold[1]);
  var element = document.getElementById("distinctProductsSold");
  element.innerHTML = "";
  var tag = document.createElement("h2");
  var text = document.createTextNode(total);
  tag.appendChild(text);
  element.appendChild(tag);
  var subelement = element.parentElement.parentElement.parentElement.parentElement.parentElement
  if(total>=last){
    subelement.style.color='#0DA65F';
    subelement.style.backgroundImage = "url('../static/img/green.svg')";
    subelement.style.backgroundSize = "cover";
  }
  else{
    subelement.style.color='#BF1140';
    subelement.style.backgroundImage = "url('../static/img/red.svg')";
    subelement.style.backgroundSize = "cover";
  }
}

function outOfStock(results) {
  var total = parseInt(results.outOfStock[0]);
  var last = parseInt(results.outOfStock[1]);
  var element = document.getElementById("outOfStock");
  element.innerHTML = "";
  var tag = document.createElement("h2");
  var text = document.createTextNode(total);
  tag.appendChild(text);
  element.appendChild(tag);
  var subelement = element.parentElement.parentElement.parentElement.parentElement.parentElement
  if(total<=last){
    subelement.style.color='#0DA65F';
    subelement.style.backgroundImage = "url('../static/img/green.svg')";
    subelement.style.backgroundSize = "cover";
  }
  else{
    subelement.style.color='#BF1140';
    subelement.style.backgroundImage = "url('../static/img/red.svg')";
    subelement.style.backgroundSize = "cover";
  }
}

function totalsalesPerDay(results) {
  var myChart = echarts.init(
    document.getElementById("totalsalesperday"),
    null,
    { renderer: "svg" }
  );

  // specify chart configuration item and data
  option = {
    toolbox: {
      show: true,
      feature: {
        saveAsImage: {
          title: "save",
        },
      },
    },
    title: {
      text: "Total Sales Per Day",
    },
    xAxis: {
      type: "category",
      data: results.totalsalesPerDay.index,
    },
    tooltip: {
      trigger: "axis",
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        data: results.totalsalesPerDay.data,
        type: "line",
      },
    ],
  };
  // use configuration item and data specified to show chart
  myChart.setOption(option);
  window.addEventListener("resize", function () {
    myChart.resize();
  });
}

function totalsalesPerCountry(results) {
  var chartDom = document.getElementById("totalsalespercountry");
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
      text: "Total Sales Per Country",
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
        data: results.totalsalesPerCountry.index,
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
        type: "bar",
        barWidth: "60%",
        data: results.totalsalesPerCountry.data,
      },
    ],
  };
  option && myChart.setOption(option);
  window.addEventListener("resize", function () {
    myChart.resize();
  });
}

function totalsalesPerCity(results) {
  var chartDom = document.getElementById("totalsalespercity");
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
      text: "Total Sales Per City",
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
        data: results.totalsalesPerCity.index,
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
        type: "bar",
        barWidth: "60%",
        data: results.totalsalesPerCity.data,
      },
    ],
  };
  option && myChart.setOption(option);
  window.addEventListener("resize", function () {
    myChart.resize();
  });
}

function totalsalesPerStore(results) {
  var chartDom = document.getElementById("totalsalesperstore");
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
      text: "Total Sales Per Store",
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
        data: results.totalsalesPerStore.index,
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
        type: "bar",
        barWidth: "60%",
        data: results.totalsalesPerStore.data,
      },
    ],
  };
  option && myChart.setOption(option);
  window.addEventListener("resize", function () {
    myChart.resize();
  });
}

function topProducts(results) {
  var chartDom = document.getElementById("topproducts");
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
      text: "Top Products",
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
        data: results.topProducts.index,
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
        type: "bar",
        barWidth: "60%",
        data: results.topProducts.data,
      },
    ],
  };
  option && myChart.setOption(option);
  window.addEventListener("resize", function () {
    myChart.resize();
  });
}

function topBrands(results) {
  var chartDom = document.getElementById("topbrands");
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
      text: "Top Brands",
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
        data: results.topBrands.index,
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
        type: "bar",
        barWidth: "60%",
        data: results.topBrands.data,
      },
    ],
  };
  option && myChart.setOption(option);
  window.addEventListener("resize", function () {
    myChart.resize();
  });
}

function salesPercentageForBrand(results) {
  var count = Object.keys(results.salesPercentageForBrand.data).length;
  var values = [["value", "name"]];
  for (let i = 1; i <= count; i++) {
    values.push([
      results.salesPercentageForBrand.data[i - 1],
      results.salesPercentageForBrand.index[i - 1],
    ]);
  }
  var chartDom = document.getElementById("salespercentageforbrand");
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

function getData() {
  var getData = $.get("/data/pos/"+document.title);
  getData.done(function (results) {
    try{
      totalsalesPerDay(results);
    }
    catch(err){
      console.log(err);
    }
    try{
      totalsalesPerCountry(results);
    }
    catch(err){
      console.log(err);
    }
    try{
      topProducts(results);
    }
    catch(err){
      console.log(err);
    }
    try{
      topBrands(results);
    }
    catch(err){
      console.log(err);
    }
    try{
      salesPercentageForBrand(results);
    }
    catch(err){
      console.log(err);
    }
    try{
      totalsalesPerCity(results);
    }
    catch(err){
      console.log(err);
    }
    try{
      totalsalesPerStore(results);
    }
    catch(err){
      console.log(err);
    }
    try{
      totalSales(results);
    }
    catch(err){
      console.log(err);
    }
    try{
      averageInventoryAmount(results);
    }
    catch(err){
      console.log(err);
    }
    try{
      totalOnhandAmount(results);
    }
    catch(err){
      console.log(err);
    }
    try{
      salesPerStore(results);
    }
    catch(err){
      console.log(err);
    }
    try{
      distinctProductsSold(results);
    }
    catch(err){
      console.log(err);
    }
    try{
      outOfStock(results);
    }
    catch(err){
      console.log(err);
    }
  });
}

function filter() {
  var data = {};
  var e = document.getElementById("brand");
  data["Brand"] = e.options[e.selectedIndex].text;
  var e = document.getElementById("city");
  data["City"] = e.options[e.selectedIndex].text;
  var e = document.getElementById("product");
  data["Product"] = e.options[e.selectedIndex].text;
  var e = document.getElementById("store");
  data["Store"] = e.options[e.selectedIndex].text;
  var e = document.getElementById("country");
  data["Country"] = e.options[e.selectedIndex].text;
  var e = document.getElementById("startdate");
  data["StartDate"] = e.value;
  var e = document.getElementById("enddate");
  data["EndDate"] = e.value;
  jsonData = JSON.stringify(data);
  $.ajax({
    type: "POST",
    url: window.location.origin+"/filter/pos/"+ document.title,
    data: jsonData,
    dataType: "json",
  })
    .done(function (results) {
      $('h5').each(function(){$(this).remove()});
      try{
        totalsalesPerDay(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        totalsalesPerCountry(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        topProducts(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        topBrands(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        salesPercentageForBrand(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        totalsalesPerCity(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        totalsalesPerStore(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        totalSales(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        averageInventoryAmount(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        totalOnhandAmount(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        salesPerStore(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        distinctProductsSold(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        outOfStock(results);
      }
      catch(err){
        console.log(err);
      }
    })
    .done(function () {
      $(".counter").each(function () {
        $(this)
          .prop("Counter", 0)
          .animate(
            {
              Counter: $(this).text(),
            },
            {
              duration: 500,
              easing: "swing",
              step: function (now) {
                $(this).text(Math.ceil(now));
              },
            }
          );
      });
    });
}

function filterOption() {
  var getData = $.get("/data/pos/"+document.title);
  getData.done(function (results) {
    country = results.totalsalesPerCountry.index;
    cities = results.totalsalesPerCity.index;
    stores = results.totalsalesPerStore.index;
    brands = results.salesPercentageForBrand.index;
    products = results.topProducts.index;
    addOptions("country", country);
    addOptions("city", cities);
    addOptions("store", stores);
    addOptions("brand", brands);
    addOptions("product", products);
  });
}

function addOptions(element, arrOptions) {
  var e = document.getElementById(element);
  for (let i = 0; i < arrOptions.length; i++) {
    var option = document.createElement("option");
    option.text = arrOptions[i];
    e.add(option);
  }
}
