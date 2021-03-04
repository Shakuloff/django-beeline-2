// Sorting table
function sortTable(n, self) {
    let table_header_items = document.querySelectorAll(".table-header");

//Цикл для изменения стрелок
    for (let i = 0; i < table_header_items.length; i++) {
        table_header_items[i].classList.remove("desc")
        table_header_items[i].classList.add("asc")
    }


    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("table");
    switching = true;
    dir = "asc";
    self.classList.remove("desc")
    self.classList.add("asc")
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];
            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
                self.classList.remove("asc")
                self.classList.add("desc")
            }
        }
    }
}


//функция проверки на введенные символы
function check_min(event) {
    let input = document.getElementById("search-input").value;
    let form = document.getElementById("search-form");

    if (input.length >= 3) {
        form.submit();
    } else {
        // form.onsubmit = "return false";
        alert("Поиск не должен состоять из менее чем 3х символов ")
        event.preventDefault()
        // console.log(e)
        return false;
    }

}

//TreeView
var toggler = document.getElementsByClassName("box");
var i;

for (i = 0; i < toggler.length; i++) {
    toggler[i].addEventListener("click", function () {
        this.parentElement.querySelector(".nested").classList.toggle("active");
        this.classList.toggle("check-box");
    });
}

function getPathNameCountryAndCity(){
    let pathName = window.location.pathname.split('/')
    let mainbox = document.getElementsByClassName('main-country-filter')
    let mainested = document.getElementsByClassName('main-nested')
    if (pathName[1] == 'country'){
        let boxId = 'countryid=' + pathName[2]
        let box = document.getElementById(boxId)
        let link = document.getElementsByClassName(boxId)
        link[0].classList.toggle("active-btn")
        mainbox[0].classList.toggle("check-box")
        mainested[0].classList.toggle("active")
        box.classList.toggle("check-box")
        box.parentElement.querySelector(".nested").classList.toggle("active");
    } else if (pathName[1] == 'city'){
        let boxId = 'cityid=' + pathName[2]
        let box = document.getElementById(boxId)
        box.classList.toggle("active-btn")
        mainbox[0].classList.toggle("check-box")
        mainested[0].classList.toggle("active")
        let parent = box.closest(".nested").classList.toggle("active");
        let parent2 = box.parentElement.parentElement.parentElement.querySelector(".box").classList.toggle("check-box")
    }


}
getPathNameCountryAndCity()

function getPathNameJob(){
    let pathName = window.location.pathname.split('/')
    let mainbox = document.getElementsByClassName('main-job-filter')
    let main_nested_job = document.getElementsByClassName('main-nested-job')
    // console.log(pathName[1])
    if (pathName[1] == 'job'){
        // console.log(mainbox[0])
        let encode = decodeURIComponent(pathName[2])
        let boxId = 'jobname=' + encode
        let link = document.getElementsByClassName(boxId)
        console.log(boxId, link)
        link[0].classList.toggle("active-btn")
        mainbox[0].classList.toggle("check-box")
        main_nested_job[0].classList.toggle("active")
    }


}
getPathNameJob()

function getPathName_search_filter(){
    let pathName = window.location.pathname.split('/')
    let mainbox = document.getElementsByClassName('main-detail-filter')
    let main_nested_job = document.getElementsByClassName('main-nested-detail')
    // console.log(pathName[1])
    if (pathName[1] == 'search_filter'){
        // console.log(mainbox[0])
        let encode = decodeURIComponent(pathName[2])
        let boxId = 'jobname=' + encode
        mainbox[0].classList.toggle("check-box")
        main_nested_job[0].classList.toggle("active")
    }


}
getPathName_search_filter()


function slider() {
    var slider = document.getElementById("SalaryRange");
    var output = document.getElementById("output");
    output.innerHTML = slider.value; // Display the default slider value

    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function() {
      output.innerHTML = this.value;
}

}
slider()
// function save() {
//     let fav, favs = [];
//     let tree_items = document.querySelectorAll(".box");
//     tree_items.forEach(function () {
//         fav = {id: $(this).attr('id'), value: $(this).prop('checked')};
//         favs.push(fav);
//     })
//     localStorage.setItem("favorites", JSON.stringify(favs));
//     console.log(favs)
// }


// $('.box').on('click', function() {
//   var fav, favs = [];
//   $('.box').each(function() { // run through each of the checkboxes
//     fav = {id: $(this).attr('id'), value: $(this).prop('checked')};
//     favs.push(fav);
//   });
//   localStorage.setItem("favorites", JSON.stringify(favs));
// });

// $(document).ready(function () {
//     var favorites = JSON.parse(localStorage.getItem('favorites'));
//     if (!favorites.length) {
//         return
//     }
//     ;
//     console.debug(favorites);
//
//     for (var i = 0; i < favorites.length; i++) {
//         console.debug(favorites[i].value == 'on');
//         $('#' + favorites[i].id).prop('checked', favorites[i].value);
//     }
// });

// document.addEventListener("DOMContentLoaded", function () {
//     let favorites = JSON.parse(localStorage.getItem('favorites'));
//     if (!favorites.length) {
//         return
//     }
//     ;
//     console.debug(favorites);
//
//     for (let i = 0; i < favorites.length; i++) {
//         console.debug(favorites[i].value == 'on');
//         $('#' + favorites[i].id).prop('checked', favorites[i].value);
//     }
// })

 // $(function () {
 //
 //      var $populationChart = $("#population-chart");
 //      $.ajax({
 //        url: $populationChart.data("url"),
 //        success: function (data) {
 //            console.log(data)
 //          var ctx = $populationChart[0].getContext("2d");
 //
 //          new Chart(ctx, {
 //            type: 'bar',
 //            data: {
 //              labels: data.labels,
 //              datasets: [{
 //                label: 'Population',
 //                backgroundColor: 'blue',
 //                data: data.data
 //              }]
 //            },
 //            options: {
 //              responsive: true,
 //              legend: {
 //                position: 'top',
 //              },
 //              title: {
 //                display: true,
 //                text: 'Population Bar Chart'
 //              }
 //            }
 //          });
 //
 //        }
 //      });
 //
 //    });



// function ajaxSend() {
//     // Отправляем запрос
//     fetch(`population-chart`, {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded',
//         },
//     })
//         .then(response => response.json())
//         .then(json => render(json))
//         .catch(error => console.error(error))
// }
// ajaxSend()

function render (json){
    console.log(json)
}