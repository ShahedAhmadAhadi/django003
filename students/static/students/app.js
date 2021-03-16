let input = document.getElementById("search");
let search_str = "";
let initial = document.getElementById("wrapper").innerHTML;
if (input.value == "") {
    document.getElementById("wrapper").innerHTML = initial;
}

let data = {}

let search = async function(page = 1) {
    let val = input.value;
        // console.log(page);
        fetch(`http://localhost:8001/search/?text=${val}&page=${page}`)
            .then((response) => response.json())
            .then((res) => JSON.parse(res.res))
            .then((res) => {
                console.log(res);
                document.getElementById("wrapper").innerHTML = "";
                if (Object.getOwnPropertyNames(res).length < 1) {
                    document.getElementById(
                        "wrapper"
                    ).innerHTML += `<div class="justify-self-center self-center font-bold text-4xl text-purple-200 py-44">No Result</div>`;
                    console.log("emptyr");
                } else if (res) {
                    for (i in res) {
                        document.getElementById("wrapper").innerHTML += `
                    <a href="../home/${res[i]["pk"]}" class="hover:bg-gray-100">
                    <div class="font-bold border-t-2 border-gray-200 px-2 py-3">
                        <span class="w-1/6 ml-2 inline-block"> ${res[i]["fields"]["s_name"]} </span>
                        <span class="w-1/6 inline-block">${res[i]["fields"]["s_father_name"]}</span>
                        <span class="w-1/6 inline-block">(+93) - ${res[i]["fields"]["s_phone"]}</span>
                    </div>
                </a>`;
                    }
                    document.getElementById("wrapper").innerHTML += `
                <div class="pagination row font-bold border-t-2 border-gray-200 px-2 py-3 text-blue-600">
                        <span class="step-links  block text-center">
                            {% if page_obj.has_previous %}
                                <a href="?page=1" class="mx-2">First / </a>
                                <a href="?page={{ page_obj.previous_page_number }}" class="mx-2">{{page_obj.previous_page_number}} / </a>
                            {% endif %}
                            <span class="current mx-2 bg-blue-600 rounded px-6 text-white py-1.5">{{ page_obj.number }}</span>


                            {% if page_obj.has_next %}
                            <a id='second' class="mx-2">{{page_obj.next_page_number}}  <span> / </span> </a>

                            <span>
                                ...
                            </span>

                            <a href="?page={{ page_obj.paginator.num_pages }}" class="mx-2">/ Last</a>
                            {% endif %}
                        </span>
                    </div>
                </div>`;
                }
                document
                    .getElementById("second")
                    .addEventListener("click", () => {
                        search(1);
                        console.log("object");
                    });
            });
}

input.addEventListener('keyup', console.log('clik'));


// function search(page=1) {
//     console.log('aldfjl')
//     input.addEventListener("keyup", async function () {
//         let val = input.value;
//         // console.log(page);
//         fetch(`http://localhost:8001/search/?text=${val}&page=${page}`)
//             .then((response) => response.json())
//             .then((res) => JSON.parse(res.res))
//             .then((res) => {
//                 console.log(res);
//                 document.getElementById("wrapper").innerHTML = "";
//                 if (Object.getOwnPropertyNames(res).length < 1) {
//                     document.getElementById(
//                         "wrapper"
//                     ).innerHTML += `<div class="justify-self-center self-center font-bold text-4xl text-purple-200 py-44">No Result</div>`;
//                     console.log("emptyr");
//                 } else if (res) {
//                     for (i in res) {
//                         document.getElementById("wrapper").innerHTML += `
//                     <a href="../home/${res[i]["pk"]}" class="hover:bg-gray-100">
//                     <div class="font-bold border-t-2 border-gray-200 px-2 py-3">
//                         <span class="w-1/6 ml-2 inline-block"> ${res[i]["fields"]["s_name"]} </span>
//                         <span class="w-1/6 inline-block">${res[i]["fields"]["s_father_name"]}</span>
//                         <span class="w-1/6 inline-block">(+93) - ${res[i]["fields"]["s_phone"]}</span>
//                     </div>
//                 </a>`;
//                     }
//                     document.getElementById("wrapper").innerHTML += `
//                 <div class="pagination row font-bold border-t-2 border-gray-200 px-2 py-3 text-blue-600">
//                         <span class="step-links  block text-center">
//                             {% if page_obj.has_previous %}
//                                 <a href="?page=1" class="mx-2">First / </a>
//                                 <a href="?page={{ page_obj.previous_page_number }}" class="mx-2">{{page_obj.previous_page_number}} / </a>
//                             {% endif %}
//                             <span class="current mx-2 bg-blue-600 rounded px-6 text-white py-1.5">{{ page_obj.number }}</span>


//                             {% if page_obj.has_next %}
//                             <a id='second' class="mx-2">{{page_obj.next_page_number}}  <span> / </span> </a>

//                             <span>
//                                 ...
//                             </span>

//                             <a href="?page={{ page_obj.paginator.num_pages }}" class="mx-2">/ Last</a>
//                             {% endif %}
//                         </span>
//                     </div>
//                 </div>`;
//                 }
//                 document
//                     .getElementById("second")
//                     .addEventListener("click", () => {
//                         search(1);
//                         console.log("object");
//                     });
//             });
//     });
// }

// search();
