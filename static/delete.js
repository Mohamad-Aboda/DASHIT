function deleteDashboard() {
    var e = document.getElementById("deleteDashboard");
    var data = {};
    data["name"] = e.options[e.selectedIndex].text;
    jsonData = JSON.stringify(data);
    console.log(jsonData);
    $.ajax({
      type: "POST",
      url: window.location.origin + "/delete",
      data: jsonData,
      dataType: "json",
    }).done(function () {
      Swal.fire({
        icon: "success",
        title: "Dashboard deleted successfully",
        confirmButtonColor: "#FC6A28",
      }).then((result) => {
        if (result.isConfirmed) {
            location.reload();
        }
      });
    });
  }