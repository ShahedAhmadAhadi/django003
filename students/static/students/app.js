let input = document.getElementById('search')
let search_str = ''
let ht = document.getElementById('wrapper').innerHTML
input.addEventListener("keyup",async function () {
    let val = input.value
if (input.value == '') {
    document.getElementById('wrapper').innerHTML = ht
}
    

    fetch(`http://localhost:8000/search/${val}`)
        .then(response => response.json()).then(res => {
            console.log(res)
            document.getElementById('wrapper').innerHTML = ''
            for (i in res){
                document.getElementById('wrapper').innerHTML += `
                <a href="../home/${ res[i]['roll_no'] }">
                <div class="font-bold border-t-2 border-gray-200 px-2 py-3">
                    <span class="w-1/6 ml-2 inline-block"> ${res[i]['name']} </span>
                    <span class="w-1/6 inline-block">${res[i]['f/name']}</span>
                    <span class="w-1/6 inline-block">(+93) - ${res[i]['phone']}</span>
                </div>
            </a>`
                // let li = show.appendChild(document.createElement('li'));
                // let span1 = li.appendChild(document.createElement("span"));
                // let span2 = li.appendChild(document.createElement('span'));
                // span1.appendChild(document.createTextNode(`${res[i]['name']}`))
                // span2.appendChild(document.createTextNode(`${res[i]['f/name']}`))
            } 
        })
        // if (!val) {
        //     document.getElementById('wrapper').innerHTML += `
        //     console.log('a')
        //     {% for student in stu_lst %}
        //             <a href="../home/{{ student.s_roll }}">
        //                 <div class="row font-bold border-t-2 border-gray-200 px-2 py-3">
        //                     <span class="w-1/6 ml-2 inline-block"> {{ student.s_name }} </span>
        //                     <span class="w-1/6 inline-block">{{ student.s_father_name }}</span>
        //                     <span>(+93) - {{ student.s_phone }}</span>
        //                 </div>
        //             </a>
        //             {% endfor %}`
        // }
})
