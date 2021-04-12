function getSelected() {
  var checkboxes = document.getElementsByName("selectedDashboard");
  var e = document.getElementById("Dashboard");
  var data = {};
  data["type"] = e.options[e.selectedIndex].text;
  data["name"] = document.getElementById("dashboardName").value;
  if(data["name"] == ''){
    Swal.fire({
      icon: "error",
      title: "Dashboard should have a name",
      confirmButtonColor: "#FC6A28",
    });
    return 
  }
  if(data["type"] == "None"){
    Swal.fire({
      icon: "error",
      title: "Select a valid dashboard type",
      confirmButtonColor: "#FC6A28",
    });
    return 
  }
  if(data['type']=='General')
  {
    var kpi = {}
    var chart = {}
    var kpiName = document.querySelectorAll("#kpiName");
    var fun = document.querySelectorAll("#function");
    var columns = document.querySelectorAll("#columns");
    for(var i = 0; i<kpiName.length; i++)
    {
      if(fun[i].options[fun[i].selectedIndex].text.includes('CHART'))
        chart[kpiName[i].value] = {"type": fun[i].options[fun[i].selectedIndex].text, "columns": (columns[i].value).split(',')}
      else
        kpi[kpiName[i].value] = {"operation": fun[i].options[fun[i].selectedIndex].text, "columns": (columns[i].value).split(',')}
    }
    data['kpi'] = kpi
    data['chart'] = chart
    jsonData = JSON.stringify(data);
    console.log(jsonData);
    $.ajax({
      type: "POST",
      url: window.location.origin+"/generate",
      data: jsonData,
      dataType: "json",
    }).done(function (results) {
      if(results.Success)
      {
        Swal.fire({
          icon: "success",
          title: "Dashboard generated successfully",
          confirmButtonColor: "#FC6A28",
        });
      }
      else{
        Swal.fire({
          icon: "error",
          title: "Dashboard with this name already exists",
          confirmButtonColor: "#FC6A28",
        });
      }
    });
  }
  else if(data['type'] == 'POS')
  {
    var selected = [];
    for (var checkbox of checkboxes) {
      if (checkbox.checked) {
        selected.push(checkbox.id);
      }
    }
    data["KPIs"] = selected;
    jsonData = JSON.stringify(data);
    $.ajax({
      type: "POST",
      url: window.location.origin+"/generate",
      data: jsonData,
      dataType: "json",
    }).done(function (results) {
      if(results.Success)
      {
        Swal.fire({
          icon: "success",
          title: "Dashboard generated successfully",
          confirmButtonColor: "#FC6A28",
        });
      }
      else{
        Swal.fire({
          icon: "error",
          title: "Dashboard with this name already exists",
          confirmButtonColor: "#FC6A28",
        });
      }
    });
  }
}

function addKpi(){
  var div = document.getElementById('kpicard');
  var fullcard = document.createElement('div');
  fullcard.innerHTML = '<div class="container"> <div class="selectdiscription">KPI Name</div><input id="kpiName" class="columns" type="text"> </div><div class="container"> <div class="selectdiscription">Function</div><div class="selectKPI" id="selectKPI"> <select id="function"> <option value="Option 1">None</option> <option value="Option 2">SUM</option> <option value="Option 3">AVERAGE</option> <option value="Option 4">ADD</option> <option value="Option 5">SUBTRACT</option> <option value="Option 6">DIVIDE</option> <option value="Option 7">PERCENTAGE</option> <option value="Option 8">BARCHART</option><option value="Option 9">PIECHART</option><option value="Option 10">LINECHART</option> </select> </div></div><div class="container"> <div class="selectdiscription">Columns</div><input id="columns" class="columns" type="text"> </div>'
  fullcard.setAttribute('class', 'fullcard')
  div.appendChild(fullcard)
}